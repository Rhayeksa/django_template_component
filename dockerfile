FROM python:3.11.8-alpine

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# WORKDIR /usr/src/app
WORKDIR /code
COPY . .

# RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt
RUN python ./manage.py makemigrations
RUN python ./manage.py migrate

# USER django

EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
