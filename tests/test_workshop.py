import json

import pytest

from carpeta.mi_modulo import saludar
from tools.validate_notebooks import validate_directory, validate_notebook


def notebook(cells=None, nbformat=4):
    return {
        "cells": cells
        if cells is not None
        else [{"cell_type": "markdown", "metadata": {}, "source": ["# Lesson"]}],
        "metadata": {},
        "nbformat": nbformat,
        "nbformat_minor": 5,
    }


def test_saludar_normalizes_name_and_prints(capsys):
    assert saludar("  Jaime ") == "Hola, Jaime"
    assert capsys.readouterr().out == "Hola, Jaime\n"
    with pytest.raises(ValueError, match="non-empty"):
        saludar(" ")


def test_notebook_validation_and_directory_summary(tmp_path):
    path = tmp_path / "lesson.ipynb"
    path.write_text(json.dumps(notebook()), encoding="utf-8")
    assert validate_notebook(path) == 1
    assert validate_directory(tmp_path) == {"lesson.ipynb": 1}


@pytest.mark.parametrize(
    "document",
    [
        notebook(nbformat=3),
        notebook(cells=[]),
        notebook(cells=[{"cell_type": "unknown", "source": []}]),
        notebook(cells=[{"cell_type": "code", "source": None}]),
    ],
)
def test_rejects_invalid_notebook_structures(tmp_path, document):
    path = tmp_path / "invalid.ipynb"
    path.write_text(json.dumps(document), encoding="utf-8")
    with pytest.raises(ValueError):
        validate_notebook(path)


def test_rejects_invalid_json_and_empty_directory(tmp_path):
    path = tmp_path / "broken.ipynb"
    path.write_text("{", encoding="utf-8")
    with pytest.raises(ValueError, match="not valid"):
        validate_notebook(path)
    path.unlink()
    with pytest.raises(ValueError, match="no notebooks"):
        validate_directory(tmp_path)
