import pandas as pd
import xlrd
from utils import filesdir, datadir, log

sheet_names = [
    "Tabelle_IDX",
    "Tabelle_ENH",
    "Tabelle_EEG",
    "Tabelle_KWK",
    "Tabelle_SGE",
    "Tabelle_MAK",
]

sourcefile = filesdir / "200303_MaStR-Daten_registriert_ab_31-01-2019.xlsx"

output_dir = datadir / sourcefile.stem / "raw"
output_dir.mkdir(exist_ok=True, parents=True)


def read_sheet(sheet_name, dtypes=None):
    log.msg("Reading sheet", sheet_name=sheet_name, sourcefile=sourcefile)
    workbook = xlrd.open_workbook(sourcefile, on_demand=True)
    with pd.ExcelFile(workbook) as xls:
        df = pd.read_excel(xls, sheet_name=sheet_name, dtype=dtypes)
    return df


def write_schema(df, sheet_name):
    output_path = output_dir / f"{sheet_name}-schema.csv"
    log.msg("Writing schema", sheet_name=sheet_name, output_path=output_path)
    df.dtypes.to_csv(output_path, header=False)


def write_sheet(df, sheet_name):
    output_path = output_dir / f"{sheet_name}.parquet"
    log.msg("Writing sheet", sheet_name=sheet_name, output_path=output_path)
    df.to_parquet(output_path)


def main():
    sheet_name = "Tabelle_ENH"
    dtypes = {"ENH_Gemeindeschluessel": "string"}

    df = read_sheet(sheet_name, dtypes=dtypes)
    write_schema(df, sheet_name)
    write_sheet(df, sheet_name)


main()
