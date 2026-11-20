.DEFAULT_GOAL := help
.PHONY: help

help:
	@printf '%s\n' \
		'Install development dependencies: python -m pip install -r requirements-dev.txt' \
		'Run contract tests: python -m unittest discover -s tests' \
		'Validate a handoff: python check.py RECORD.json'
