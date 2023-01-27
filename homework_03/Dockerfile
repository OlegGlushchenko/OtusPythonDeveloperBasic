# For build image please use:
#
# docker build --progress plain . -t app_image
#
# For running this container please use this command:
#
# docker run --rm --name app_container -p 8000:8000 app_image
#
# which:
# - start container with "app_container" name
# - passthrough 8000 port into container
# - remove container after it stops

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000

WORKDIR /var/app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r /var/app/requirements.txt

COPY . .

CMD . /opt/venv/bin/activate && uvicorn main:app --host 0.0.0.0
