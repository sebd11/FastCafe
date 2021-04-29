# FastCafe
[![Python 3.8.5](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/release/python-385/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)

## Quick start
To start the app run the following:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run tests
Tests can be run with:
```
pytest
```
With coverage:
```
coverage run -m pytest
coverage report -m
```
