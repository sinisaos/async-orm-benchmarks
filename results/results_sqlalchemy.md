# SqlAlchemy ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       204.86     175.04     731.59
  Latency         0.92s   229.09ms      1.86s
  Latency Distribution
     50%      0.87s
     75%      1.00s
     90%      1.19s
     95%      1.44s
     99%      1.79s
  HTTP codes:
    1xx - 0, 2xx - 2240, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   306.75KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       414.53     176.53     806.35
  Latency      467.52ms   120.39ms      1.20s
  Latency Distribution
     50%   436.90ms
     75%   480.36ms
     90%   490.79ms
     95%   502.77ms
     99%      1.09s
  HTTP codes:
    1xx - 0, 2xx - 4335, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    92.36KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        13.76      62.56     490.65
  Latency         6.59s      3.80s     10.03s
  Latency Distribution
     50%      8.90s
     75%     10.01s
     90%     10.02s
     95%     10.02s
     99%     10.03s
  HTTP codes:
    1xx - 0, 2xx - 170, 3xx - 0, 4xx - 0, 5xx - 0
    others - 168
  Errors:
       timeout - 168
  Throughput:   485.52KB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       308.07     181.45     843.59
  Latency      620.23ms   253.76ms      1.94s
  Latency Distribution
     50%   565.35ms
     75%   611.53ms
     90%   734.42ms
     95%      1.29s
     99%      1.82s
  HTTP codes:
    1xx - 0, 2xx - 3276, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   407.08KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec         8.30      41.98     480.72
  Latency         7.56s      3.69s     10.03s
  Latency Distribution
     50%     10.01s
     75%     10.01s
     90%     10.02s
     95%     10.02s
     99%     10.03s
  HTTP codes:
    1xx - 0, 2xx - 92, 3xx - 0, 4xx - 0, 5xx - 0
    others - 191
  Errors:
       timeout - 191
  Throughput:    85.85KB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       127.49     143.00     516.49
  Latency         1.43s   603.46ms      3.90s
  Latency Distribution
     50%      1.26s
     75%      1.28s
     90%      1.76s
     95%      3.41s
     99%      3.78s
  HTTP codes:
    1xx - 0, 2xx - 1470, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    99.40KB/s
```
