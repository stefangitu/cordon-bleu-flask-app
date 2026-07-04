# Cordon Bleu – Flask Web App

A Python/Flask web application built as part of a collaborative university project on the theme of Gastronomy (Politehnica University of Bucharest, group 444D). The app presents information about the classic Cordon Bleu dish: its description and origin.

## Technologies Used

| Category | Tools |
|---|---|
| Backend | Python 3.11, Flask |
| Testing | pytest, unittest |
| Linting | pylint |
| CI/CD | Jenkins (declarative pipeline) |
| Containerization | Docker |
| Version Control | Git / GitHub |

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_gastronomie.py   # Business logic (descriere, origine)
│   └── tests/
│       ├── __init__.py
│       └── test_cordon_bleu.py         # Unit tests (4 tests)
├── img/                                # Screenshots
├── conftest.py
├── Dockerfile                          # python:3.11-slim, port 5000
├── Jenkinsfile                         # Install → Lint → Test pipeline
├── gastronomie.py                      # Flask app entry point
└── requirements.txt                    # flask, pytest, pylint
```

## Available Routes

| Route | Description |
|---|---|
| `/gastronomie` | Main gastronomy page |
| `/cordon_bleu` | Cordon Bleu overview |
| `/cordon_bleu/descriere` | Dish description |
| `/cordon_bleu/origine` | Origin and history |

## Running Locally

**Prerequisites:** Python 3.x, pip

```bash
git clone https://github.com/stefangitu/cordon-bleu-flask-app
cd cordon-bleu-flask-app
pip install -r requirements.txt
python gastronomie.py
```

App starts on `http://localhost:5000`. Navigate to `/gastronomie` to begin.

## Running with Docker

```bash
docker build -t cordon-bleu-app .
docker run -p 5000:5000 cordon-bleu-app
```

## Running Tests

```bash
PYTHONPATH=$(pwd) python -m pytest app/tests/test_cordon_bleu.py -v
```

4 tests covering all routes — status codes and response content validation.

## CI/CD – Jenkins Pipeline

The Jenkinsfile defines a declarative pipeline with four stages:

1. **Install Python** – ensures Python 3 and pip are available on the agent
2. **Install Dependencies** – installs Flask, pytest, pylint via pip
3. **Lint** – runs pylint across all source files (non-blocking)
4. **Test** – executes unit tests via pytest with PYTHONPATH set correctly

## Challenges & Solutions

- **PYTHONPATH in Jenkins:** Tests failed initially because Jenkins couldn't resolve the top-level `gastronomie` module from within `app/tests/`. Fixed by explicitly setting `PYTHONPATH=$(pwd)` in the test stage.
- **Docker host binding:** Flask defaults to `127.0.0.1`, making the app unreachable from outside the container. Fixed by setting `host='0.0.0.0'` in `app.run()`.

## Future Improvements

- Add ingredient quantity calculator (scale recipe for N servings)
- Extend to a full recipe database with search and filter
- Add HTML templates via Jinja2 instead of inline HTML strings
- Add authentication for user-submitted recipes
