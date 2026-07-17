#!/bin/bash

echo Choose an ORM or driver:

generate_output() {

    select result in piccolo piccolo_enhanced tortoise oxyde yara;
    do
        case $result in "piccolo") 
            echo '# Piccolo ORM'
            ;; 
            "piccolo_enhanced") 
            echo '# Piccolo ORM(enhanced)'
            ;;
            "tortoise") 
            echo '# Tortoise ORM'
            ;;
            "oxyde") 
            echo '# Oxyde ORM'
            ;;
            "yara") 
            echo '# Yara ORM'
            ;;
            *)
            echo "ORM or driver does not exist!"
            ;;
        esac
        echo '### Small table (50 rows)'
        echo '```bash'
        bombardier -c 200 -d 60s -l --print=intro,result http://localhost:8000/small-table/
        echo '```'
        echo "### Small table (single row)"
        echo '```bash'
        bombardier -c 200 -d 60s -l --print=intro,result http://localhost:8000/small-table/1/ 
        echo '```'
        echo "### Mega table (50 rows)"
        echo '```bash'
        bombardier -c 200 -d 60s -l --print=intro,result http://localhost:8000/mega-table/
        echo '```'
        echo "### Mega table (single row)"
        echo '```bash'
        bombardier -c 200 -d 60s -l --print=intro,result http://localhost:8000/mega-table/1/
        echo '```'
        echo "### Related table (50 rows)"
        echo '```bash'
        bombardier -c 200 -d 60s -l --print=intro,result http://localhost:8000/related-table/
        echo '```'
        echo "### Related table (single row)"
        echo '```bash'
        bombardier -c 200 -d 60s -l --print=intro,result http://localhost:8000/related-table/1/
        echo '```'
    exit 1
    done 
}

generate_output >> results.md

