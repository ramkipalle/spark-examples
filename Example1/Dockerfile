FROM gcr.io/datamechanics/spark:platform-3.2-latest

ENV PYSPARK_MAJOR_PYTHON_VERSION=3

WORKDIR /opt/application/

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./main.py .