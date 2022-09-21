FROM gcr.io/datamechanics/spark:platform-3.2-latest

USER root
RUN apt-get update && apt-get install -y python3  python3-pip libffi-dev
#RUN apt-get install -y curl
ENV PYSPARK_MAJOR_PYTHON_VERSION=3

WORKDIR /opt/application/

COPY ./HelloExample1.ipynb .


RUN pip3 install jupyter
RUN jupyter nbconvert --to script HelloExample1.ipynb


