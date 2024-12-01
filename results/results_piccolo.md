# Piccolo ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       714.43     170.52    2282.31
  Latency      276.37ms   134.96ms      1.37s
  Latency Distribution
     50%   267.22ms
     75%   297.98ms
     90%   487.91ms
     95%   535.62ms
     99%   742.25ms
  HTTP codes:
    1xx - 0, 2xx - 7291, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.01MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       699.16     163.97    1212.38
  Latency      280.92ms   144.28ms      1.26s
  Latency Distribution
     50%   271.81ms
     75%   305.10ms
     90%   504.39ms
     95%   542.58ms
     99%   775.01ms
  HTTP codes:
    1xx - 0, 2xx - 7174, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   154.49KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       276.25      88.23     515.48
  Latency      692.46ms   241.03ms      2.81s
  Latency Distribution
     50%   711.86ms
     75%   774.46ms
     90%   847.24ms
     95%      0.88s
     99%      1.53s
  HTTP codes:
    1xx - 0, 2xx - 2953, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    15.06MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       544.57     143.11    1003.20
  Latency      358.70ms   163.74ms      1.66s
  Latency Distribution
     50%   349.20ms
     75%   378.41ms
     90%   546.40ms
     95%   680.98ms
     99%      0.91s
  HTTP codes:
    1xx - 0, 2xx - 5629, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   706.80KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       223.23     101.85     521.07
  Latency      847.57ms   473.99ms      4.81s
  Latency Distribution
     50%   824.86ms
     75%      0.87s
     90%      1.56s
     95%      1.61s
     99%      2.83s
  HTTP codes:
    1xx - 0, 2xx - 2422, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.56MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       256.84      98.49     761.04
  Latency      735.53ms   336.15ms      2.77s
  Latency Distribution
     50%   721.13ms
     75%      0.94s
     90%      1.10s
     95%      1.39s
     99%      1.74s
  HTTP codes:
    1xx - 0, 2xx - 2756, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   286.95KB/s
```
