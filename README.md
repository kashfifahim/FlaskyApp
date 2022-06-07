# Web Development Project

## Create an empty application directory
```bash
mkdir flasky
cd flasky
```

## Inside Application Directory Create a virtual environment

### Python3 
```bash
python3 -m venv virtual-environment-name
```
### Python2
```bash
sudo pip install virtualenv
virtualenv venv
```

## Activate the virtual environment
```bash
source venv/bin/activate
```

## Install Python Packages with pip
```bash
(venv) $ pip install flask
```
- Commonly used convention for virtual environments is to call them ```venv```

## A Complete Application

```hello.py```
```python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```

## Development Web Server

```bash
(venv) $ export FLASK_APP=hello.py
(venv) $ flask run
```

```python3
if __name__ == '__main__':
    app.run()
```

## Dynamic Routes
```python3
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
```

## Debug Mode
```bash
(venv) $ export FLASK_APP=hello.py
(venv) $ export FLASK_DEBUG=1
(venv) $ flask run
```

# Notes

### virtual environment -- a copy of the Python interpreter into which you can install packages privately; they prevent package clutter and version conflicts.  Creating a virtual environment for each project ensures that applications have access only to the packages that they use, while the global interpreter remains neat and clean and serves only as a source from which more virtual environments can be created.

### Initializing a Flask app -- all Flask apps must create an application instance:
```python3
from flask import Flask
app = Flask(__name__)
```

### The __name__ argument is passed to the Flask application constructor; Flask uses this argument to determine the location of the app, which in turn allows Flask to locate other files that are part of the app.

### Web browsers, clients, send ```requests``` to the web server.  The web server sends the ```requests``` to the Flask app.  The Flask app needs to know what code to run  for each URL requested, so the Flask app keeps a mapping of the URLs to Python functions.

### route -- A ```route``` is the association between a URL and the function that handles it.

### Defining a route in a Flask app
```python3
@app.route('/')
def index():
  return '<h1>Hello World!</h1>'
```

### View function -- a function that handle application URLS; the return value of this view function is the response the client receives.

### path type -- the ```path``` type is a special string type that can include forward slashes

### Code 404 -- error message for a web page that does not exist


