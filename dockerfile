FROM python:3.11.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# RUN mkdir /code/
# WORKDIR /code/
# # COPY requirements.txt /code/
# COPY ./ /code/
# # COPY ./core/ /code/
# # COPY ./requirements.txt /code/
# # COPY ./manage.py /code/
# # COPY ./apps/ /code/
# # COPY ./templates/ /code/
# # COPY ./utils/ /code/
# # COPY ./dockerfile /code/
# # COPY ./docker-compose.yml /code/
# RUN pip install --upgrade pip

# # RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r ./requirements.txt

# EXPOSE 8000

# CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     postgresql-client \
#     && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]