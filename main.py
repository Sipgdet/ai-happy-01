"""ai-happy-01 entry: write one joyful image to /output/entry.png.

The image bundled beside this file is a golden retriever puppy smiling
in a sunny wildflower meadow -- bright, warm and unambiguously happy.
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
