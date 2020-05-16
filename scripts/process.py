import pandas as pd
from utils import datadir

columns = [
    "ENH_MastrNummer",
    "ENH_Betriebsstatus",
    "ENH_InbetriebnahmeDatum",
    "ENH_Meldedatum",
    "ENH_LetzteAktualisierung",
    "ENH_Gemeindeschluessel",
    "ENH_Bruttoleistung",
    "ENH_Nettonennleistung",
    "ENH_Energietraeger",
]

df = pd.read_parquet(
    datadir
    / "200303_MaStR-Daten_registriert_ab_31-01-2019/raw/"
    / "Tabelle_ENH.parquet",
    columns=columns,
)

subset = df[["ENH_Gemeindeschluessel", "ENH_Energietraeger", "ENH_Nettonennleistung"]]
subset.columns = ["AGS", "Energieträger", "Nettonennleistung"]

# Filter for SN
subset = subset[subset["AGS"].str.startswith("14")]

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

result.to_csv(datadir / "nettonennleistung.csv")
