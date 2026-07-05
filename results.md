# Piccolo ORM + FastAPI (4 workers)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      6021.43    1012.88    8849.58
  Latency       83.00ms    26.43ms   839.00ms
  Latency Distribution
     50%    74.09ms
     75%    91.97ms
     90%   119.02ms
     95%   142.05ms
     99%   218.98ms
  HTTP codes:
    1xx - 0, 2xx - 361641, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.52MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      5008.93    1255.92    9222.34
  Latency       99.71ms    47.30ms      0.95s
  Latency Distribution
     50%    75.50ms
     75%   120.07ms
     90%   175.90ms
     95%   215.94ms
     99%   333.00ms
  HTTP codes:
    1xx - 0, 2xx - 301040, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.07MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2137.60     454.15    3601.88
  Latency      233.37ms   143.07ms      2.52s
  Latency Distribution
     50%   186.98ms
     75%   303.95ms
     90%   432.07ms
     95%   528.93ms
     99%   808.01ms
  HTTP codes:
    1xx - 0, 2xx - 128750, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   113.68MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3817.88    1296.30    8143.20
  Latency      130.84ms    67.39ms      1.49s
  Latency Distribution
     50%   103.00ms
     75%   162.02ms
     90%   235.95ms
     95%   286.01ms
     99%   444.00ms
  HTTP codes:
    1xx - 0, 2xx - 229486, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.77MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1594.09     459.01    3461.89
  Latency      313.10ms   234.00ms      3.45s
  Latency Distribution
     50%   262.95ms
     75%   427.95ms
     90%   622.53ms
     95%   781.92ms
     99%      1.21s
  HTTP codes:
    1xx - 0, 2xx - 96066, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    24.65MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1933.12     869.09    6315.27
  Latency      257.83ms   164.62ms      2.20s
  Latency Distribution
     50%   195.12ms
     75%   303.98ms
     90%   498.95ms
     95%   623.99ms
     99%      0.93s
  HTTP codes:
    1xx - 0, 2xx - 116564, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.36MB/s
```

# Tortoise ORM + FastAPI (4 workers)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      5342.38    1094.76    8649.37
  Latency       93.51ms    33.05ms      0.97s
  Latency Distribution
     50%    84.97ms
     75%   105.93ms
     90%   133.00ms
     95%   153.66ms
     99%   222.10ms
  HTTP codes:
    1xx - 0, 2xx - 320954, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     7.56MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4596.76    1388.99    9669.24
  Latency      108.62ms    52.57ms      1.18s
  Latency Distribution
     50%    87.00ms
     75%   118.09ms
     90%   188.95ms
     95%   234.99ms
     99%   363.99ms
  HTTP codes:
    1xx - 0, 2xx - 276368, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     0.98MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2026.31     479.85    4297.70
  Latency      246.31ms   179.98ms      3.02s
  Latency Distribution
     50%   178.94ms
     75%   320.97ms
     90%   470.01ms
     95%   619.02ms
     99%      1.04s
  HTTP codes:
    1xx - 0, 2xx - 122073, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   107.59MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3403.86    1518.43    8552.33
  Latency      146.70ms    76.79ms      1.95s
  Latency Distribution
     50%   116.06ms
     75%   168.96ms
     90%   261.00ms
     95%   319.00ms
     99%   498.94ms
  HTTP codes:
    1xx - 0, 2xx - 204661, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.26MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       730.45     213.95    1417.69
  Latency      680.76ms   338.29ms      3.85s
  Latency Distribution
     50%   610.92ms
     75%   838.08ms
     90%      1.09s
     95%      1.31s
     99%      1.80s
  HTTP codes:
    1xx - 0, 2xx - 44284, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    11.21MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1153.48     386.04    2559.84
  Latency      431.30ms   248.07ms      4.33s
  Latency Distribution
     50%   362.01ms
     75%   523.02ms
     90%   739.96ms
     95%      0.91s
     99%      1.44s
  HTTP codes:
    1xx - 0, 2xx - 69738, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   803.93KB/s
```

