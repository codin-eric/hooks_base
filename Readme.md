# Formatters, Linters and Pre-commit hooks
Este repo lo voy a tener como guia para cada vez que quiero hacer esto de formatters, linters y pre-commit hooks ja!
## Linters
Estos son pequeños scripts que hacen que mi código se vea siempre igual respetando las normas pep8
- flake8: linter general, te acomoda casi todo.
- mypy: checks types
- pylint: Mejor que flak8 pero mas pesado. Puede tardar mucho así que a veces no lo uso.

## Formatters
- black: the cool one
- isort: Los imports tienen un orden, yo no lo recuerdo, isort lo hace por mi.


# Setup
- Instalar todo lo que hay en requirements.txt
- Crear 
    - .pre-commit-config.yaml
    - .flake8
    - pyproject.toml
- Correr el comando `pre-commit install`

# Algunos usos para recordar
Si queres correr black a mano
```
black [file]
```
Si queres correr black solo para ver donde puede haber errores
```
black --diff [file]
```
y todo lo demas se puede leer aqui https://pypi.org/project/black/

## Saltar hooks
Puede darse el caso donde sea necesario subir a github sin tener todo andando. para eso existe el `-n --no-verify` 