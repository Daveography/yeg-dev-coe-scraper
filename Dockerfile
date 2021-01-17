FROM selenium/standalone-chrome:87.0

USER root
WORKDIR /app/

# Install Python and Poetry
RUN sudo apt-get update && apt-get install -y python3.7 python3-pip
RUN python3 -m pip install -U pip
RUN python3 -m pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev

# Copy the app
COPY scraper/ scraper/

ENV TZ=America/Edmonton PYTHONPATH=.

CMD python3 -m scraper
