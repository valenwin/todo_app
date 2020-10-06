# ToDo App

## Overview
#### Django3 

# Deploy on Heroku server
https://todo-list-app-django.herokuapp.com/

# Deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings (see example .env.gist):
and change file name to .env:

`SECRET_KEY`,
`DB_PASSWORD`,
`DB_NAME`,
`DB_USER`

3 - Migrate db models:

`python3 manage.py migrate`

4 - Run app:

`python3 manage.py runserver`
