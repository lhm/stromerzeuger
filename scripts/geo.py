import pandas as pd
import geopandas as gpd
from utils import root

df = pd.read_csv(root / "data" / "nettonennleistung.csv", dtype={"AGS": "object"})

gdf = gpd.read_file(root / "files" / "gemeinden-sn.json")
gdf = gdf[["id", "GEN", "BEZ", "AGS_0", "geometry"]]
gdf.columns = ["id", "Name", "Bezeichnung", "AGS", "geometry"]

result = gdf.merge(df, on="AGS", how="left")
result.to_file(root / "data" / "nettonennleistung.json", driver="GeoJSON")
