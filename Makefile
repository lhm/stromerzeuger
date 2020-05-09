data: data/nettonennleistung.csv

data/nettonennleistung.csv: venv
	./venv/bin/python ./scripts/process.py

publish: data
	./venv/bin/python ./scripts/update-datawrapper.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install wheel
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv

clean-venv:
	rm -rf venv

.PHONY: clean clean-venv publish
