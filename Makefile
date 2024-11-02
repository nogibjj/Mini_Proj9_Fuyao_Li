install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

test: 
	python -m pytest -cov=main test_main.py

lint:
	ruff check *.py mylib/*.py test_*.py

deploy:

all: install format lint test deploy