"""Проверяет, что все блоки ```json в документации содержат валидный JSON."""

import json
import re
import sys
from pathlib import Path

PATTERN = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)


def main() -> int:
    root = Path("docs")
    if not root.exists():
        print("docs/ not found")
        return 1

    errors = 0
    for md_file in root.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        for i, block in enumerate(PATTERN.findall(text), start=1):
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                print(f"{md_file}: block #{i} invalid JSON: {exc}")
                errors += 1

    if errors:
        print(f"Found {errors} invalid JSON block(s)")
        return 1

    print("All JSON blocks are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())