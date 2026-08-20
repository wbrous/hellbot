"""Entry point for the desktop launcher.

Shows errors in a message box instead of a console, so a crash is visible even
when the launcher is started without a terminal (e.g. from a desktop entry).
"""

from __future__ import annotations

import io
import sys
import traceback
from pathlib import Path

# Make `hell` / `launcher` importable when run from anywhere.
sys.path.insert(0, str(Path(__file__).resolve().parent))


def _popup(title: str, message: str) -> None:
    """Best-effort message box; falls back to stderr when there is no GUI."""
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(title, message)
        root.destroy()
        return
    except Exception:
        pass
    print(f"{title}: {message}", file=sys.stderr)


def main() -> int:
    # Guard against a missing stdio when launched without a terminal.
    if sys.stdout is None:
        sys.stdout = io.StringIO()
    if sys.stderr is None:
        sys.stderr = io.StringIO()

    try:
        import tkinter  # noqa: F401
    except Exception:
        _popup(
            "Welcome to Hell — missing Tkinter",
            "Python was installed without Tkinter, so the control panel cannot open.\n\n"
            "Install the python3-tk package for your distribution "
            "(Debian/Ubuntu: sudo apt install python3-tk).\n\n"
            "You can still run the bot in a console with:  ./run_bot_console.sh",
        )
        return 1

    try:
        from launcher.gui import run_gui

        return run_gui()
    except Exception as exc:
        _popup(
            "Welcome to Hell — crash",
            f"The launcher hit an unexpected error:\n\n{type(exc).__name__}: {exc}\n\n"
            f"{traceback.format_exc()[-1500:]}",
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
