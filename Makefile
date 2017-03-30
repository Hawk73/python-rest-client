.PHONY: install tests publish

install:
	pip install -r requirements.txt

tests:
	behave

publish:
	python setup.py sdist upload
