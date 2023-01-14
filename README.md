## Vending Machine Tracking Application

### Requirement
<ul>
    <li>Poetry version > 1.0.0</li>
    <li>pre-commit</li>
    <li>docker</li>
</ul>

### Set up `pre-commit`
1. Install pre-commit ``pip install pre-commit``
2. Run ``pre-commit install``

### Set up poetry as virtual environment
1. install poetry
``curl -sSL https://install.python-poetry.org | python3 -``
2. Run ``poetry install``
3. To run virtual environment, ``poetry shell``

### Set up database via docker
Run ``docker compose up -d``

To stop running database: ``docker compose down`` or stop container from docker UI

### Running project
run server on port 8000

``./manage.py runserver 8000`` or ``python manage.py runserver 8000``
