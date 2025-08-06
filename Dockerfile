FROM python:3.12

WORKDIR /usr/src/app


COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["uvicorn", "TodoApp.main:app", "--host", "0.0.0.0", "--port", "4000"]