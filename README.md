# Small API 

Author: Pablo Valdunciel

Date:  07/09/2022

## Comments on implementation decisions

1. Uniqueness of the username: the inclusion of the `UNIQUE` constraint for the username does not seem appropriate, since two people can easily have the same name, especially if it is a common name. In a real scenario, the `UNIQUE` constraint should be applied to the `username` in any case, since the username is usually used as an alternate primary key. 

2. Including the `TVShow` table. When it comes to representing *Enums* in databases, there are two possibilities:

    - Inserting a table containing the possible values of the *Enum* and adding a *foreign key* in the main table.
    - inserting a *string* column in the main table

The decision can be made based on how much space each of the two approaches takes up. In general, it is better to insert an additional table if the *enum* has few values, so the *string* column would have many repetitions. 

In this task, I chose the fastest to implement option, which is to simply insert a *string* column, and ignored the space complexity issue.

## Execution

### Command prompt

First, create a virtual environment and activate it.
```bash
python -m venv .venv
source .venv/bin/activate # (Linux) .venv/Scripts/activate (Windows)
```

Second, install the dependencies.

```bash
pip install -r api/requirements.txt
```

Finally, start the FastAPI app.

```bash
cd api
python run.py
```

The API is available at [localhost:8080/](http://localhost:8080/).

### Docker 

Execute the following commands. To do so, it is necessary to have Docker and Docker Compose installed.

```bash
docker-compose build 
docker-compose up
```

The API is available at [localhost:8080/](http://localhost:8080/).

## Testing 

The tests can be found in the `test/` folder. To run the tests, execute the following commands:

```bash
cd api
python -m pytest ./test/
```

## Documentation 
Once the FastAPI app is running, the documentation is available under [localhost/8080/redoc](http://localhost:8080/redoc)


## Resources 

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [GUID type with SQLAlchemy](https://fastapi-utils.davidmontague.xyz/user-guide/basics/guid-type/)
- [Pydantic - Usage - Models](https://pydantic-docs.helpmanual.io/usage/models/)
- [DB configuration for testing](https://stackoverflow.com/questions/67255653/how-to-set-up-and-tear-down-a-database-between-tests-in-fastapi)