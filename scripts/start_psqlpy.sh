#!/bin/bash

cd benchmarks/psqlpy
uvicorn main:app --log-level error