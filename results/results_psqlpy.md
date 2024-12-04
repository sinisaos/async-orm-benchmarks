# PSQLPy
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       950.27     216.33    1613.94
  Latency      207.90ms    42.47ms   390.57ms
  Latency Distribution
     50%   189.21ms
     75%   202.53ms
     90%   287.43ms
     95%   304.14ms
     99%   353.96ms
  HTTP codes:
    1xx - 0, 2xx - 9663, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.35MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1032.29     148.75    1873.72
  Latency      191.59ms    22.40ms   324.25ms
  Latency Distribution
     50%   186.41ms
     75%   189.75ms
     90%   198.42ms
     95%   253.24ms
     99%   283.42ms
  HTTP codes:
    1xx - 0, 2xx - 10487, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   227.04KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       295.02      83.20     482.61
  Latency      654.87ms   117.39ms      0.90s
  Latency Distribution
     50%   653.29ms
     75%   730.60ms
     90%   799.96ms
     95%   841.97ms
     99%      0.88s
  HTTP codes:
    1xx - 0, 2xx - 3148, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    15.78MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       905.03     162.31    1591.05
  Latency      218.06ms    28.35ms   360.37ms
  Latency Distribution
     50%   204.53ms
     75%   236.90ms
     90%   256.24ms
     95%   276.34ms
     99%   313.71ms
  HTTP codes:
    1xx - 0, 2xx - 9218, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.14MB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       501.34      86.97     675.48
  Latency      390.22ms    44.42ms   534.82ms
  Latency Distribution
     50%   382.14ms
     75%   392.59ms
     90%   465.94ms
     95%   475.89ms
     99%   508.06ms
  HTTP codes:
    1xx - 0, 2xx - 5205, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.34MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       912.25     130.14    1540.79
  Latency      216.72ms    14.49ms   344.77ms
  Latency Distribution
     50%   214.80ms
     75%   218.66ms
     90%   232.96ms
     95%   240.08ms
     99%   255.25ms
  HTTP codes:
    1xx - 0, 2xx - 9291, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   682.83KB/s
```
