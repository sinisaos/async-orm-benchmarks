# Piccolo ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1908.26     385.13    2464.17
  Latency      104.72ms    35.66ms   689.13ms
  Latency Distribution
     50%    97.22ms
     75%   111.25ms
     90%   131.93ms
     95%   182.98ms
     99%   246.14ms
  HTTP codes:
    1xx - 0, 2xx - 114659, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.70MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2057.09     183.61    2417.61
  Latency       97.15ms    25.80ms   459.52ms
  Latency Distribution
     50%    95.69ms
     75%    98.63ms
     90%   106.43ms
     95%   181.73ms
     99%   195.85ms
  HTTP codes:
    1xx - 0, 2xx - 123603, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   449.99KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1031.76     174.29    1566.31
  Latency      193.51ms    65.55ms      0.90s
  Latency Distribution
     50%   187.66ms
     75%   206.28ms
     90%   223.53ms
     95%   358.35ms
     99%   394.82ms
  HTTP codes:
    1xx - 0, 2xx - 62076, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    54.89MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1756.56     149.30    2052.89
  Latency      113.76ms    43.01ms   655.02ms
  Latency Distribution
     50%   112.35ms
     75%   115.72ms
     90%   213.36ms
     95%   218.20ms
     99%   319.00ms
  HTTP codes:
    1xx - 0, 2xx - 105571, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.20MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       863.29     140.19    1232.23
  Latency      231.21ms    92.13ms      1.23s
  Latency Distribution
     50%   227.54ms
     75%   241.84ms
     90%   279.70ms
     95%   433.88ms
     99%   486.42ms
  HTTP codes:
    1xx - 0, 2xx - 51971, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    13.37MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       791.81     146.79    1442.73
  Latency      251.98ms   105.33ms      1.02s
  Latency Distribution
     50%   247.12ms
     75%   286.04ms
     90%   373.52ms
     95%   472.75ms
     99%   594.46ms
  HTTP codes:
    1xx - 0, 2xx - 47679, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   568.35KB/s
```

# Tortoise ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2388.36     342.54    3042.44
  Latency       83.70ms    35.35ms   763.57ms
  Latency Distribution
     50%    80.65ms
     75%    85.92ms
     90%   144.02ms
     95%   153.02ms
     99%   218.93ms
  HTTP codes:
    1xx - 0, 2xx - 143447, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.38MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2160.18     335.52    3763.51
  Latency       92.52ms    39.79ms   599.22ms
  Latency Distribution
     50%    90.03ms
     75%    98.38ms
     90%   159.51ms
     95%   176.31ms
     99%   253.41ms
  HTTP codes:
    1xx - 0, 2xx - 129740, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   472.65KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       957.01     155.91    1580.83
  Latency      208.57ms    97.27ms      1.09s
  Latency Distribution
     50%   205.00ms
     75%   223.17ms
     90%   376.12ms
     95%   394.44ms
     99%   558.20ms
  HTTP codes:
    1xx - 0, 2xx - 57595, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    50.93MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1549.53     348.48    2554.32
  Latency      128.96ms    59.62ms   770.05ms
  Latency Distribution
     50%   123.81ms
     75%   140.58ms
     90%   223.56ms
     95%   246.80ms
     99%   349.15ms
  HTTP codes:
    1xx - 0, 2xx - 93109, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.94MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       315.10      94.08     644.19
  Latency      630.55ms   213.11ms      2.70s
  Latency Distribution
     50%   599.95ms
     75%   714.25ms
     90%      0.86s
     95%      0.96s
     99%      1.22s
  HTTP codes:
    1xx - 0, 2xx - 19103, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.85MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       498.73     187.51    1360.55
  Latency      399.27ms   135.77ms      1.36s
  Latency Distribution
     50%   384.47ms
     75%   486.40ms
     90%   575.68ms
     95%   638.73ms
     99%   793.16ms
  HTTP codes:
    1xx - 0, 2xx - 30109, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   347.89KB/s
```

