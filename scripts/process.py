import pandas as pd
from utils import root

cols = {
    "MaStR-Nr. der Einheit": "string",
    "Betriebs-Status": "category",
    "Energieträger": "string",
    "Bruttoleistung der Einheit": "float",
    "Nettonennleistung der Einheit": "float",
    "Gemeindeschlüssel": "string",
}

df = pd.read_csv(
    root / "files" / "mastr-sample-ags-147-2014f.csv",
    sep=";",
    decimal=",",
    thousands=".",
    usecols=cols.keys(),
    dtype=cols,
)

subset = df[["Gemeindeschlüssel", "Energieträger", "Nettonennleistung der Einheit"]]
subset.columns = ["AGS", "Energieträger", "Nettonennleistung"]

grouped = subset.groupby(["AGS", "Energieträger"])
stats = grouped.agg({"Nettonennleistung": "sum"})

pivoted = stats.unstack(level=-1)
pivoted.columns = pivoted.columns.get_level_values(1)

totals = subset.groupby("AGS").agg({"Nettonennleistung": "sum"})
totals.columns = ["Gesamt"]

result = pivoted.merge(totals, left_index=True, right_index=True)
result = result.round(2)

result.to_csv(root / "data" / "nettonennleistung.csv")
