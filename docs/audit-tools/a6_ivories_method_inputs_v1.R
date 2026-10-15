#!/usr/bin/env Rscript
# A6 independent input-method reconciliation: base R, read-only source, private output.
# Usage: Rscript audit-tools/a6_ivories_method_inputs_v1.R downloads/official/levantine_corpus_gansell.csv
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) stop("Provide exactly one local source CSV path")
src <- normalizePath(args[[1]], mustWork = TRUE)
outdir <- file.path("downloads", "private-review", "a6-ivories")
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)
expected_sha <- "d52ed8033ad7304024e207e02117d2cc1b425da8799e582858dac8a6b0b90941"
sha <- NA_character_
if (nzchar(Sys.which("shasum"))) {
  h <- system2("shasum", c("-a", "256", shQuote(src)), stdout=TRUE)
  if (length(h)) sha <- strsplit(trimws(h[1]), "[[:space:]]+")[[1]][1]
}
df <- read.csv(src, check.names=FALSE, stringsAsFactors=FALSE, na.strings=c("", " "), fileEncoding="UTF-8")
n <- nrow(df)
m <- ncol(df)
missing <- function(x) is.na(x) | trimws(as.character(x)) == ""
missing_by_col <- vapply(df, function(z) sum(missing(z)), integer(1))
vals <- data.frame(test=character(), status=character(), evidence=character(),stringsAsFactors=FALSE)
check <- function(test,ok,evidence) {
  vals[nrow(vals)+1,] <<- list(test,if(isTRUE(ok)) "PASS" else "FAIL",as.character(evidence))
  cat(if(isTRUE(ok)) "PASS" else "FAIL","|",test,"|",evidence,"\n")
}
check("SHA-256 matches locally verified fixed official CSV", identical(sha,expected_sha),if(is.na(sha))"shasum unavailable" else sha)
check("162 rows and 34 columns", n==162L && m==34L,paste(n,"rows;",m,"columns"))
check("Key and Site names", identical(names(df)[1:2],c("Key","Site")),paste(names(df)[1:2],collapse=", "))
check("Key unique and populated", all(!missing(df$Key)) && anyDuplicated(df$Key)==0L,"unique record IDs")
check("Site has five labels",length(unique(df$Site[!missing(df$Site)]))==5L,"distinct sites")
check("32 model feature columns after Key and Site",m-2L==32L,"12 candidate numeric + 20 candidate categorical")
check("12 numerical feature values parse",all(vapply(df[3:14],function(v){z<-as.character(v)[!missing(v)];all(!is.na(suppressWarnings(as.numeric(z))))},logical(1))),"columns 3–14")
check("20 categorical feature columns",length(df[15:34])==20L,"columns 15–34")
miss_features <- sum(missing_by_col[-(1:2)])
rate <- miss_features/(n*(m-2L))
check("1931 missing model-feature values",miss_features==1931L,paste("missing",miss_features))
check("Feature missing rate about 37 percent",abs(rate-0.3725)<0.001,paste("observed",sprintf("%.4f%%",100*rate)))
check("Site and Key are not part of predictor matrix",all(names(df)[3:34]!="Site") && all(names(df)[3:34]!="Key"),"model candidate indices 3–34")
site_tab <- table(df$Site)
check("Site label distribution matches prior audit",
 identical(as.integer(site_tab[c("Nimrud","ArslanTash","Khorsabad","SharifKhan","Nineveh")]),as.integer(c(126,26,7,2,1))),
 "aggregate distribution; no object identities exported")
# Explicitly do not cluster, impute, export the 162 records or infer missingness mechanism.
fields <- data.frame(field=names(df),kind=c("record_id","site",rep("numeric_candidate",12),rep("categorical_candidate",20)),
 missing=missing_by_col,available=n-missing_by_col,stringsAsFactors=FALSE)
groups <- split(seq_len(n),df$Site)
summary <- data.frame(site=names(groups),records=vapply(groups,length,integer(1)),
  missing_input_cells=vapply(groups,function(ii)sum(vapply(df[ii,3:34,drop=FALSE],function(z)sum(missing(z)),integer(1))),integer(1)),
  stringsAsFactors=FALSE)
summary$missing_rate <- summary$missing_input_cells/(summary$records*32)
write.csv(vals,file.path(outdir,"A6_METHOD_CHECKS_PRIVATE.csv"),row.names=FALSE)
write.csv(fields,file.path(outdir,"A6_METHOD_FIELDS_PRIVATE.csv"),row.names=FALSE)
write.csv(summary,file.path(outdir,"A6_METHOD_SITE_MISSING_PRIVATE.csv"),row.names=FALSE)
report <- c("# A6 method-input PRIVATE QA", "",
 paste("SHA-256:",sha),paste("Candidate predictors: 32; missing fraction:",sprintf("%.4f%%",100*rate)),
 paste("Checks:",sum(vals$status=="PASS"),"PASS /",sum(vals$status=="FAIL"),"FAIL"),"",
 "Limitations:", "- This verifies only model input structure, not the historic model output.",
 "- Paper reports 33 features; audited runner excludes Site and uses 32 predictors; unresolved.",
 "- Missing values were not imputed; source CSV not modified or publicly exported.",
 "- Per-site table contains aggregates only; it must remain private until reviewed."
)
writeLines(report,file.path(outdir,"A6_METHOD_REPORT_PRIVATE.md"))
ok <- all(vals$status=="PASS")
cat("\nOVERALL:",if(ok)"PASS" else "FAIL","—",sum(vals$status=="PASS"),"PASS /",sum(vals$status=="FAIL"),"FAIL\n")
cat("PRIVATE outputs:",outdir,"\n")
if (!ok) quit(status=1)
