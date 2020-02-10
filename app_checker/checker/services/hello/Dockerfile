FROM python:alpine3.6

COPY app.py /
COPY . /
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
