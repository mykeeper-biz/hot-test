:: This application is built with python 3.8

:: To set up install pipenv
pip install pipenv

::Upgrade pip
python -m pip install --upgrade pip

:: Then navigate to the root of this code and create a pipenv from the included pipfile files
pipenv install

:: Start the protected environment
pipenv shell
python --version

:: To run the test
python tester.py
:: cd hotinstinet
:: python tester.py
:: cd ..
