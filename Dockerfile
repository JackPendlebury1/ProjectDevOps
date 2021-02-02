FROM python:3.6-onbuild
WORKDIR /devopsproject
ADD . /devopsproject
RUN pip install -r requirements.txt
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app:app"]