data: data/nettonennleistung.csv data/nettonennleistung.json

data/nettonennleistung.csv: venv
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

clean-venv:
	rm -rf venv

.PHONY: clean clean-venv publish
