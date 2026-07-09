#!/bin/bash

echo "Running black..."
uv run black .
echo "-----"

echo "Running mypy..."
uv run mypy .
echo "-----"

echo "Running ruff..."
uv run ruff check . --fix
echo "-----"

echo "Finished"