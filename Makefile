.PHONY: install tests

install:
	pip install -r requirements.txt

tests:
	behave
