#!/bin/bash

echo Choose an ORM or driver:

select result in piccolo tortoise sqlalchemy asyncpg psqlpy psycopg;
do
    case $result in "piccolo") 
        cd benchmarks/piccolo_orm
        uvicorn main:app --log-level error
        ;; 
        "tortoise") 
        cd benchmarks/tortoise_orm
        uvicorn main:app --log-level error
        ;;
        "sqlalchemy") 
        cd benchmarks/sqlalchemy_orm
        uvicorn main:app --log-level error
        ;; 
        "asyncpg") 
        cd benchmarks/asyncpg
        uvicorn main:app --log-level error
        ;; 
        "psqlpy") 
        cd benchmarks/psqlpy
        uvicorn main:app --log-level error
        ;; 
        "psycopg") 
        cd benchmarks/psycopg
        uvicorn main:app --log-level error
        ;;
        *)
        echo "ORM or driver does not exist!"
        ;;
    esac
done 