# SQLAlchemy ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       663.08     147.29    1033.70
  Latency      300.87ms   223.03ms      2.81s
  Latency Distribution
     50%   299.60ms
     75%   539.05ms
     90%   575.07ms
     95%   804.15ms
     99%      1.09s
  HTTP codes:
    1xx - 0, 2xx - 39963, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     0.94MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1195.98     194.00    1924.55
  Latency      166.97ms    91.05ms      1.05s
  Latency Distribution
     50%   162.26ms
     75%   174.21ms
     90%   310.27ms
     95%   341.84ms
     99%   494.60ms
  HTTP codes:
    1xx - 0, 2xx - 71926, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   261.81KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       183.66      51.00     314.70
  Latency         1.08s   816.22ms      9.09s
  Latency Distribution
     50%      1.02s
     75%      1.08s
     90%      1.95s
     95%      3.08s
     99%      3.32s
  HTTP codes:
    1xx - 0, 2xx - 11215, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     9.78MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1049.89     138.87    1563.16
  Latency      190.20ms    78.16ms      1.07s
  Latency Distribution
     50%   185.68ms
     75%   190.20ms
     90%   245.18ms
     95%   357.35ms
     99%   519.64ms
  HTTP codes:
    1xx - 0, 2xx - 63156, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.32MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       120.86      54.78     312.39
  Latency         1.63s      1.85s     10.02s
  Latency Distribution
     50%      1.56s
     75%      1.78s
     90%      3.79s
     95%      5.67s
     99%      7.90s
  HTTP codes:
    1xx - 0, 2xx - 7416, 3xx - 0, 4xx - 0, 5xx - 0
    others - 30
  Errors:
       timeout - 30
  Throughput:     1.95MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       368.93      99.73     780.72
  Latency      539.34ms   375.71ms      4.61s
  Latency Distribution
     50%   523.76ms
     75%   569.29ms
     90%      1.02s
     95%      1.18s
     99%      1.77s
  HTTP codes:
    1xx - 0, 2xx - 22326, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   271.59KB/s
```

# Asyncpg

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2172.33     186.68    2597.93
  Latency       92.01ms    17.11ms   353.56ms
  Latency Distribution
     50%    90.56ms
     75%    93.21ms
     90%    97.60ms
     95%   103.00ms
     99%   178.97ms
  HTTP codes:
    1xx - 0, 2xx - 130515, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.07MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2174.23     212.97    2621.96
  Latency       91.93ms    18.59ms   432.81ms
  Latency Distribution
     50%    90.29ms
     75%    93.07ms
     90%    97.45ms
     95%   103.41ms
     99%   179.78ms
  HTTP codes:
    1xx - 0, 2xx - 130629, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   475.54KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1152.64     222.15    1583.35
  Latency      173.27ms    60.01ms      0.86s
  Latency Distribution
     50%   170.56ms
     75%   180.61ms
     90%   200.06ms
     95%   320.41ms
     99%   360.10ms
  HTTP codes:
    1xx - 0, 2xx - 69329, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    61.30MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2151.55     185.36    2552.12
  Latency       92.90ms    16.83ms   378.29ms
  Latency Distribution
     50%    91.54ms
     75%    93.97ms
     90%    98.58ms
     95%   103.83ms
     99%   180.90ms
  HTTP codes:
    1xx - 0, 2xx - 129270, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.69MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1393.68     266.52    1935.67
  Latency      143.34ms    34.88ms   564.35ms
  Latency Distribution
     50%   140.53ms
     75%   151.25ms
     90%   164.37ms
     95%   180.22ms
     99%   285.45ms
  HTTP codes:
    1xx - 0, 2xx - 83795, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    23.13MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2063.91     205.98    2442.21
  Latency       96.85ms    19.59ms   469.10ms
  Latency Distribution
     50%    94.90ms
     75%    98.59ms
     90%   104.65ms
     95%   115.41ms
     99%   189.38ms
  HTTP codes:
    1xx - 0, 2xx - 124012, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.50MB/s
```

