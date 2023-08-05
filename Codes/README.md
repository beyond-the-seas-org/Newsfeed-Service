# Database

## Steps

- Create a postgresql database server instance on Render 
- Create the basic Flask-Restful app and save the external url to the database instance as an environment variable
- Connect the newly created server with PgAdmin and check if the database is okay
- careful about the hostname, port, psql command with password
- [YouTube Tutorial](https://youtu.be/AgTr5mw4zdI)
- Connecting with [SQLAlchemy and PgAdmin](https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/)
- [Debugging](https://github.com/asifhaider/Beyond-The-Seas-Information-System-Design-3-2#database-for-local) postgres connection, roles, restart, port error etc.

## Creating Tables

- [Flask-SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#)
- Write model class
- flask db init
- flask db migrate -m "message"
- flask db upgrade
- Create new tables
    - db.create_all()

- if schema needed to change, migrate and upgrade needed again, otherwise no need
- [model file structure related debug](https://github.com/miguelgrinberg/Flask-Migrate/issues/50)
