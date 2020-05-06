import pandas as pd
from utils import root

df = pd.read_parquet(root / "data" / "raw.parquet")

subset = df[["ENH_Gemeindeschluessel", "ENH_EinheitenTyp", "ENH_Nettonennleistung"]]
subset.columns = ["AGS", "Energieträger", "Nettonennleistung"]

# Filter for SN
subset = subset[subset["AGS"].str.startswith("14")]

# Filter for producers only
producers = [
    "Solareinheit",
    "Stromspeichereinheit",
    "Biomasse",
    "Verbrennung",
    "Windeinheit",
    "Wasser",
    "Gasverbrauchseinheit",
    "Geothermie",
]
subset = subset[subset["Energieträger"].isin(producers)]

# Group by AGS and calculate totals per energy source
grouped = subset.groupby(["AGS", "Energieträger"])
stats = grouped.agg({"Nettonennleistung": "sum"})

pivoted = stats.unstack(level=-1)
pivoted.columns = pivoted.columns.get_level_values(1)

# Caculate totals per AGS
totals = subset.groupby("AGS").agg({"Nettonennleistung": "sum"})
totals.columns = ["Gesamt"]

# Append totals and save result
result = pivoted.merge(totals, left_index=True, right_index=True)
result = result.round(2)

result.to_csv(root / "data" / "nettonennleistung.csv")
