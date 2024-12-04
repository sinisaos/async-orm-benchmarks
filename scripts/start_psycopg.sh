#!/bin/bash

cd benchmarks/psycopg
uvicorn main:app --log-level error