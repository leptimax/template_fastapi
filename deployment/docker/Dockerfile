FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=.
ENV PIP_BREAK_SYSTEM_PACKAGES=1

WORKDIR /usr/app

ARG ARTIFACT_PATH
COPY ${ARTIFACT_PATH} ./

# Installation des dépendances nécessaires pour compiler Python
RUN apt update && apt upgrade -y && \
    apt install -y wget build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
    python3-openssl git libpq-dev

# Téléchargement et compilation de Python 3.14
RUN wget https://www.python.org/ftp/python/3.14.0/Python-3.14.0.tar.xz && \
    tar -xf Python-3.14.0.tar.xz && \
    cd Python-3.14.0 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.14.0 Python-3.14.0.tar.xz

# Vérification de l'installation
RUN python3.14 --version

# Installation des dépendances Python
RUN python3.14 -m pip install --break-system-packages -U pip setuptools wheel Cython

# Installation de votre package
RUN python3.14 -m pip install ./dist/*.whl

WORKDIR /usr/app/build-sources

# Utilisation de python3.14 pour lancer votre application
CMD ["python3.14", "server_template/main.py"]
