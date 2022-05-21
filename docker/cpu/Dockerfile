ARG BASE_CONTAINER=ghcr.io/makinarocks/python:3.8-base-cpu
FROM $BASE_CONTAINER

WORKDIR /assets

COPY README.md /assets/README.md
COPY setup.py /assets/setup.py
COPY src /assets/src

RUN pip3 install -e .
