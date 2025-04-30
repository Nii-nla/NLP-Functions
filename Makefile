install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
	pip install --upgrade fire
test:
	python -m pytest -vv --cov=phrases --cov=nlplogic test_corenlp.py

format:
	black *.py nlplogic

lint:
	pylint --disable=R,C *.py

all: install lint test