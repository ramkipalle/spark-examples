FROM gcr.io/datamechanics/spark:platform-3.2-latest

USER root
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN apt-get update && apt-get install -y apt-transport-https python3  python3-pip libffi-dev
ENV PYSPARK_MAJOR_PYTHON_VERSION=3

WORKDIR /opt/application/

COPY ./VSCodeNotebookExample.ipynb .

RUN pip3 install jupyter
RUN conda update jupyter_core jupyter_client
RUN jupyter nbconvert --to script VSCodeNotebookExample.ipynb