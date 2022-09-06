# Small API 

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
python main.py
```

The API is available at [localhost:8080/](http://localhost:8080/).

### Docker 

Execute the following commands. To do so is necessary to have Docker and Docker Compose installed.

```bash
docker-compose build 
docker-compose up
```

The API is available at [localhost:8080/](http://localhost:8080/).


## API Documentation 
Once the FastAPI app is running, the documentation is available under [localhost/8080/redoc](http://localhost:8080/redoc)

## Resources 

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [GUID type with SQLAlchemy](https://fastapi-utils.davidmontague.xyz/user-guide/basics/guid-type/)
- [Pydantic - Usage - Models](https://pydantic-docs.helpmanual.io/usage/models/)