#!/bin/bash

src_path="`pwd`/src/*"
venv_path="`pwd`/_build/venv"
working_path_python="`pwd`/_build/venv/bin/python3.14"
working_path_compile="`pwd`/_build/venv/bin/pip-compile"
output_file="`pwd`/_build/build-sources/requirements.txt"
pyproject_path="`pwd`/_build/build-sources/pyproject.toml"
dist_path="`pwd`/_build/dist"
build_sources_path="`pwd`/_build/build-sources"
external_lib_path="`pwd`/_external_lib/*.whl"
pip_version=26.0.0

if [ ! -d "`pwd`/_build" ]; then
    echo "Installation de l'environnement virtuel..."
    python3 -m venv $venv_path
    echo "Mise à jour de pip en version XXX"
    $working_path_python -m pip install --upgrade pip < $pip_version
    echo "Installation des outils..."
    $working_path_python -m pip install build wheel setuptools pip-tools
    echo "Compilation en cours..."
    mkdir $dist_path
    mkdir $build_sources_path

    cp -r $src_path $build_sources_path

    $working_path_compile --no-header --no-annotate --resolver=backtracking --output-file $output_file $pyproject_path
    echo "Installation des dépendances..."
    #$working_path_python -m pip install $external_lib_path
    $working_path_python -m pip install $build_sources_path

    echo "Création du .wheel..."
    $working_path_python -m build --wheel --outdir $dist_path $build_sources_path

fi
