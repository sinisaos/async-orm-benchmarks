# Piccolo ORM + FastAPI (4 workers)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4728.56    1351.63    9548.69
  Latency      105.64ms    84.04ms      2.05s
  Latency Distribution
     50%    69.91ms
     75%   105.80ms
     90%   218.13ms
     95%   284.97ms
     99%   525.01ms
  HTTP codes:
    1xx - 0, 2xx - 284222, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     6.69MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4519.31    1602.44    9359.85
  Latency      110.51ms    74.78ms      1.46s
  Latency Distribution
     50%    81.14ms
     75%   116.56ms
     90%   212.98ms
     95%   274.17ms
     99%   456.90ms
  HTTP codes:
    1xx - 0, 2xx - 271630, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     0.97MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2085.22     461.13    3664.96
  Latency      239.18ms   219.84ms      3.77s
  Latency Distribution
     50%   152.04ms
     75%   269.02ms
     90%   504.01ms
     95%   677.11ms
     99%      1.18s
  HTTP codes:
    1xx - 0, 2xx - 125600, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   110.93MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3642.82    1416.36    8894.20
  Latency      137.07ms    98.80ms      1.72s
  Latency Distribution
     50%    96.96ms
     75%   150.03ms
     90%   267.02ms
     95%   345.48ms
     99%   575.99ms
  HTTP codes:
    1xx - 0, 2xx - 219020, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.56MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1513.05     622.68    3532.87
  Latency      329.59ms   294.60ms      4.00s
  Latency Distribution
     50%   181.94ms
     75%   478.98ms
     90%   729.03ms
     95%      0.95s
     99%      1.46s
  HTTP codes:
    1xx - 0, 2xx - 91225, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    23.20MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1883.76     808.52    4836.40
  Latency      264.41ms   205.43ms      2.25s
  Latency Distribution
     50%   191.02ms
     75%   331.97ms
     90%   542.97ms
     95%   708.00ms
     99%      1.10s
  HTTP codes:
    1xx - 0, 2xx - 113611, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.58MB/s
```

# Tortoise ORM + FastAPI (4 workers)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3783.28    1251.70    8169.24
  Latency      131.95ms    98.26ms      2.03s
  Latency Distribution
     50%    93.98ms
     75%   159.13ms
     90%   243.32ms
     95%   326.15ms
     99%   560.86ms
  HTTP codes:
    1xx - 0, 2xx - 227513, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     5.36MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3479.23    1588.21    9633.55
  Latency      143.50ms    91.98ms      1.87s
  Latency Distribution
     50%   112.07ms
     75%   170.11ms
     90%   258.95ms
     95%   339.94ms
     99%   560.00ms
  HTTP codes:
    1xx - 0, 2xx - 209239, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   761.54KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1697.05     433.03    3190.09
  Latency      293.87ms   237.00ms      3.44s
  Latency Distribution
     50%   201.12ms
     75%   375.97ms
     90%   580.95ms
     95%   802.06ms
     99%      1.28s
  HTTP codes:
    1xx - 0, 2xx - 102295, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    90.22MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2817.04    1307.01    8046.65
  Latency      176.98ms   131.56ms      2.00s
  Latency Distribution
     50%   124.88ms
     75%   206.00ms
     90%   355.09ms
     95%   444.01ms
     99%   744.93ms
  HTTP codes:
    1xx - 0, 2xx - 169699, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.53MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       617.28     196.12    1251.08
  Latency      803.59ms   438.11ms      5.74s
  Latency Distribution
     50%   737.98ms
     75%      0.99s
     90%      1.31s
     95%      1.57s
     99%      2.57s
  HTTP codes:
    1xx - 0, 2xx - 37514, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     9.40MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       761.02     252.48    1793.42
  Latency      652.94ms   365.68ms      4.42s
  Latency Distribution
     50%   584.04ms
     75%   833.06ms
     90%      1.12s
     95%      1.34s
     99%      1.82s
  HTTP codes:
    1xx - 0, 2xx - 46100, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   641.52KB/s
```

# Drizzle ORM + Hono (4 workers)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      8989.54    2613.64   16281.45
  Latency       55.60ms    26.90ms      1.40s
  Latency Distribution
     50%    51.90ms
     75%    64.40ms
     90%    78.04ms
     95%    87.64ms
     99%   109.56ms
  HTTP codes:
    1xx - 0, 2xx - 539619, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    12.97MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      9376.93    2771.32   16013.49
  Latency       53.31ms    16.98ms   722.98ms
  Latency Distribution
     50%    49.34ms
     75%    63.55ms
     90%    79.17ms
     95%    90.02ms
     99%   111.53ms
  HTTP codes:
    1xx - 0, 2xx - 562813, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.27MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1712.78     446.32    3248.45
  Latency      291.23ms   100.36ms      3.07s
  Latency Distribution
     50%   287.78ms
     75%   317.59ms
     90%   346.84ms
     95%   365.15ms
     99%   411.95ms
  HTTP codes:
    1xx - 0, 2xx - 103223, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    87.69MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4884.30    1136.79    9490.20
  Latency      102.32ms    26.97ms      1.01s
  Latency Distribution
     50%    99.98ms
     75%   115.51ms
     90%   132.16ms
     95%   142.85ms
     99%   166.37ms
  HTTP codes:
    1xx - 0, 2xx - 293261, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     6.05MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1541.07     514.50    3410.06
  Latency      323.98ms    88.11ms      2.50s
  Latency Distribution
     50%   322.82ms
     75%   361.17ms
     90%   393.95ms
     95%   412.53ms
     99%   458.77ms
  HTTP codes:
    1xx - 0, 2xx - 92802, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    26.03MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1958.38     698.49    5056.05
  Latency      254.85ms    76.93ms      1.93s
  Latency Distribution
     50%   259.28ms
     75%   291.88ms
     90%   317.29ms
     95%   332.04ms
     99%   360.83ms
  HTTP codes:
    1xx - 0, 2xx - 117805, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.72MB/s
