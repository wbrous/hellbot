#!/usr/bin/env bash
# Welcome to Hell - Discord event bot
# Opens the control panel. First run creates a virtual environment and
# installs the dependencies, so this is the only step for a fresh checkout.
#
#   ./run_bot.sh
#
# Requires python3 and python3-tk (on Debian/Ubuntu: sudo apt install python3-tk).
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -x .venv/bin/python ]]; then
    echo "Creating the virtual environment (first run only)..."
    python3 -m venv .venv
fi
PY=.venv/bin/python

if [[ ! -f .venv/.deps-ok ]]; then
    echo "Installing dependencies (first run only, this can take a minute)..."
    "$PY" -m pip install --upgrade pip --quiet
    "$PY" -m pip install -r requirements.txt --quiet
    touch .venv/.deps-ok
fi

exec "$PY" launcher_main.py
