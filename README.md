# pathetic-url
Django app for shorten long urls

Installation guide:
* virtualenv
```
virtualenv -p python3 venv
. venv/bin/activate
```

* install requirements
```
pip install -r requirements.txt
```

* navigate to project directory
```
cd pathetic_url
```

* create a secret key
```
echo "itsasecretdontlook" > secret.txt
```

* run migrations
```
python manage.py migrate
```

* run server
```
python manage.py runserver
```

* go to [this url](http://127.0.0.1:8000/pathetic/) to see the results