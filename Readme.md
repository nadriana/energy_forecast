# Forecast

Forecast models running in a REST API

## Requirements

Python 3.8

## Quickstart

1. Clone this repo
2. On your terminal, run `pip install -r requirements.txt`
3. Then run `uvicorn main:app --reload`
4. Finally, go to http://localhost:8000/docs#

### Troubleshooting

Error: `Library not loaded: @rpath/libtbb.dylib in Prophet / Python` while installing requirements.

- This error happens because you are using a different Python version than 3.8, to fix this do :
  1. `python3 -m pip install virtualenv`
  2. `virtualenv -p python3.8 venv`
  3. `source venv/bin/activate`
  4. Run the quickstart steps again
