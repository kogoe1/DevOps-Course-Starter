FROM python:3.8.8-buster AS base
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
EXPOSE 5000
ENV PATH="${PATH}:/root/.poetry/bin"
RUN mkdir -p /devops_mod5
WORKDIR /devops_mod5
COPY . /devops_mod5
RUN poetry install 
ENV VIRTUAL_ENV=.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

FROM base AS production
ENTRYPOINT ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "todo_app.app:app"]

FROM base AS development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"] 