FROM python:3.9

WORKDIR /app

RUN apt-get update

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend-dir /app/backend-dir

ENTRYPOINT ["bash", "/app/entrypoint.sh"]

CMD ["uvicorn", "backend-dir.main:app", "--host", "0.0.0.0", "--port", "90"]