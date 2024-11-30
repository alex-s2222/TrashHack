FROM python:3.11

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

COPY . ./

CMD alembic upgrade head && \
    uvicorn --host=0.0.0.0 app.main:app