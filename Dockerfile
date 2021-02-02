FROM python:3.6.9-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["gunicorn","--workers=4","--bind=0.0.0.0:5000","app:app"]