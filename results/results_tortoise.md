# Tortoise ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       538.90     163.86    1102.83
  Latency      361.61ms   106.21ms      1.06s
  Latency Distribution
     50%   342.92ms
     75%   407.32ms
     90%   504.55ms
     95%   551.93ms
     99%   666.55ms
  HTTP codes:
    1xx - 0, 2xx - 5572, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   793.81KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       689.16      84.63    1322.16
  Latency      284.87ms    24.63ms   637.94ms
  Latency Distribution
     50%   284.02ms
     75%   288.37ms
     90%   293.83ms
     95%   318.46ms
     99%   378.40ms
  HTTP codes:
    1xx - 0, 2xx - 7070, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   152.43KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       298.92      64.93     482.22
  Latency      642.31ms    63.23ms      0.89s
  Latency Distribution
     50%   643.05ms
     75%   677.68ms
     90%   695.80ms
     95%   699.71ms
     99%   791.75ms
  HTTP codes:
    1xx - 0, 2xx - 3180, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    16.21MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       454.14      90.02    1068.20
  Latency      426.83ms    67.80ms      1.04s
  Latency Distribution
     50%   410.11ms
     75%   457.43ms
     90%   508.08ms
     95%   564.37ms
     99%   621.45ms
  HTTP codes:
    1xx - 0, 2xx - 4725, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   594.25KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        23.09      37.32     208.85
  Latency         5.41s      3.89s     10.02s
  Latency Distribution
     50%      4.48s
     75%     10.00s
     90%     10.01s
     95%     10.01s
     99%     10.02s
  HTTP codes:
    1xx - 0, 2xx - 297, 3xx - 0, 4xx - 0, 5xx - 0
    others - 133
  Errors:
       timeout - 133
  Throughput:   350.09KB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       160.41      83.61     469.35
  Latency         1.15s   530.61ms      4.96s
  Latency Distribution
     50%      1.05s
     75%      1.38s
     90%      1.65s
     95%      1.90s
     99%      3.32s
  HTTP codes:
    1xx - 0, 2xx - 1800, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   118.04KB/s
```
