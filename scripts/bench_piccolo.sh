#!/bin/bash

echo '# Piccolo ORM' >> results/results_piccolo.md
echo '### Small table (50 rows)' >> results/results_piccolo.md
echo '```bash' >> results/results_piccolo.md
bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/small-table/ >> results/results_piccolo.md
echo '```' >> results/results_piccolo.md
echo "### Small table (single row)" >> results/results_piccolo.md
echo '```bash' >> results/results_piccolo.md
bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/small-table/1/ >> results/results_piccolo.md
echo '```' >> results/results_piccolo.md
echo "### Mega table (50 rows)" >> results/results_piccolo.md
echo '```bash' >> results/results_piccolo.md
bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/mega-table/ >> results/results_piccolo.md
echo '```' >> results/results_piccolo.md
echo "### Mega table (single row)" >> results/results_piccolo.md
echo '```bash' >> results/results_piccolo.md
bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/mega-table/1/ >> results/results_piccolo.md
echo '```' >> results/results_piccolo.md
echo "### Related table (50 rows)" >> results/results_piccolo.md
echo '```bash' >> results/results_piccolo.md
bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/related-table/ >> results/results_piccolo.md
echo '```' >> results/results_piccolo.md
echo "### Related table (single row)" >> results/results_piccolo.md
echo '```bash' >> results/results_piccolo.md
bombardier -c 200 -d 10s -l --print=intro,result http://localhost:8000/related-table/1/ >> results/results_piccolo.md
echo '```' >> results/results_piccolo.md