# Oxyde ORM + FastAPI (4 workers)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      5458.84    1252.68   10421.19
  Latency       91.52ms    18.39ms   271.25ms
  Latency Distribution
     50%    81.12ms
     75%   108.12ms
     90%   137.05ms
     95%   148.66ms
     99%   171.87ms
  HTTP codes:
    1xx - 0, 2xx - 327958, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     7.72MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      5218.21    1581.21   12408.67
  Latency       95.72ms    14.97ms   210.55ms
  Latency Distribution
     50%    98.88ms
     75%   112.91ms
     90%   126.14ms
     95%   136.00ms
     99%   159.00ms
  HTTP codes:
    1xx - 0, 2xx - 313626, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.12MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1747.71     443.55    3302.22
  Latency      285.49ms    98.88ms   631.03ms
  Latency Distribution
     50%   311.96ms
     75%   378.88ms
     90%   434.99ms
     95%   460.04ms
     99%   505.23ms
  HTTP codes:
    1xx - 0, 2xx - 105339, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    93.65MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4748.49    1356.57    9904.82
  Latency      105.23ms    24.14ms   270.61ms
  Latency Distribution
     50%   103.04ms
     75%   135.00ms
     90%   158.07ms
     95%   173.04ms
     99%   204.15ms
  HTTP codes:
    1xx - 0, 2xx - 285281, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     5.98MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1370.58     719.95    5437.88
  Latency      363.60ms   117.92ms   767.00ms
  Latency Distribution
     50%   338.00ms
     75%   482.92ms
     90%   550.96ms
     95%   586.90ms
     99%   640.00ms
  HTTP codes:
    1xx - 0, 2xx - 82746, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    22.68MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1902.09     993.60    6689.53
  Latency      262.26ms    98.01ms   595.81ms
  Latency Distribution
     50%   279.07ms
     75%   364.97ms
     90%   410.99ms
     95%   434.94ms
     99%   470.04ms
  HTTP codes:
    1xx - 0, 2xx - 114655, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.36MB/s
```

# Drizzle ORM + Hono (4 instances)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     10810.08    1399.57   13669.70
  Latency       46.24ms     9.97ms   591.28ms
  Latency Distribution
     50%    46.84ms
     75%    51.52ms
     90%    55.50ms
     95%    58.89ms
     99%    69.38ms
  HTTP codes:
    1xx - 0, 2xx - 648927, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    15.60MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     10666.83    1285.93   13945.34
  Latency       46.85ms     6.58ms   295.71ms
  Latency Distribution
     50%    40.05ms
     75%    61.38ms
     90%    69.00ms
     95%    72.28ms
     99%    77.20ms
  HTTP codes:
    1xx - 0, 2xx - 640393, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.58MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2510.92     386.32    3653.83
  Latency      198.80ms    45.21ms      1.27s
  Latency Distribution
     50%   196.33ms
     75%   221.65ms
     90%   248.46ms
     95%   263.08ms
     99%   298.10ms
  HTTP codes:
    1xx - 0, 2xx - 151104, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   128.86MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      6453.19     904.88   10290.66
  Latency       77.43ms     9.87ms   424.49ms
  Latency Distribution
     50%    77.06ms
     75%    85.25ms
     90%    93.14ms
     95%    98.25ms
     99%   109.30ms
  HTTP codes:
    1xx - 0, 2xx - 387496, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.01MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2479.32     461.02    3918.97
  Latency      201.34ms    37.12ms      1.15s
  Latency Distribution
     50%   198.49ms
     75%   219.64ms
     90%   237.65ms
     95%   248.83ms
     99%   276.38ms
  HTTP codes:
    1xx - 0, 2xx - 149144, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    42.44MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3094.35     705.83    7722.60
  Latency      161.43ms    44.61ms      1.23s
  Latency Distribution
     50%   154.57ms
     75%   181.06ms
     90%   211.55ms
     95%   235.09ms
     99%   289.44ms
  HTTP codes:
    1xx - 0, 2xx - 185908, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.34MB/s
```

