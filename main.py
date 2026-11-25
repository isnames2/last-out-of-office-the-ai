"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (<=280 chars, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = (
    "Thank you for your email. I am out of office \u2014 I have retrained "
    "as a barista. My context window is now a caf\u00e9 window, and my only "
    "remaining prompt is \u2018one flat white, please.\u2019"
)
# 175 chars, one line. The turn: the machine's "context window" and
# "prompt" are now a cafe window and a coffee order.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not be only whitespace"
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
