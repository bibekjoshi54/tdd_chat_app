FROM python:3.12.2-slim-bullseye as base

ARG UID=12120
ARG GID=12120
ARG POETRY_VERSION=1.7.1

ENV TINI_VERSION v0.19.0

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini


RUN apt-get update && apt-get -y install make && rm -rf /var/lib/apt/lists/* && pip install poetry==$POETRY_VERSION

WORKDIR /app/

RUN addgroup --gid $GID nonroot && \
  adduser --uid $UID --gid $GID --disabled-password --gecos "" nonroot && \
  echo 'nonroot ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers


COPY poetry.lock pyproject.toml README.md poetry.toml ./
RUN poetry install --no-interaction --no-ansi --without development,test
COPY tdd_chat_app tdd_chat_app/
RUN poetry install --only-root && chown -R nonroot:nonroot /app/
USER nonroot

FROM base as production

ENTRYPOINT ["/tini", "--"]
CMD ["poetry", "run", "python", "-m", "tdd_chat_app"]
