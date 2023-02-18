To start the application:

<h6>Create virtual environment</h6>

```bash
python -m venv .venv
```

<h6>Activate virtual environment</h6>

```bash
source .venv/bin/activate
```

<h6>Install dependencies</h6>

```bash
pip install -r requirements.txt
```

<h6>Export environmental variable</h6>

```bash
export FLASKAPP=app.py
```

<h6>Run the app</h6>

```bash
flask run
```

<h6>How to get help with the flask command</h6>

```bash
flask --help
```

<h6>How to use flask with flags</h6>

```bash
flask run --help
```

The --reload, --no-reload, --debugger, and --no-debugger options provide a greater degree of control on top of the debug mode setting. For example, if debug mode is enabled, --no-debugger can be used to turn off the debugger, while keeping debug mode and the reloader enabled.

