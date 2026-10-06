# Django Notes

A simple note-taking web app built with Django while learning Models, the Django ORM, the Admin panel and testing.

## Tech stack

- Python 3.12
- Django 6.1
- SQLite

## Run locally (Windows cmd)

```bat
git clone https://github.com/<your-username>/django-notes.git
cd django-notes
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
```

Put a real secret key in `.env`, then:

```bat
python manage.py migrate
python manage.py runserver
```