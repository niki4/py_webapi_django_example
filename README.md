## Installation:
```bash
python3 -m venv ./venv
source venv/bin/activate
```

```bash
(venv):$ python --version
Python 3.5.2
```

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

```bash
export DJANGO_SECRET_KEY='blah'
python manage.py migrate
```

## Run:
```bash
python manage.py runserver
```

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


* More info on usage server specific settings
http://django-configurations.readthedocs.io/en/latest/patterns/#server-specific-settings
```