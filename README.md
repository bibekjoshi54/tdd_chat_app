# Simple URL shortner using basic postgres sharding 


Warning:
- config.yaml is just for reference. Never commit you credentials or database information.
- Always use environment variables for the sensitive information.
- Never commit the .env file.
- When deploying have a script to generate the config.yaml
- I will move the database URI and other sensitive information to the environment variables in the future as this is currently on development


## Project Description
Simple python application using the python and postgres to implement the url shortner


NOTE:
- Some command might not be working as of now.
- Currently I am trying to setup the project structure and boilerplate clode.

### Make Commands
- `make setup`: Setups the development environment
- `make lint`: Runs the lint process using mypy and ruff
- `make format`: Formats the project using ruff
- `make unit_test`: Runs the unit test

### Containers

The project comes with Dockerfile which performs the multistage build
The docker image would not have development and test dependencies installed, and the final image would have only installed production dependencies.

To test inside the container you can use the docker compose.

**Warning**
I have made the UID and GUID as configrable in docker image to run the tests and coverage report. In production make sure to make this as static or have a seperate docker image for production

- `HOST_UID=$(id -u) HOST_GID=$(id -g) docker build --build-arg UID=$HOST_UID --build-arg GID=$HOST_GID -t tdd_chat_app_app:latest . ` 
- To quickly run above command: `./scripts/build-docker.sh`
- `docker compose run unit_tests`: Runs the unit_tests inside the container.


### Poetry

Poetry is used for managing the dependencies of the project.
`project.toml` file contains the configuration for the various tools used in this project.

#### Quick commands to remember:

- `poetry add --group test coverage`: Installs the coverage package as a test dependency
- `poetry add pydantic`: Installs the pydantic package as a dependency
- `poetry config --list`: Quickly check the environment variables related to the poetry
- `poetry run <Any commad>`: Runs the command inside the poetry virtual environment
- `poetry shell`: Activates the poetry virtual environment

### Pending Items
- Add support for GitHub actions