# PSQLPy

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1222.05     197.36    2115.57
  Latency      163.44ms    12.66ms   250.62ms
  Latency Distribution
     50%   165.21ms
     75%   173.04ms
     90%   178.93ms
     95%   182.44ms
     99%   189.60ms
  HTTP codes:
    1xx - 0, 2xx - 73499, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.73MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2153.40     481.51    3082.86
  Latency       92.83ms    10.95ms   178.03ms
  Latency Distribution
     50%    91.38ms
     75%   103.34ms
     90%   112.85ms
     95%   118.31ms
     99%   129.15ms
  HTTP codes:
    1xx - 0, 2xx - 129362, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   470.95KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       564.30      98.95    1053.07
  Latency      353.26ms    24.29ms   528.99ms
  Latency Distribution
     50%   355.05ms
     75%   366.68ms
     90%   375.71ms
     95%   381.90ms
     99%   395.87ms
  HTTP codes:
    1xx - 0, 2xx - 34053, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    30.02MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2089.67     433.38    2851.02
  Latency       95.64ms    10.55ms   192.67ms
  Latency Distribution
     50%    93.56ms
     75%   104.67ms
     90%   115.05ms
     95%   120.70ms
     99%   134.42ms
  HTTP codes:
    1xx - 0, 2xx - 125576, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.61MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       881.70     195.72    1401.59
  Latency      226.48ms    26.20ms   308.13ms
  Latency Distribution
     50%   226.45ms
     75%   246.14ms
     90%   264.92ms
     95%   273.26ms
     99%   286.67ms
  HTTP codes:
    1xx - 0, 2xx - 53086, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    14.63MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2009.72     449.48    2868.10
  Latency       99.46ms    11.78ms   186.03ms
  Latency Distribution
     50%    97.25ms
     75%   110.52ms
     90%   121.73ms
     95%   128.38ms
     99%   138.78ms
  HTTP codes:
    1xx - 0, 2xx - 120739, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.46MB/s
```

# Psycopg

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1474.46     131.62    1720.05
  Latency      135.50ms     6.09ms   254.36ms
  Latency Distribution
     50%   132.81ms
     75%   138.92ms
     90%   145.63ms
     95%   149.67ms
     99%   159.26ms
  HTTP codes:
    1xx - 0, 2xx - 88648, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.09MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1487.82     125.02    1746.93
  Latency      134.30ms     5.39ms   172.68ms
  Latency Distribution
     50%   131.36ms
     75%   136.97ms
     90%   143.95ms
     95%   148.27ms
     99%   156.99ms
  HTTP codes:
    1xx - 0, 2xx - 89452, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   325.39KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       870.73     102.81    1060.47
  Latency      229.23ms    10.56ms   287.20ms
  Latency Distribution
     50%   227.15ms
     75%   233.43ms
     90%   246.50ms
     95%   251.20ms
     99%   258.11ms
  HTTP codes:
    1xx - 0, 2xx - 52431, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    46.31MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1391.93     160.31    1671.84
  Latency      143.54ms     9.89ms   224.42ms
  Latency Distribution
     50%   141.60ms
     75%   148.95ms
     90%   156.60ms
     95%   161.63ms
     99%   187.99ms
  HTTP codes:
    1xx - 0, 2xx - 83692, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.74MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1031.97     148.55    1332.76
  Latency      193.49ms    16.48ms   285.46ms
  Latency Distribution
     50%   189.88ms
     75%   202.48ms
     90%   216.59ms
     95%   228.63ms
     99%   254.13ms
  HTTP codes:
    1xx - 0, 2xx - 62103, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    17.13MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1420.13     111.75    1575.82
  Latency      140.70ms     4.51ms   214.26ms
  Latency Distribution
     50%   138.97ms
     75%   143.02ms
     90%   147.19ms
     95%   150.33ms
     99%   158.83ms
  HTTP codes:
    1xx - 0, 2xx - 85378, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.03MB/s
```

