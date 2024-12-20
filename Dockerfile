FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt 

COPY . /app/

RUN python manage.py collectstatic --noinput -v 2

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "apt_ca.wsgi:application"]