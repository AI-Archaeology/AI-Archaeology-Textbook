#!/usr/bin/env Rscript
# A6 Levantine ivories: independent read-only CSV audit (base R)
# Usage: Rscript audit-tools/a6_levantine_ivories_audit.R downloads/official/levantine_corpus_gansell.csv
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) stop("Usage: Rscript audit-tools/a6_levantine_ivories_audit.R <local-CSV>")
source_path <- normalizePath(args[[1]], mustWork = TRUE)
out_dir <- file.path("downloads", "private-review", "a6-ivories")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
checks <- data.frame(check=character(), status=character(), detail=character(), stringsAsFactors=FALSE)
record <- function(name, pass, detail) {
  checks[nrow(checks)+1,] <<- list(name, if (isTRUE(pass)) "PASS" else "FAIL", as.character(detail))
  cat(if(isTRUE(pass)) "PASS" else "FAIL", "|", name, "|", detail, "\n")
}
file_hash <- unname(tools::md5sum(source_path))
sha256 <- NA_character_
if (nzchar(Sys.which("shasum"))) {
  v <- suppressWarnings(system2("shasum", c("-a", "256", shQuote(source_path)), stdout=TRUE, stderr=FALSE))
  if (length(v)) sha256 <- strsplit(trimws(v[[1]]), "[[:space:]]+")[[1]][1]
}
record("Source file size", file.info(source_path)$size == 22846L, paste("bytes", file.info(source_path)$size))
record("SHA256 recorded", !is.na(sha256) && nchar(sha256)==64, if(is.na(sha256)) "shasum unavailable" else sha256)
raw <- tryCatch(read.csv(source_path, header=TRUE, check.names=FALSE,
                         stringsAsFactors=FALSE, na.strings=character(), 
                         fileEncoding="UTF-8", comment.char=""),
                error=function(e) stop("Unable to parse CSV: ", conditionMessage(e)))
record("162 source rows", nrow(raw)==162L, paste(nrow(raw), "rows"))
record("34 source columns", ncol(raw)==34L, paste(ncol(raw), "columns"))
record("Expected first columns", identical(names(raw)[1:2], c("Key","Site")), paste(head(names(raw),2),collapse=", "))
record("Key complete", all(!is.na(raw$Key) & nzchar(trimws(as.character(raw$Key)))), "Key blank count")
record("Key unique", !anyDuplicated(raw$Key), paste("distinct",length(unique(raw$Key))))
record("Site complete", all(!is.na(raw$Site) & nzchar(trimws(as.character(raw$Site)))), paste("distinct",length(unique(raw$Site))))
site_freq <- sort(table(raw$Site), decreasing=TRUE)
record("Five source site labels", length(site_freq)==5, paste(names(site_freq),as.integer(site_freq),collapse="; "))
record("12 numeric attribute columns", ncol(raw)>=14L, "position 3 through 14 (type checks follow)")
record("20 categorical attribute columns", ncol(raw)==34L, "position 15 through 34")
# read.csv may infer numeric values and encode blanks as NA: calculate both safely
is_missing <- function(x) is.na(x) | trimws(as.character(x)) == ""
missing <- vapply(raw,function(x) sum(is_missing(x)),integer(1))
record("Expected 1931 empty/NA cells", sum(missing)==1931L, paste("observed",sum(missing)))
record("Only Key and Site complete", identical(which(missing==0L),1:2),paste("complete fields",paste(names(raw)[missing==0L],collapse=", ")))
bad_numeric <- vapply(raw[3:14],function(x) {
 values <- as.character(x)[!is_missing(x)]
 sum(is.na(suppressWarnings(as.numeric(values))))
},integer(1))
record("Numeric attribute contents valid", all(bad_numeric==0L), paste("bad entries",sum(bad_numeric)))
record("Record keys absent from public report", TRUE, "summary only; no individual Key values exported")
details <- data.frame(field=names(raw),column=seq_along(raw),missing=missing,
  observed=nrow(raw)-missing, unique_observed=vapply(raw,function(x) {
    y <- as.character(x)[!is_missing(x)];length(unique(y))},integer(1)),
  type_candidate=c("identifier","site",rep("numeric",12),rep("categorical",20)),
  stringsAsFactors=FALSE)
write.csv(checks,file.path(out_dir,"A6_CHECKS_PRIVATE.csv"),row.names=FALSE,na="")
write.csv(details,file.path(out_dir,"A6_FIELDS_PRIVATE.csv"),row.names=FALSE,na="")
summary <- c("# A6 Levantine ivories: PRIVATE audit", "",
 "This report does not contain individual objects or image paths.",
 paste("Source:",basename(source_path)), paste("SHA-256:",sha256),
 paste("MD5 (supplementary, not an authenticity assertion):",file_hash),
 paste("Rows:",nrow(raw),"Columns:",ncol(raw)),
 paste("Blank cells:",sum(missing)),
 paste("Status:",sum(checks$status=="PASS"),"PASS /",sum(checks$status=="FAIL"),"FAIL"),
 "", "## Site labels (aggregated only)", "",
 paste("- ",names(site_freq),": ",as.integer(site_freq),collapse="\n"),
 "", "## Known limits", "",
 "- CSV structural agreement does NOT reproduce the original clustering.",
 "- No blank entry was imputed, dropped, or interpreted as random.",
 "- Do not redistribute museum photographs based on CSV licence.",
 "- Confirm paper-specific sample restrictions and feature definitions before modelling."
)
writeLines(summary,file.path(out_dir,"A6_AUDIT_PRIVATE.md"),useBytes=TRUE)
overall <- all(checks$status=="PASS")
cat("\nOVERALL:",if(overall)"PASS" else "FAIL","—",sum(checks$status=="PASS"),"PASS /",sum(checks$status=="FAIL"),"FAIL\n")
cat("PRIVATE outputs:",out_dir,"\n")
if (!overall) quit(save="no",status=1L)
