# base image
FROM python:3.10.6
# setup environment variable
ENV Books_drf=/home/app/webapp

# set work directory
RUN mkdir -p $Books_drf

# where your code lives
WORKDIR $Books_drf



# install dependencies
ARG POETRY_VERSION=1.3.2
RUN pip install --upgrade pip
RUN pip install "poetry==${POETRY_VERSION}"

# copy whole project to your docker home directory.
COPY . $Books_drf
ENV POETRY_VIRTUALENVS_ALWAYS_COPY=false
ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV POETRY_VIRTUALENVS_PATH=${DIR_CACHE}

RUN poetry env use "${PYTHON_VERSION}" \
    && poetry env info > ${DIR_CACHE}/.poetry-env-info.txt
RUN poetry install


EXPOSE 8080

CMD poetry run python manage.py makemigrations \
    && poetry run python manage.py migrate \
    && poetry run python manage.py runserver --noreload