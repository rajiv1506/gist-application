FROM python:3.8-slim AS dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000

ENV FLASK_APP=app.py

FROM dev AS test

COPY test.py /app/

CMD ["python", "-m", "unittest", "test.py"]

FROM dev AS prod

CMD ["flask", "run", "--host=0.0.0.0"]

