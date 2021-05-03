FROM python:3.8.8-buster AS base
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
EXPOSE 5000
ENV PATH="${PATH}:/root/.poetry/bin"
RUN mkdir -p /devops_mod5
WORKDIR /devops_mod5
COPY . /devops_mod5

FROM base AS production
RUN poetry config virtualenvs.create false --local && poetry install --no-dev --no-root
ENTRYPOINT ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "todo_app.app:create_app()"]

FROM base AS development
RUN poetry install 
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"] 