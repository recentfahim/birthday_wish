##  Birthday Wish

Birthday wish is a Django and rest API based web platform. This application provide API for sign-in and sign-up through email. And wish the user on their birthday.

#### Requirements

-   Python 3.9.19
-   Django 4.2.11
-   Django Rest Framework 3.15.1

#### Install Dependencies

Before installing project dependencies please install `virtualenv` if you don't have it installed your system.

    pip3 install virtualenv
 
Create a virtual environment using `virtualenv`

    virtualenv venv

Activate the virtual environment `venv`

    source venv/bin/activate

Install all dependency from  root  folder

    pip install -r requirements.txt


#### Database Setup

You can use any database you want, but in this project MySQL has been used.

Once a database is created and connected, migrate the models

    python manage.py migrate

Create and configure the  `.env`  file. Put all essential configuration in this file, like Secret, Database credentials, Allowed hosts, etc. You can check the `.env.example` for reference. Or you can rename the `.env.example` to `.env`.

Now, run the project with
```
python manage.py runserver
```

Open the browser and put `127.0.0.1:8000` to see the application output.

Create a superuser to get access to admin

    python manage.py createsuperuser

You can see the Django admin panel at `127.0.0.1:8000/admin`.

Check the `urls.py` and navigate to the urls to view the web outputs.

### Docker
You can also use Docker for this project. To use it run
```shell
docker-compose up --build
```

It'll build the web and db. 

To migrate the models

```shell
docker-compose exec web python manage.py migrate
```

Create a superuser to get access to admin
```shell
docker-compose exec web python manage.py createsuperuser
```
You can see the Django admin panel at `127.0.0.1:8000/admin`.

Check the urls.py and navigate to the urls to view the API outputs.

