#!/usr/bin/env bash
# Welcome to Hell - console mode (for debugging).
# Runs the bot directly with log output in this terminal.
#
#   ./run_bot_console.sh
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -x .venv/bin/python ]]; then
    echo "No virtual environment found. Run ./run_bot.sh once first." >&2
    exit 1
fi

exec .venv/bin/python bot.py
