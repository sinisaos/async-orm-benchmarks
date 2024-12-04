# Psycopg
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       660.16     199.48    1292.66
  Latency      296.89ms    74.95ms      1.03s
  Latency Distribution
     50%   286.06ms
     75%   335.43ms
     90%   390.63ms
     95%   446.33ms
     99%   472.63ms
  HTTP codes:
    1xx - 0, 2xx - 6785, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     0.95MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       740.01     189.16    1478.30
  Latency      265.39ms    31.27ms   461.73ms
  Latency Distribution
     50%   257.09ms
     75%   266.52ms
     90%   298.53ms
     95%   339.60ms
     99%   363.96ms
  HTTP codes:
    1xx - 0, 2xx - 7585, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   163.81KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       338.06     106.00     522.34
  Latency      570.65ms    68.21ms   849.92ms
  Latency Distribution
     50%   560.61ms
     75%   591.07ms
     90%   615.17ms
     95%   715.92ms
     99%   796.72ms
  HTTP codes:
    1xx - 0, 2xx - 3577, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    18.28MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       553.83     149.81    1238.88
  Latency      352.95ms    50.89ms   737.05ms
  Latency Distribution
     50%   340.73ms
     75%   367.96ms
     90%   386.82ms
     95%   475.32ms
     99%   531.22ms
  HTTP codes:
    1xx - 0, 2xx - 5711, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   719.66KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       245.80     141.65     529.63
  Latency      779.40ms    97.49ms      1.24s
  Latency Distribution
     50%   757.55ms
     75%   808.41ms
     90%      0.91s
     95%      0.95s
     99%      1.13s
  HTTP codes:
    1xx - 0, 2xx - 2640, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.86MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       242.42      96.13     556.78
  Latency      784.18ms   245.24ms      1.95s
  Latency Distribution
     50%   747.30ms
     75%      0.87s
     90%      1.10s
     95%      1.22s
     99%      1.67s
  HTTP codes:
    1xx - 0, 2xx - 2612, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   181.06KB/s
```
