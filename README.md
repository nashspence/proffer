# Proffer

Non-authoritative reference handoffs for independent repository evaluation. Validation is not acceptance or permission to integrate.

- [Contract](schema/proffer.schema.json)
- [Valid and invalid examples](tests/fixtures/)
- [Validator](check.py) and [tests](tests/test_contract.py)

Handoffs use `.reference/proffer.json`. Publication and disposition records belong in the owning issue, not inside the published commit. Run `python check.py RECORD.json` after installing `requirements-dev.txt`.
