PYTHON ?= $(shell which python)
NOSE ?= $(PYTHON) $(shell which nosetests)

ETALON = test/etalon
CHARPATH = test

.PHONY:
all: unit-tests characterization-tests sdist bdist_egg

.PHONY:
unit-tests:
	$(NOSE)

.PHONY: characterization-tests
characterization-tests:
	$(NOSE) --etalon $(ETALON) $(CHARPATH)

.PHONY: update-characterization-tests
update-characterization-tests:
	$(NOSE) --etalon $(ETALON) $(CHARPATH) --update

.PHONY: sdist
sdist:
	$(PYTHON) setup.py sdist

.PHONY: bdist_egg
bdist_egg:
	$(PYTHON) setup.py bdist_egg
