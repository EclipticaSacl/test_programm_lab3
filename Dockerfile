FROM python:3.10

WORKDIR /app

COPY serial_fake.py .

CMD ["python", "-u", "serial_fake.py"]

