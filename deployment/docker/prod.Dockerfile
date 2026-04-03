FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=.
ENV PIP_BREAK_SYSTEM_PACKAGES=1

WORKDIR /usr/app

ARG ARTIFACT_PATH
COPY ${ARTIFACT_PATH} ./

RUN apt update && apt upgrade -y && \
    apt install -y wget build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
    python3-openssl git libpq-dev

RUN wget https://www.python.org/ftp/python/3.14.0/Python-3.14.0.tar.xz && \
    tar -xf Python-3.14.0.tar.xz && \
    cd Python-3.14.0 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.14.0 Python-3.14.0.tar.xz

RUN python3.14 --version

RUN python3.14 -m pip install --break-system-packages -U pip setuptools wheel Cython

RUN python3.14 -m pip install ./dist/*.whl

WORKDIR /usr/app/build-sources

CMD ["python3.14", "server_template/main.py"]
