import pandas as pd
from utils import root

cols = {
    "ENH_MastrNummer": "string",
    "ENH_Betriebsstatus": "category",
    "ENH_EinheitenTyp": "string",
    "ENH_InbetriebnahmeDatum": "datetime64[ns]",
    "ENH_LetzteAktualisierung": "datetime64[ns]",
    "ENH_Gemeindeschluessel": "string",
    "ENH_Bruttoleistung": "float",
    "ENH_Nettonennleistung": "float",
}

df = pd.read_excel(
    root / "files" / "200303_MaStR-Daten_registriert_ab_31-01-2019.xlsx",
    sheet_name="Tabelle_ENH",
    usecols=cols.keys(),
    dtype=cols,
)

df.to_parquet(root / "data" / "raw.parquet")
