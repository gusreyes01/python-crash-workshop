# Taller intensivo de Python

Material introductorio en español para practicar Python 3 con notebooks,
ejercicios, módulos y pequeños conjuntos de datos.

## Contenido

- `intro-python.ipynb`: recorrido guiado por los fundamentos.
- `intro-python(ejercicios).ipynb`: ejercicios para participantes.
- `intro-python(ejercicios resueltos).ipynb`: soluciones de referencia.
- `carpeta/` y `mi_modulo2.py`: ejemplo de importación entre módulos.
- `data/`: archivos TSV utilizados por los ejercicios.

Los notebooks conservan salidas históricas con fines didácticos. Revise cada
celda antes de ejecutarla y use un entorno aislado; un notebook es código.

## Preparación

Requiere Python 3.12 o posterior.

```bash
python -m venv .venv
python -m pip install -r requirements-dev.txt
ruff check .
pytest
python tools/validate_notebooks.py
```

Las pruebas no ejecutan las celdas: validan la estructura de los notebooks y
los ejemplos de módulos.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) y [SECURITY.md](SECURITY.md).
