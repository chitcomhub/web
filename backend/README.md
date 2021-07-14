# Backend

The application is written on the FastAPI framework to implement the REST API.
The whole backend includes a PostGres database with a web-interface to manage it.

This code is following Part 1 of this tutorial: 
https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396


Notice: one of the changes made is that we use ``virtualenv`` instead of ``pipenv``


# To migrate new datamodel with Alembic:
Run following code after you update new model in ``models.py`` (you need to run it from within current folder (called ``backend``):

``docker-compose run backend alembic revision --autogenerate -m "Set in your comments"``

``docker-compose run backend alembic upgrade head``

``docker-compose down``

# For development
## Installing
    $ python -m pip install virtualenv
    $ python -m venv venv
    Activate your virtual environment which is named ``venv``: 
    - if on Windows: $ .\venv\Scripts\activate
    - in on Linux: $ .\venv\bin\activate
    $ pip install -r requirements.txt

## Run
    - if on Windows: $ python -m uvicorn main:app --reload 
    - if on Linux: $ ./run

# To run the whole backend (with Postgres DB)
While in the backend folder ``backend`` type

    docker-compose up

After successeful installation of db, backend and web-interface, do following:

0) Go to ``http://localhost:8000/docs`` to see all the APIs

1) Go to ``http://localhost:5050/`` and configure your database connection for the first time
2) type username and password (defined in ``docker-compose.yml`` file) and click ``Login``
3) Click on ``Add New Server`` and type: Name = chitweb
4) Go to ``Connection`` in the popup and type:
Host = db (or see in docker-compose)
Port = 5432 (or see in docker-compose)
Username = see in docker-compose
password = see in docker-compose
Click ``Save``
5) Open ``Databases`` and right click on the one called ``postgres``. Choose ``Query Tool``.
6) Test a simple query by typing in ``Query Editor``: ``select * from public.members``

