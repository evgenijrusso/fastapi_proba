FROM python:3.11.3-slim

# Set the current working directory to /code.
WORKDIR /code

# Copy the pyproject.toml and poetry.lock files.
COPY ./pyproject.toml ./poetry.lock* /code/

# Install dependencies
RUN poetry install --only main --all-extras

COPY . /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]