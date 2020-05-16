data: data/nettonennleistung.csv data/nettonennleistung.json

prepare: data/200303_MaStR-Daten_registriert_ab_31-01-2019/raw/Tabelle_ENH.parquet

data/200303_MaStR-Daten_registriert_ab_31-01-2019/raw/Tabelle_ENH.parquet: venv
	./venv/bin/python ./scripts/convert.py

data/nettonennleistung.csv: prepare
	./venv/bin/python ./scripts/process.py

data/nettonennleistung.json: data/nettonennleistung.csv
	./venv/bin/python ./scripts/geo.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install wheel
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv
	rm -rf data/*.json
	rm -rf data/200303_MaStR-Daten_registriert_ab_31-01-2019/

clean-venv:
	rm -rf venv

.PHONY: clean clean-venv
