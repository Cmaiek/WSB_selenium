=========================
Example App with Selenium
=========================

Development
===========

1. Setup the virtualenv or use the existing:

   - Prepare the coding environment with python3

     ::

       $ python3 -m venv .venv
       $ source .venv/bin/activate
       $ pip install -r requirements.txt

   - Prepare the coding environment with python2

     ::

       # you need to have the virtualenvwrapper installed
       # sudo pip install -U  virtualenvwrapper
       $ source /usr/bin/virtualenvwrapper.sh
       $ mkvirtualenv wsb-simple-selenium
       $ pip install -r requirements.txt

     ::

        # Continue working with virtualenv:
        $ workon wsb-simple-selenium

2. Get the driver:

   - chrome (check https://sites.google.com/a/chromium.org/chromedriver/):

     ::

       $ wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
       $ unzip chromedriver_linux64.zip
       $ chmod +x chromedriver*

   - firefox:

     ::

       wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
       tar -xvzf geckodriver*tar.gz
       chmod +x geckodriver*

Uruchamianie
============

::

  export PATH=$PATH:$(pwd)
  python auto_search.py
