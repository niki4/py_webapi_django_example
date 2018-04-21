Example of Web API for some e-commerce catalog.

The code is pretty short and declarative, as the Django and [Django REST Framework](http://www.django-rest-framework.org/tutorial/quickstart/) both takes care on standard ORM, UI, serialization and Web CRUD logic.
## Installation:
Just clone the repo from github, then create and activate new virtual environment in cloned folder on local disk:
```bash
python3 -m venv ./venv
source venv/bin/activate
```
Make sure you have Python 3 as your interpreter (since Django 2.0 doesn't support Python 2 anymore).
```bash
(venv):$ python --version
Python 3.5.2
```
Install the project requirements.
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
Now you have to "initialize" the db (that's `manage.py migrate` command for). In order to ensure the source code doesn't
contain any sensitive data (in our case it's `DJANGO_SECRET_KEY`), we must provide it before we can run the `manage.py`.

For the convenience, you may store setting in your system variable as it shown below:
```bash
export DJANGO_SECRET_KEY='blah'
python manage.py migrate
```

> Dynamic set up the server specific settings provided by the [django-configurations](http://django-configurations.readthedocs.io/en/latest/patterns/#server-specific-settings) plugin. 

## Run:
If you did the export of `DJANGO_SECRET_KEY` as described above, you could simply run the server: 
```bash
python manage.py runserver
```

However, if you aren't comfortable to set values in system variables, you can provide them explicitly in command line, e.g.:
```bash
DJANGO_CONFIGURATION=Dev DJANGO_SECRET_KEY='blah' python ./manage.py runserver

>>>
django-configurations version 2.0, using configuration 'Dev'
Performing system checks...

System check identified no issues (0 silenced).
April 20, 2018 - 20:34:37
Django version 2.0.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now simply open the browser with the address http://127.0.0.1:8000/ and explore the API.