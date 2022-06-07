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

# Notes

### virtual environment -- a copy of the Python interpreter into which you can install packages privately; they prevent package clutter and version conflicts.  Creating a virtual environment for each project ensures that applications have access only to the packages that they use, while the global interpreter remains neat and clean and serves only as a source from which more virtual environments can be created.

