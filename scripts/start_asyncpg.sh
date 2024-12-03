#!/bin/bash

cd benchmarks/asyncpg
uvicorn main:app --log-level error