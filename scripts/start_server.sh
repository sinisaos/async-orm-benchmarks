#!/bin/bash

echo Choose an ORM or driver:

select result in piccolo tortoise sqlalchemy asyncpg psqlpy psycopg django oxyde yara;
do
    case $result in "piccolo") 
        cd benchmarks/piccolo_orm
        uv run uvicorn main:app --log-level error
        ;; 
        "tortoise") 
        cd benchmarks/tortoise_orm
        uv run uvicorn main:app --log-level error
        ;;
        "sqlalchemy") 
        cd benchmarks/sqlalchemy_orm
        uv run uvicorn main:app --log-level error
        ;; 
        "asyncpg") 
        cd benchmarks/asyncpg
        uv run uvicorn main:app --log-level error
        ;; 
        "psqlpy") 
        cd benchmarks/psqlpy
        uv run uvicorn main:app --log-level error
        ;; 
        "psycopg") 
        cd benchmarks/psycopg
        uv run uvicorn main:app --log-level error
        ;;
        "django") 
        cd benchmarks/django_orm
        uv run uvicorn core.asgi:application --log-level error
        ;;
        "oxyde") 
        cd benchmarks/oxyde_orm
        uv run uvicorn main:app --log-level error
        ;;
        "yara") 
        cd benchmarks/yara_orm
        uv run uvicorn main:app --log-level error
        ;;
        *)
        echo "ORM or driver does not exist!"
        ;;
    esac
done 


