FROM python:3.5-alpine AS compile-image
RUN apk add --no-cache gcc libc-dev libjpeg-turbo-dev zlib-dev
COPY requirements/ /tmp/requirements/
RUN pyvenv /venv \
	&& /venv/bin/pip install -U pip \
	&& LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install -r /tmp/requirements/base.txt"


FROM python:3.5-alpine AS dev-image
COPY --from=compile-image /venv /venv
RUN apk add --no-cache libjpeg-turbo-dev
ENV PATH=/venv/bin:$PATH

RUN mkdir /code/
WORKDIR /code/
ADD . /code/
EXPOSE 8000