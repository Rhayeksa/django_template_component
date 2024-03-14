FROM python:3.11.8-alpine

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# WORKDIR /usr/src/app
WORKDIR /code
COPY . .
# COPY core/ /code/
# COPY requirements.txt /code/
# COPY manage.py /code/
# COPY apps/ /code/
# COPY templates/ /code/
# COPY utils/ /code/
# COPY dockerfile .
# COPY docker-compose.yml .
# RUN pip install --upgrade pip

# # RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python ./manage.py makemigrations
RUN python ./manage.py migrate

EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
