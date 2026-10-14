"""Reproduce the PREPARED teaching example using synthetic data only.

Dependencies: pandas, scikit-learn.
The output is a toy clustering exercise, not archaeological evidence.
"""
from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA

folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "rim_morphometrics_synthetic.csv")
cols = ["rim_diameter_cm", "rim_thickness_cm", "rim_angle_deg"]
X = StandardScaler().fit_transform(df[cols])
km = KMeans(n_clusters=2, random_state=42, n_init=20).fit_predict(X)
ward = AgglomerativeClustering(n_clusters=2, linkage="ward").fit_predict(X)
pca = PCA(n_components=2).fit_transform(X)
out = pd.DataFrame({
    "artifact_id": df["artifact_id"],
    "illustrative_manual_type": df["illustrative_manual_type"],
    "kmeans_k2_label": km,
    "ward_k2_label": ward,
    "pc1": pca[:, 0],
    "pc2": pca[:, 1],
})
out.to_csv(folder / "reproduced_clusters_with_pca.csv", index=False, encoding="utf-8-sig")
print(out.to_string(index=False))
print("Toy result: cluster numbers are arbitrary and do not signify real types.")