# Django ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       298.52     157.10     947.01
  Latency      665.39ms    77.27ms      0.98s
  Latency Distribution
     50%   648.91ms
     75%   713.05ms
     90%   744.00ms
     95%   782.27ms
     99%      0.94s
  HTTP codes:
    1xx - 0, 2xx - 18108, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   501.78KB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       352.81     146.19    1032.87
  Latency      563.02ms    80.26ms      0.86s
  Latency Distribution
     50%   541.13ms
     75%   606.96ms
     90%   684.15ms
     95%   725.38ms
     99%   794.64ms
  HTTP codes:
    1xx - 0, 2xx - 21365, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    90.36KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       112.97     109.17     518.59
  Latency         1.74s   305.51ms      5.77s
  Latency Distribution
     50%      1.73s
     75%      1.82s
     90%      1.90s
     95%      1.94s
     99%      3.72s
  HTTP codes:
    1xx - 0, 2xx - 6968, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     6.52MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       303.86     161.74    1001.94
  Latency      652.96ms   121.65ms      0.98s
  Latency Distribution
     50%   658.07ms
     75%   715.28ms
     90%   809.93ms
     95%   845.91ms
     99%      0.93s
  HTTP codes:
    1xx - 0, 2xx - 18431, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   427.33KB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        18.62     186.50    4700.67
  Latency         9.27s      2.44s     10.02s
  Latency Distribution
     50%     10.01s
     75%     10.02s
     90%     10.02s
     95%     10.02s
     99%     10.02s
  HTTP codes:
    1xx - 0, 2xx - 110, 3xx - 0, 4xx - 0, 5xx - 0
    others - 1200
  Errors:
       timeout - 1200
  Throughput:    36.49KB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        16.86     332.00   10051.22
  Latency        10.72s      1.16s     15.13s
  Latency Distribution
     50%     10.02s
     75%     11.07s
     90%     13.13s
     95%     13.13s
     99%     13.13s
  HTTP codes:
    1xx - 0, 2xx - 0, 3xx - 0, 4xx - 0, 5xx - 0
    others - 1200
  Errors:
       timeout - 1200
  Throughput:     6.79KB/s
```

# Oxyde ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1710.87     385.65    3411.65
  Latency      116.77ms     9.10ms   196.95ms
  Latency Distribution
     50%   115.99ms
     75%   123.65ms
     90%   131.74ms
     95%   136.82ms
     99%   146.68ms
  HTTP codes:
    1xx - 0, 2xx - 102831, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.42MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1761.59     348.61    2975.03
  Latency      113.44ms     7.89ms   194.42ms
  Latency Distribution
     50%   112.84ms
     75%   119.24ms
     90%   125.33ms
     95%   129.93ms
     99%   142.39ms
  HTTP codes:
    1xx - 0, 2xx - 105858, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   385.39KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       848.17     261.24    1508.32
  Latency      235.28ms    27.04ms   408.44ms
  Latency Distribution
     50%   230.94ms
     75%   251.44ms
     90%   273.01ms
     95%   287.96ms
     99%   320.94ms
  HTTP codes:
    1xx - 0, 2xx - 51099, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    45.48MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1697.25     402.85    3177.34
  Latency      117.70ms    10.46ms   196.62ms
  Latency Distribution
     50%   116.47ms
     75%   125.08ms
     90%   134.47ms
     95%   140.89ms
     99%   153.46ms
  HTTP codes:
    1xx - 0, 2xx - 102034, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.14MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       402.11     236.07    1808.59
  Latency      495.10ms    37.33ms   637.42ms
  Latency Distribution
     50%   495.78ms
     75%   518.53ms
     90%   540.11ms
     95%   554.85ms
     99%   583.74ms
  HTTP codes:
    1xx - 0, 2xx - 24314, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     6.66MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       446.66     356.69    2145.18
  Latency      445.64ms    20.26ms   554.42ms
  Latency Distribution
     50%   444.87ms
     75%   456.43ms
     90%   467.81ms
     95%   478.92ms
     99%   498.92ms
  HTTP codes:
    1xx - 0, 2xx - 26993, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   321.16KB/s
```
