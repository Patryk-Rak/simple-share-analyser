# Simple Share Analyser

This application was created for the purpose of solving a
preliminary qualification assignment. No updates or code
changes are planned, the app can serve as a template for future ideas.

## Description

The application is used to store data related to the history of financial
transactions. We can store information about recent purchases 
/ sales, date of transactions, number of shares purchased and their costs.
![alt text](https://i.imgur.com/zLiLAnC.png)
![alt text](https://i.imgur.com/r70eKSM.png)
## Getting Started

### Tech stack:

* Python == 3.9v
* Django == 4.0.4v
* Pycharm == 2021.2

### Installing

* Simply clone project or download it in .zip. Repo is public and there's no usage restrictions.
* Create a project directory
* Change location into the project directory in cmd
* Run ```python3 -m venv name_of_virtualenv``` or create venv
using the tools from your IDE, then activate it with ```source bin/activate```
* Use command to install all required libraries ```pip install -r /path/to/requirements.txt```

### Executing program

* ```python manage.py makemigrations``` and then ```python manage.py migrate```
* *Optionally create superuser with ```python manage.py makesuperuser```
* Start server with ```python manage.py runserver```, then open web explorer and
visit app page using address http://127.0.0.1:8000/. There is also 
http://127.0.0.1:8000/admin address for superuser's use 