```

# Ent ORM + Chi

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     36973.73    7390.47   66432.20
  Latency       13.51ms     6.23ms   296.69ms
  Latency Distribution
     50%    10.29ms
     75%    17.80ms
     90%    28.14ms
     95%    36.38ms
     99%    56.02ms
  HTTP codes:
    1xx - 0, 2xx - 2218867, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    71.16MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     58198.57   11166.31   90117.26
  Latency        8.59ms     3.29ms   195.74ms
  Latency Distribution
     50%     6.42ms
     75%    11.48ms
     90%    18.16ms
     95%    23.24ms
     99%    35.56ms
  HTTP codes:
    1xx - 0, 2xx - 3489217, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    12.14MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      6749.00    1135.39   11329.75
  Latency       74.10ms    59.51ms      0.98s
  Latency Distribution
     50%    52.62ms
     75%   100.27ms
     90%   163.78ms
     95%   212.72ms
     99%   329.51ms
  HTTP codes:
    1xx - 0, 2xx - 405022, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   317.93MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     36543.88    6272.94   63886.95
  Latency       13.68ms     6.05ms   192.55ms
  Latency Distribution
     50%    10.35ms
     75%    18.11ms
     90%    28.72ms
     95%    36.94ms
     99%    56.59ms
  HTTP codes:
    1xx - 0, 2xx - 2191418, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    40.68MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      9528.57    1435.94   13851.01
  Latency       52.51ms    20.35ms   330.75ms
  Latency Distribution
     50%    46.97ms
     75%    67.53ms
     90%    91.14ms
     95%   107.83ms
     99%   144.68ms
  HTTP codes:
    1xx - 0, 2xx - 571302, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   181.94MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     17336.98    2884.19   25260.73
  Latency       28.84ms     7.56ms   163.90ms
  Latency Distribution
     50%    26.32ms
     75%    36.31ms
     90%    47.74ms
     95%    55.75ms
     99%    73.65ms
  HTTP codes:
    1xx - 0, 2xx - 1040138, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    15.91MB/s
```

# SQLC + Chi

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     58863.28    7815.16   90706.79
  Latency        8.49ms     2.92ms   133.66ms
  Latency Distribution
     50%     6.53ms
     75%    11.43ms
     90%    17.53ms
     95%    22.39ms
     99%    33.86ms
  HTTP codes:
    1xx - 0, 2xx - 3529719, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    82.35MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     73621.36    9598.33   98322.32
  Latency        6.79ms     2.07ms   111.22ms
  Latency Distribution
     50%     5.11ms
     75%     9.11ms
     90%    14.39ms
     95%    18.38ms
     99%    27.71ms
  HTTP codes:
    1xx - 0, 2xx - 4416102, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    14.60MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      8720.44    1313.72   12415.15
  Latency       57.34ms    43.82ms   756.10ms
  Latency Distribution
     50%    40.85ms
     75%    77.38ms
     90%   126.62ms
     95%   163.92ms
     99%   253.69ms
  HTTP codes:
    1xx - 0, 2xx - 523279, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   443.29MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     50496.54    8859.64   75523.30
  Latency        9.90ms     3.81ms   165.39ms
  Latency Distribution
     50%     7.41ms
     75%    13.26ms
     90%    20.82ms
     95%    26.68ms
     99%    41.01ms
  HTTP codes:
    1xx - 0, 2xx - 3029099, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    60.03MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      7440.33    1301.94   10278.24
  Latency       67.19ms    55.06ms      1.13s
  Latency Distribution
     50%    47.00ms
     75%    90.94ms
     90%   150.63ms
     95%   196.63ms
     99%   306.75ms
  HTTP codes:
    1xx - 0, 2xx - 446577, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   129.95MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 500 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec     28523.61    4105.59   40083.09
  Latency       17.53ms     9.60ms   289.39ms
  Latency Distribution
     50%    12.41ms
     75%    23.79ms
     90%    39.00ms
     95%    50.58ms
     99%    78.00ms
  HTTP codes:
    1xx - 0, 2xx - 1710820, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    24.55MB/s
```
