
makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

superuser:
	python manage.py createsuperuser