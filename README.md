https://habr.com/ru/post/160117/
# Django_REST

Select a project (one of the team members) from the previous sprint and copy the project.

Add Django-Rest-Framework to project and implement appropriate CRUD operation for resources:

`http://127.0.0.1:8000/api/v1/user/{id}?`
`http://127.0.0.1:8000/api/v1/user/{id}/order/{id}?`
`http://127.0.0.1:8000/api/v1/order/{id}?`
`http://127.0.0.1:8000/api/v1/book/{id}?`
`http://127.0.0.1:8000/api/v1/author/{id}?`

Check all operation with Postman


And record short video (2-10min) that shows functionality in action





## install requirement project's packages

```commandline
pip install -r requirements.txt
```

## Run project

Go to the folder with manage.py file, run library
```commandline
python manage.py migrate 
```

```commandline
python manage.py runserver
```