# Development

- [Schema](schema/proffer.schema.json) defines the records; [fixtures](tests/fixtures/) exercise the contract.
- [Validator](check.py) handles checks JSON Schema cannot express.
- Change schema, fixtures, and tests together. No compatibility layers or duplicate prose specifications.
- Run `python -m pip install -r requirements-dev.txt` and `python -m unittest discover -s tests`.
