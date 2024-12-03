#!/bin/bash

cd benchmarks/sqlalchemy_orm
uvicorn main:app --log-level error