#!/bin/bash

generate_output() {
    echo '# Piccolo ORM'
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
}

generate_output > results/results_piccolo.md
