# Piccolo ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       738.72     136.35    1171.53
  Latency      266.42ms    35.10ms   622.90ms
  Latency Distribution
     50%   261.53ms
     75%   277.06ms
     90%   304.65ms
     95%   331.64ms
     99%   359.56ms
  HTTP codes:
    1xx - 0, 2xx - 7566, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.05MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       706.87     153.93    1397.61
  Latency      277.89ms    43.51ms   690.29ms
  Latency Distribution
     50%   264.44ms
     75%   281.79ms
     90%   332.11ms
     95%   371.39ms
     99%   417.43ms
  HTTP codes:
    1xx - 0, 2xx - 7243, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   156.30KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       305.96     120.25     521.24
  Latency      632.41ms   149.34ms      1.63s
  Latency Distribution
     50%   572.15ms
     75%   726.65ms
     90%      0.87s
     95%      0.90s
     99%      1.02s
  HTTP codes:
    1xx - 0, 2xx - 3257, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    16.36MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       516.65     152.04    1336.00
  Latency      376.97ms    61.21ms   655.10ms
  Latency Distribution
     50%   368.88ms
     75%   402.21ms
     90%   467.30ms
     95%   489.66ms
     99%   566.09ms
  HTTP codes:
    1xx - 0, 2xx - 5340, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   673.65KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       226.34     121.67     531.67
  Latency      840.51ms   109.92ms      1.39s
  Latency Distribution
     50%   809.91ms
     75%      0.90s
     90%      0.97s
     95%      1.00s
     99%      1.23s
  HTTP codes:
    1xx - 0, 2xx - 2449, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.57MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       232.59      77.00     620.54
  Latency      808.49ms   367.06ms      3.53s
  Latency Distribution
     50%   772.78ms
     75%      0.92s
     90%      1.25s
     95%      1.43s
     99%      2.00s
  HTTP codes:
    1xx - 0, 2xx - 2514, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   175.21KB/s
```
