FROM python:3.10

WORKDIR /app

# install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src/pyback /app/app

EXPOSE 80
CMD ["uvicorn", "pyback.main:app", "--host", "0.0.0.0", "--port", "80"]
