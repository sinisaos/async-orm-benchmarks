# Tortoise ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       593.88     119.21     862.69
  Latency      330.12ms   140.20ms      1.42s
  Latency Distribution
     50%   313.55ms
     75%   332.77ms
     90%   452.31ms
     95%   612.55ms
     99%   814.67ms
  HTTP codes:
    1xx - 0, 2xx - 6125, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   867.67KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       598.70      89.12     871.15
  Latency      327.47ms   150.64ms      1.26s
  Latency Distribution
     50%   320.63ms
     75%   327.68ms
     90%   436.06ms
     95%   630.20ms
     99%   841.33ms
  HTTP codes:
    1xx - 0, 2xx - 6174, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   132.05KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       219.91      74.36     454.31
  Latency         0.86s   602.14ms      5.19s
  Latency Distribution
     50%   797.24ms
     75%      1.00s
     90%      1.35s
     95%      1.83s
     99%      3.18s
  HTTP codes:
    1xx - 0, 2xx - 2389, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    11.96MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       405.58     104.13     802.70
  Latency      476.76ms   207.78ms      1.98s
  Latency Distribution
     50%   466.50ms
     75%   520.15ms
     90%   594.60ms
     95%      0.91s
     99%      1.06s
  HTTP codes:
    1xx - 0, 2xx - 4245, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   530.55KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        18.25      40.25     207.93
  Latency         5.89s      3.66s     10.04s
  Latency Distribution
     50%      5.61s
     75%     10.01s
     90%     10.02s
     95%     10.03s
     99%     10.04s
  HTTP codes:
    1xx - 0, 2xx - 254, 3xx - 0, 4xx - 0, 5xx - 0
    others - 127
  Errors:
       timeout - 127
  Throughput:   313.98KB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       140.52     111.63     620.25
  Latency         1.31s   330.01ms      3.60s
  Latency Distribution
     50%      1.23s
     75%      1.44s
     90%      1.61s
     95%      1.77s
     99%      2.86s
  HTTP codes:
    1xx - 0, 2xx - 1601, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   145.84KB/s
```
