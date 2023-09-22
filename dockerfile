from python:3.11.5-alpine3.17
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]