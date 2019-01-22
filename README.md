# ObjectDetection

## Under Development
Object Detection software written on python

# Set Up Development Environment
## 1. Set Up Virtual Environment (Optional)
### Ubuntu
Install `virtualenv` and `virtualenvwrapper`:
```
sudo pip install virtualenv virtualenvwrapper
```
Using a text editor, add the following lines to your `~/.bashrc` file:
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
Source the `~/.bashrc` file:
```
source ~/.bashrc
```
Create a virtual environment:
```
mkvirtualenv name -p python3
```
## 2. Install Dependencies
Inside your virtual environment install the requirements:
```
pip install -r dev-requirements.txt
```
