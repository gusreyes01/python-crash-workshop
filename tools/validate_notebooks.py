import argparse
import json
from pathlib import Path

ALLOWED_CELL_TYPES = {"code", "markdown", "raw"}


def validate_notebook(path):
    notebook_path = Path(path)
    try:
        document = json.loads(notebook_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"{notebook_path} is not valid UTF-8 notebook JSON") from error

    if document.get("nbformat") != 4:
        raise ValueError(f"{notebook_path} must use notebook format 4")
    cells = document.get("cells")
    if not isinstance(cells, list) or not cells:
        raise ValueError(f"{notebook_path} must contain cells")
    for index, cell in enumerate(cells):
        if cell.get("cell_type") not in ALLOWED_CELL_TYPES:
            raise ValueError(f"{notebook_path} cell {index} has an invalid type")
        if not isinstance(cell.get("source"), (str, list)):
            raise ValueError(f"{notebook_path} cell {index} has an invalid source")
    return len(cells)


def validate_directory(root):
    paths = sorted(Path(root).glob("*.ipynb"))
    if not paths:
        raise ValueError("no notebooks found")
    return {path.name: validate_notebook(path) for path in paths}


def main():  # pragma: no cover - thin CLI wrapper
    parser = argparse.ArgumentParser(description="Validate workshop notebooks")
    parser.add_argument("directory", nargs="?", type=Path, default=Path.cwd())
    summaries = validate_directory(parser.parse_args().directory)
    for name, cell_count in summaries.items():
        print(f"validated {name}: {cell_count} cells")


if __name__ == "__main__":  # pragma: no cover
    main()