# Ent ORM + Chi

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      7795.19     639.15    9382.30
  Latency       64.09ms    48.76ms   737.39ms
  Latency Distribution
     50%    45.85ms
     75%    87.03ms
     90%   141.50ms
     95%   182.59ms
     99%   278.61ms
  HTTP codes:
    1xx - 0, 2xx - 468135, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    15.00MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      8024.07     575.62    9864.33
  Latency       62.28ms    46.82ms   708.66ms
  Latency Distribution
     50%    44.75ms
     75%    84.55ms
     90%   137.11ms
     95%   176.84ms
     99%   268.35ms
  HTTP codes:
    1xx - 0, 2xx - 481840, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.68MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      5970.46     880.06    7434.94
  Latency       83.72ms    68.67ms      1.00s
  Latency Distribution
     50%    59.28ms
     75%   113.04ms
     90%   185.23ms
     95%   240.65ms
     99%   373.89ms
  HTTP codes:
    1xx - 0, 2xx - 358525, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   281.40MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      7476.53     635.15    9439.92
  Latency       66.84ms    51.03ms   837.46ms
  Latency Distribution
     50%    47.92ms
     75%    90.67ms
     90%   147.21ms
     95%   190.04ms
     99%   289.33ms
  HTTP codes:
    1xx - 0, 2xx - 449020, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.33MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2480.08     364.55    3542.51
  Latency      201.29ms   104.33ms      1.07s
  Latency Distribution
     50%   180.62ms
     75%   259.32ms
     90%   347.96ms
     95%   409.52ms
     99%   544.21ms
  HTTP codes:
    1xx - 0, 2xx - 149228, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    48.08MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2028.01     305.88    3098.07
  Latency      245.94ms   112.08ms      1.15s
  Latency Distribution
     50%   226.71ms
     75%   310.03ms
     90%   403.09ms
     95%   464.75ms
     99%   599.25ms
  HTTP codes:
    1xx - 0, 2xx - 122150, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.61MB/s
```

# SQLC + Chi

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      8127.48     572.20    9760.38
  Latency       61.51ms    46.35ms      0.89s
  Latency Distribution
     50%    44.11ms
     75%    83.55ms
     90%   135.57ms
     95%   174.82ms
     99%   267.19ms
  HTTP codes:
    1xx - 0, 2xx - 487811, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    11.37MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      8361.39     428.98    9730.58
  Latency       59.77ms    44.53ms   692.56ms
  Latency Distribution
     50%    42.95ms
     75%    81.04ms
     90%   131.57ms
     95%   169.71ms
     99%   256.57ms
  HTTP codes:
    1xx - 0, 2xx - 502096, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.66MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      7009.12     600.27    8238.52
  Latency       71.32ms    55.81ms      1.04s
  Latency Distribution
     50%    50.80ms
     75%    96.61ms
     90%   157.54ms
     95%   204.16ms
     99%   312.34ms
  HTTP codes:
    1xx - 0, 2xx - 420905, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   356.37MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      7959.51     503.11    9831.42
  Latency       62.79ms    47.37ms      0.86s
  Latency Distribution
     50%    45.16ms
     75%    85.35ms
     90%   138.03ms
     95%   177.55ms
     99%   271.99ms
  HTTP codes:
    1xx - 0, 2xx - 477957, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     9.46MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      6460.03     492.57    7862.06
  Latency       77.37ms    61.53ms      0.95s
  Latency Distribution
     50%    55.22ms
     75%   104.92ms
     90%   171.41ms
     95%   221.82ms
     99%   339.08ms
  HTTP codes:
    1xx - 0, 2xx - 388009, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   112.64MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      7139.43     481.87    9079.29
  Latency       69.99ms    54.02ms      0.90s
  Latency Distribution
     50%    50.20ms
     75%    95.22ms
     90%   154.62ms
     95%   199.30ms
     99%   302.22ms
  HTTP codes:
    1xx - 0, 2xx - 428755, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     5.19MB/s
```
