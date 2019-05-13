# Airport Information Service

This project is an API based web application that reads a CSV file with the information of Airports data set provided by the user, and updates the database with the data from file.

## Getting Started

Using this application the user can upload a CSV file through a simple UI (html template).
After that, the API or the Administration site of the application can be checked to retrieve the stored information.
The CSV file should have an specific format according to the CSV file provided by OurAirports.com. 
Please use the CSV in the "data" file inside the project.  


## Deployment

This application was implemented using the following technologies:


* [Python](https://www.python.org/) - Programming Language
* [Django](https://www.djangoproject.com/) - Web Framework
* [Django Rest](https://www.django-rest-framework.org/) - Web API
* [SQLite](https://www.sqlite.org/index.html) - DataBase

## Requirements

* Python 3.x.x
* Django 1.11.x

## Runing the application

To run this application, clone the repository on your local machine and execute the following commands.

```
$ cd airports_api
$ virtualenv virtenv
$ source virtenv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
 ```

## Application

After having the server running successfully. Then you can go directly to the UI and upload the CSV file to the database using the following URLs.

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/upload-file

```

To check the administration site you need to create a superuser running the following command

```
$ python manage.py createsuperuser

```

You need to set a user and a password. The super user "admin" with the password: "adminadmin" is created already. Use the following URL to get the administration site. 

```
http://127.0.0.1:8000/admin
```

### API

You can use the API in this way in order to retrieve the information:

List of Airports.
```
http://127.0.0.1:8000/api/v1/airports/
http://127.0.0.1:8000/api/v1/airports/list
``` 

An specific asset based in its IATA.
```
http://127.0.0.1:8000/api/v1/airports/iata/<airport_iata>

example:
http://127.0.0.1:8000/api/v1/airports/iata/txl/   
```

List of Airports filtered by name.
```
http://127.0.0.1:8000/api/v1/airports/iata/<airport_name>
http://127.0.0.1:8000/api/v1/airports/name/Berlin/
``` 

## Running the tests

To run the test cases of the application, enter the following command

```
$ python manage.py test
```


### Author:

* **Ernesto Zarza**

