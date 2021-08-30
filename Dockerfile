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
# ENTRYPOINT ["gunicorn", "-w", "3", "-b", "0.0.0.0:$PORT", "todo_app.app:create_app()"]
ENTRYPOINT gunicorn -w 3 -b 0.0.0.0:$PORT todo_app.app:create_app()

FROM base AS development
RUN poetry install 
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"] 

FROM base AS test
RUN poetry install
RUN apt-get update -qqy && apt-get install -qqy wget gnupg unzip

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install Chrome WebDriver
RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
  && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && unzip /tmp/chromedriver_linux64.zip -d /usr/bin \
  && rm /tmp/chromedriver_linux64.zip \
  && chmod 755 /usr/bin/chromedriver
ENTRYPOINT ["poetry", "run", "pytest"] 
