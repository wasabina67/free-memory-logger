#!/bin/bash

isort src/graph.py
black src/graph.py
flake8 src/graph.py
mypy src/graph.py
