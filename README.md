# Cordon Bleu – Flask Web App

A Python/Flask web application built as part of a collaborative university project on the theme of Gastronomy (Politehnica University of Bucharest, group 444D). The app presents information about the classic Cordon Bleu dish: its origin, description, and preparation.

## Technologies Used

| Category | Tools |
|---|---|
| Backend | Python 3, Flask |
| Testing | pytest |
| CI/CD | Jenkins (declarative pipeline) |
| Containerization | Docker |
| Version Control | Git / GitHub |

## Project Structure

```
.
├── app/
│   └── lib/
│       ├── __init__.py
│       └── biblioteca_gastronomie.py   # Business logic for Cordon Bleu
├── img/                                 # Screenshots
├── Dockerfile                           # Container configuration
├── Jenkinsfile                          # CI/CD pipeline (install → lint → test)
├── gastronomie.py                       # Flask application entry point
├── requirements.txt                     # Python dependencies
├── test_gastronomie.py                  # Unit tests
└── README.md
```

## Available Routes

| Route | Description |
|---|---|
| `/gastronomie` | Main gastronomy page |
| `/cordon_bleu` | Cordon Bleu overview page |
| `/cordon_bleu/descriere` | Dish description |
| `/cordon_bleu/origine` | Origin and history of the dish |

## Running Locally

**Prerequisites:** Python 3.x, pip

```bash
git clone https://github.com/<your-username>/cordon-bleu-flask-app
cd cordon-bleu-flask-app
pip install -r requirements.txt
python gastronomie.py
```

The app starts on `http://localhost:5000`.

## Running with Docker

```bash
docker build -t cordon-bleu-app .
docker run -p 5000:5000 cordon-bleu-app
```

Access the app at `http://localhost:5000`.

## Running Tests

```bash
python -m pytest test_gastronomie.py -v
```

All tests passed successfully both locally and through the Jenkins pipeline.

## CI/CD – Jenkins Pipeline

The Jenkinsfile defines a declarative pipeline with three stages:

1. **Install** – sets up a virtual environment and installs dependencies from `requirements.txt`
2. **Lint** – runs static code analysis
3. **Test** – executes unit tests via pytest

## Challenges & Solutions

- **Jenkins environment isolation:** The pipeline initially failed because system-level Python packages conflicted with project dependencies. Solved by configuring a dedicated virtual environment within the Jenkins workspace.
- **Docker port binding on Linux:** Running the container with the default Flask host (`127.0.0.1`) made the app unreachable from outside the container. Fixed by setting `host='0.0.0.0'` in the Flask run configuration.

## Future Improvements

- Add ingredient quantity calculator (scale recipe for N servings)
- Add a preparation timer per step
- Extend to a full recipe database with search functionality
- Add authentication for user-submitted recipes
