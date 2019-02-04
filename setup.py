try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'name': 'objectdetection',
        'description': 'Application for object detection',
        'author': 'Robotic Solutions',
        'version': '0.1',
        'install_requires': [],
        'packages': [],
        'scripts': []
}

setup(**config)
