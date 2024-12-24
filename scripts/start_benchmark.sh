#!/bin/bash

echo Choose an ORM or driver:

generate_output() {

    select result in piccolo tortoise sqlalchemy asyncpg psqlpy psycopg django mayim;
    do
        case $result in "piccolo") 
            echo '# Piccolo ORM'
            ;; 
            "tortoise") 
            echo '# Tortoise ORM'
            ;;
            "sqlalchemy") 
            echo '# SqlAlchemy ORM'
            ;; 
            "asyncpg") 
            echo '# Asyncpg'
            ;; 
            "psqlpy") 
            echo '# PSQLPy'
            ;; 
            "psycopg") 
            echo '# Psycopg'
            ;;
            "django") 
            echo '# Django ORM'
            ;;
            "mayim") 
            echo '# Mayim'
            ;;
            *)
            echo "ORM or driver does not exist!"
            ;;
        esac
        echo '### Small table (50 rows)'
        echo '```bash'
        bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/small-table/
        echo '```'
        echo "### Small table (single row)"
        echo '```bash'
        bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/small-table/1/ 
        echo '```'
        echo "### Mega table (50 rows)"
        echo '```bash'
        bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/mega-table/
        echo '```'
        echo "### Mega table (single row)"
        echo '```bash'
        bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/mega-table/1/
        echo '```'
        echo "### Related table (50 rows)"
        echo '```bash'
        bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/related-table/
        echo '```'
        echo "### Related table (single row)"
        echo '```bash'
        bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/related-table/1/
        echo '```'
    exit 1
    done 
}

generate_output >> results.md

