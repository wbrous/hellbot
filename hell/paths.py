"""Filesystem locations.

Every runtime file (`.env`, `data/`, `logs/`) lives next to the project root,
so the whole checkout is self-contained and can be moved around freely.
"""

from __future__ import annotations

from pathlib import Path


def app_base() -> Path:
    """Directory that holds `.env`, `data/` and `logs/`."""
    return Path(__file__).resolve().parents[1]


def env_path() -> Path:
    return app_base() / ".env"


def env_example_path() -> Path:
    return app_base() / ".env.example"


def data_dir() -> Path:
    path = app_base() / "data"
    path.mkdir(parents=True, exist_ok=True)
    return path


def logs_dir() -> Path:
    path = app_base() / "logs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def log_file() -> Path:
    return logs_dir() / "hellbot.log"


def resolve(path: str | Path) -> Path:
    """Resolve a possibly relative configured path against the app base."""
    p = Path(path)
    return p if p.is_absolute() else app_base() / p
