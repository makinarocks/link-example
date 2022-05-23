SHELL := /bin/bash

STAGED := $(shell git diff --cached --name-only --diff-filter=ACMR -- 'src/***.py' | sed 's| |\\ |g')

all: format lint-all utest
	echo 'Makefile for project template'

format:
	black .
	isort .
	nbqa black .
	nbqa isort .

lint:
	pytest src/ --pylint --flake8 --mypy
	# nbqa pytest src/ --pylint --flake8 --mypy

lint-all:
	pytest src/ --pylint --flake8 --mypy --cache-clear
	nbqa pytest src/ --pylint --flake8 --mypy --cache-clear

lint-staged:
ifdef STAGED
	pytest $(STAGED) --pylint --flake8 --mypy --cache-clear
	nbqa pytest $(STAGED) --pylint --flake8 --mypy --cache-clear
else
	@echo "No Staged Python File in the src folder"
endif


utest:
	pytest tests -s --verbose --cov=src/ --cov-report=html --cov-report=term-missing --ignore=tests/components


init:
	pip install -U pip
	pip install -r requirements.txt
	pip install -e .
	bash ./hooks/install.sh

link:
	python -m pip install requests
	wheelfile=$$(python ./scripts/download-link.py) && python -m pip install $$wheelfile
