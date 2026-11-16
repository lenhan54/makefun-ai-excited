"""ai-excited-01 entry (Python 3.13, standard library only).

The entry image is entry.png beside this file. The program copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), creating the
output directory if needed. The copy is byte-identical every run, so the
two graded runs write the same bytes.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("entry.png")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(SOURCE, destination)
    # Determinism guard: the graded runs must write identical bytes, so
    # refuse to finish silently if the copy came out short or different.
    # Size alone could hide a same-length corruption, so also compare the
    # full content hash of source and destination before returning.
    if destination.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("entry.png copy size mismatch")
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != hashlib.sha256(
        destination.read_bytes()
    ).hexdigest():
        raise RuntimeError("entry.png copy content mismatch")


if __name__ == "__main__":
    main()
