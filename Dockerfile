FROM Python:3.6.9-alpine
WORKDIR /Project
ADD . /Project
RUN pip3 install -r requirements.txt
CMD ["python3","create.py"]
CMD ["gunicorn","--workers=4","--bind=0.0.0.0:5000","app:app"]