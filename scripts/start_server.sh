#!/bin/bash

echo Choose an ORM or driver:

select result in piccolo tortoise oxyde drizzle ent sqlc;
do
    case $result in "piccolo") 
        cd benchmarks/piccolo_orm
        uvicorn main:app --workers 4 --log-level error
        ;; 
        "tortoise") 
        cd benchmarks/tortoise_orm
        uvicorn main:app --workers 4 --log-level error
        ;;
        "oxyde") 
        cd benchmarks/oxyde_orm
        uvicorn main:app --workers 4 --log-level error
        ;;
        "drizzle") 
        cd benchmarks/drizzle_orm
        pm2 start dist/index.js --instances 4
        ;;
        "ent") 
        cd benchmarks/ent_orm
        ./main
        ;;
        "sqlc") 
        cd benchmarks/sqlc
        ./main
        ;;
        *)
        echo "ORM or driver does not exist!"
        ;;
    esac
done 


