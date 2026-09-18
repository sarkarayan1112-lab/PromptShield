#!/bin/bash
set -e
source .venv/bin/activate
python scripts/run_all.py
python -m uvicorn app.main:app --reload
