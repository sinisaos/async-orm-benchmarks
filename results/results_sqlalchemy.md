# SqlAlchemy ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       208.85     128.98     620.66
  Latency         0.91s   429.40ms      3.19s
  Latency Distribution
     50%   778.21ms
     75%   818.36ms
     90%      0.98s
     95%      1.78s
     99%      3.10s
  HTTP codes:
    1xx - 0, 2xx - 2282, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   309.09KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       354.82     202.97     789.49
  Latency      542.46ms   223.67ms      1.80s
  Latency Distribution
     50%   492.48ms
     75%   535.16ms
     90%   631.16ms
     95%      1.08s
     99%      1.62s
  HTTP codes:
    1xx - 0, 2xx - 3733, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    79.54KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        10.32      61.95     764.10
  Latency         7.26s      3.71s     10.02s
  Latency Distribution
     50%     10.00s
     75%     10.01s
     90%     10.01s
     95%     10.01s
     99%     10.02s
  HTTP codes:
    1xx - 0, 2xx - 122, 3xx - 0, 4xx - 0, 5xx - 0
    others - 181
  Errors:
       timeout - 181
  Throughput:   410.65KB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       338.24     266.23     878.15
  Latency      567.58ms   206.90ms      1.74s
  Latency Distribution
     50%   501.17ms
     75%   551.74ms
     90%   624.51ms
     95%      0.96s
     99%      1.60s
  HTTP codes:
    1xx - 0, 2xx - 3578, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   445.09KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec         6.09      38.80     408.21
  Latency         8.08s      3.37s     10.04s
  Latency Distribution
     50%     10.02s
     75%     10.03s
     90%     10.03s
     95%     10.04s
     99%     10.04s
  HTTP codes:
    1xx - 0, 2xx - 71, 3xx - 0, 4xx - 0, 5xx - 0
    others - 189
  Errors:
       timeout - 189
  Throughput:    68.17KB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       128.46     109.81     462.25
  Latency         1.42s   376.50ms      3.64s
  Latency Distribution
     50%      1.38s
     75%      1.40s
     90%      1.49s
     95%      1.77s
     99%      3.54s
  HTTP codes:
    1xx - 0, 2xx - 1480, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   101.38KB/s
```
