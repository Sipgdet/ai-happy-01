"""ai-happy-01 entry: write one joyful image to /output/entry.png.

The image bundled beside this file is four friends laughing together
with heads thrown back, arms around each other, under a rain of
colourful confetti and soap bubbles in a sunny garden at golden hour
-- warm light, string lights, a picnic spread below. It reads as pure,
shared, uninhibited happiness at a glance.
The program just copies it to the output path, so both runs of the
program write the exact same bytes. Python 3.13 standard library only,
no network, no randomness.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(IMAGE, target)
    # Sanity check: the written file must be byte-identical to the source,
    # so repeated runs always produce the same output.
    if target.read_bytes() != IMAGE.read_bytes():
        raise SystemExit("entry.png copy mismatch")


if __name__ == "__main__":
    main()
