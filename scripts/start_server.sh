#!/bin/bash

echo Choose an ORM or driver:

select result in piccolo piccolo_enhanced tortoise oxyde yara;
do
    case $result in "piccolo") 
        cd benchmarks/piccolo_orm
        uv run uvicorn main:app --log-level error
        ;; 
        "piccolo_enhanced") 
        cd benchmarks/piccolo_enhanced
        uv run uvicorn main:app --log-level error
        ;;
        "tortoise") 
        cd benchmarks/tortoise_orm
        uv run uvicorn main:app --log-level error
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


