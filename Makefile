.PHONY: all test clean

check-pep257:
	@prospector --with-tool pep257

create-requirements:
	@pip-compile ./requirements/base.in

freeze:
	@pip freeze

format:
	@blue .
	@isort .

install-requirements:
	@pip install -r ./requirements/base.txt

lint:
	@blue . --check
	@isort . --check

test:
	@python -m pytest -s tests/

update-requirements:
	@rm ./requirements/base.txt
	@pip-compile ./requirements/base.in

