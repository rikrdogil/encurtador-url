FROM python:3.9-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.



COPY pyproject.toml ./
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false



ENV LOG_LEVEL info


COPY ./tests ./tests

RUN poetry install --no-root


# # for migrations
 COPY migrations .
 COPY aerich.ini .

COPY src/ .
