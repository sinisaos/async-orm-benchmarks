# Piccolo ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       539.17     112.55     901.55
  Latency      362.51ms   215.46ms      1.67s
  Latency Distribution
     50%   354.56ms
     75%   390.07ms
     90%   677.48ms
     95%   710.40ms
     99%      1.02s
  HTTP codes:
    1xx - 0, 2xx - 5573, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   790.51KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       537.92     112.66     934.87
  Latency      363.11ms   226.63ms      2.42s
  Latency Distribution
     50%   363.07ms
     75%   378.67ms
     90%   697.37ms
     95%   728.53ms
     99%      1.06s
  HTTP codes:
    1xx - 0, 2xx - 5563, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   119.23KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       262.78      76.04     517.71
  Latency      728.84ms   276.90ms      3.38s
  Latency Distribution
     50%   735.50ms
     75%   761.84ms
     90%   808.16ms
     95%      1.34s
     99%      1.52s
  HTTP codes:
    1xx - 0, 2xx - 2821, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    14.20MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       363.69     120.78     836.42
  Latency      529.88ms   289.17ms      3.07s
  Latency Distribution
     50%   550.00ms
     75%   613.04ms
     90%      0.90s
     95%      1.09s
     99%      1.53s
  HTTP codes:
    1xx - 0, 2xx - 3816, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   477.64KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       197.00      87.60     530.71
  Latency         0.96s   539.13ms      4.92s
  Latency Distribution
     50%      0.98s
     75%      1.02s
     90%      1.79s
     95%      1.91s
     99%      3.01s
  HTTP codes:
    1xx - 0, 2xx - 2155, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.14MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       223.70      87.18     581.77
  Latency      838.98ms   381.17ms      3.64s
  Latency Distribution
     50%   834.81ms
     75%      0.91s
     90%      1.27s
     95%      1.38s
     99%      1.94s
  HTTP codes:
    1xx - 0, 2xx - 2427, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   250.96KB/s
```
