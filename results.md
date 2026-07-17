# Piccolo ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       379.02     441.88    3667.26
  Latency      524.92ms    44.96ms   713.13ms
  Latency Distribution
     50%   525.73ms
     75%   553.02ms
     90%   579.34ms
     95%   598.55ms
     99%   636.18ms
  HTTP codes:
    1xx - 0, 2xx - 22921, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   551.29KB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       742.91     504.06    3056.05
  Latency      268.62ms    29.54ms   418.82ms
  Latency Distribution
     50%   269.97ms
     75%   289.79ms
     90%   306.29ms
     95%   316.02ms
     99%   339.88ms
  HTTP codes:
    1xx - 0, 2xx - 44744, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   162.73KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       133.18     154.72    2210.79
  Latency         1.47s   157.02ms      1.94s
  Latency Distribution
     50%      1.49s
     75%      1.56s
     90%      1.64s
     95%      1.70s
     99%      1.77s
  HTTP codes:
    1xx - 0, 2xx - 8191, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     7.17MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       619.79     565.82    4246.45
  Latency      321.53ms    37.64ms   470.29ms
  Latency Distribution
     50%   323.64ms
     75%   347.35ms
     90%   369.55ms
     95%   382.99ms
     99%   407.54ms
  HTTP codes:
    1xx - 0, 2xx - 37371, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   795.71KB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       145.10     186.37    2602.71
  Latency         1.36s   124.03ms      1.69s
  Latency Distribution
     50%      1.38s
     75%      1.44s
     90%      1.48s
     95%      1.51s
     99%      1.56s
  HTTP codes:
    1xx - 0, 2xx - 8901, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.27MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       226.68     236.48    2746.88
  Latency         0.87s    61.67ms      1.03s
  Latency Distribution
     50%      0.88s
     75%      0.91s
     90%      0.95s
     95%      0.96s
     99%      0.98s
  HTTP codes:
    1xx - 0, 2xx - 13801, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   169.17KB/s
```

# Piccolo ORM(enhanced)

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3073.34     625.71    6100.80
  Latency       65.03ms     6.01ms   134.31ms
  Latency Distribution
     50%    62.68ms
     75%    66.43ms
     90%    72.53ms
     95%    81.16ms
     99%    93.60ms
  HTTP codes:
    1xx - 0, 2xx - 184563, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.35MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3525.97     776.96    8679.64
  Latency       56.70ms     7.14ms   122.50ms
  Latency Distribution
     50%    54.55ms
     75%    57.74ms
     90%    67.97ms
     95%    75.07ms
     99%    91.94ms
  HTTP codes:
    1xx - 0, 2xx - 211664, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   771.49KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1054.98     680.69    3628.60
  Latency      189.29ms    12.70ms   256.00ms
  Latency Distribution
     50%   182.64ms
     75%   201.95ms
     90%   210.67ms
     95%   216.85ms
     99%   237.53ms
  HTTP codes:
    1xx - 0, 2xx - 63431, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    56.13MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2181.84     419.91    9374.36
  Latency       91.60ms     8.97ms   160.97ms
  Latency Distribution
     50%    87.40ms
     75%    93.10ms
     90%   105.81ms
     95%   115.86ms
     99%   132.57ms
  HTTP codes:
    1xx - 0, 2xx - 131038, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.73MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       610.49     518.39    3990.51
  Latency      326.77ms    20.54ms   431.49ms
  Latency Distribution
     50%   318.50ms
     75%   338.06ms
     90%   355.76ms
     95%   374.13ms
     99%   397.19ms
  HTTP codes:
    1xx - 0, 2xx - 36800, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     9.47MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       926.55     484.44    6355.69
  Latency      215.34ms    17.26ms   346.93ms
  Latency Distribution
     50%   209.34ms
     75%   221.99ms
     90%   237.55ms
     95%   251.00ms
     99%   281.73ms
  HTTP codes:
    1xx - 0, 2xx - 55780, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   687.27KB/s
```

# Tortoise ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3089.82     373.20    6489.14
  Latency       64.70ms     6.27ms   159.10ms
  Latency Distribution
     50%    61.42ms
     75%    66.76ms
     90%    70.90ms
     95%    79.95ms
     99%    97.45ms
  HTTP codes:
    1xx - 0, 2xx - 185502, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.37MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2720.01     445.55    6990.40
  Latency       73.48ms     7.97ms   139.80ms
  Latency Distribution
     50%    68.58ms
     75%    73.81ms
     90%    95.45ms
     95%   103.18ms
     99%   107.67ms
  HTTP codes:
    1xx - 0, 2xx - 163311, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   595.23KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       769.11     245.20    1122.95
  Latency      259.29ms    65.07ms   447.08ms
  Latency Distribution
     50%   225.63ms
     75%   318.47ms
     90%   372.42ms
     95%   398.51ms
     99%   422.54ms
  HTTP codes:
    1xx - 0, 2xx - 46345, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    40.93MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1917.27     249.79    4369.39
  Latency      104.21ms    10.08ms   176.91ms
  Latency Distribution
     50%    99.79ms
     75%   104.54ms
     90%   116.31ms
     95%   130.88ms
     99%   152.74ms
  HTTP codes:
    1xx - 0, 2xx - 115183, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.40MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       302.64     244.47     830.24
  Latency      657.87ms   101.37ms      1.02s
  Latency Distribution
     50%   641.32ms
     75%   711.79ms
     90%   801.58ms
     95%      0.86s
     99%      0.96s
  HTTP codes:
    1xx - 0, 2xx - 18363, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.65MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       647.15     699.10    2439.87
  Latency      308.43ms    53.83ms   507.02ms
  Latency Distribution
     50%   298.35ms
     75%   347.41ms
     90%   386.39ms
     95%   408.99ms
     99%   479.55ms
  HTTP codes:
    1xx - 0, 2xx - 39000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   465.92KB/s
```

# Oxyde ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2531.44    1289.74    6802.02
  Latency       78.98ms    11.05ms   152.52ms
  Latency Distribution
     50%    77.02ms
     75%    86.82ms
     90%    97.36ms
     95%   105.27ms
     99%   122.32ms
  HTTP codes:
    1xx - 0, 2xx - 152017, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.58MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      3541.27    2001.72    9932.80
  Latency       56.35ms     8.29ms   115.62ms
  Latency Distribution
     50%    54.48ms
     75%    64.14ms
     90%    73.16ms
     95%    79.10ms
     99%    91.25ms
  HTTP codes:
    1xx - 0, 2xx - 213077, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   776.10KB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       744.09     212.79    1362.46
  Latency      268.32ms    44.37ms   455.35ms
  Latency Distribution
     50%   253.28ms
     75%   306.98ms
     90%   338.85ms
     95%   353.56ms
     99%   379.85ms
  HTTP codes:
    1xx - 0, 2xx - 44834, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    39.65MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      2956.91    1693.60    9102.57
  Latency       67.53ms    10.54ms   158.61ms
  Latency Distribution
     50%    65.22ms
     75%    74.67ms
     90%    85.15ms
     95%    93.26ms
     99%   112.35ms
  HTTP codes:
    1xx - 0, 2xx - 177798, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.71MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       485.49     534.07    3300.42
  Latency      410.65ms    71.56ms   654.17ms
  Latency Distribution
     50%   413.31ms
     75%   459.20ms
     90%   501.57ms
     95%   527.62ms
     99%   576.56ms
  HTTP codes:
    1xx - 0, 2xx - 29293, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.05MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1013.14    1113.88    7386.19
  Latency      196.71ms    30.74ms   341.56ms
  Latency Distribution
     50%   196.69ms
     75%   218.37ms
     90%   237.57ms
     95%   249.81ms
     99%   278.30ms
  HTTP codes:
    1xx - 0, 2xx - 61093, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   779.63KB/s
```

# Yara ORM

### Small table (50 rows)

```bash
Bombarding http://localhost:8000/small-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4456.41    1260.99    9859.49
  Latency       44.87ms     7.56ms   140.55ms
  Latency Distribution
     50%    41.52ms
     75%    45.71ms
     90%    56.72ms
     95%    62.55ms
     99%    83.90ms
  HTTP codes:
    1xx - 0, 2xx - 267486, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     6.31MB/s
```

### Small table (single row)

```bash
Bombarding http://localhost:8000/small-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4957.43    1702.67   10162.17
  Latency       40.35ms     3.91ms    99.07ms
  Latency Distribution
     50%    38.44ms
     75%    40.44ms
     90%    48.24ms
     95%    54.47ms
     99%    61.76ms
  HTTP codes:
    1xx - 0, 2xx - 297415, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.06MB/s
```

### Mega table (50 rows)

```bash
Bombarding http://localhost:8000/mega-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       872.18     888.54    5497.46
  Latency      228.53ms    36.71ms   482.91ms
  Latency Distribution
     50%   226.74ms
     75%   254.98ms
     90%   278.43ms
     95%   292.23ms
     99%   332.16ms
  HTTP codes:
    1xx - 0, 2xx - 52579, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    46.48MB/s
```

### Mega table (single row)

```bash
Bombarding http://localhost:8000/mega-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      4147.16    2111.25    9134.56
  Latency       48.23ms     4.13ms    95.92ms
  Latency Distribution
     50%    46.19ms
     75%    48.19ms
     90%    58.38ms
     95%    63.07ms
     99%    70.48ms
  HTTP codes:
    1xx - 0, 2xx - 248853, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     5.18MB/s
```

### Related table (50 rows)

```bash
Bombarding http://localhost:8000/related-table/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       484.31     151.70     773.38
  Latency      411.57ms    32.11ms   577.36ms
  Latency Distribution
     50%   412.11ms
     75%   430.83ms
     90%   449.38ms
     95%   461.99ms
     99%   489.76ms
  HTTP codes:
    1xx - 0, 2xx - 29253, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     7.44MB/s
```

### Related table (single row)

```bash
Bombarding http://localhost:8000/related-table/1/ for 1m0s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1453.55     521.70    4339.06
  Latency      137.41ms    11.95ms   249.44ms
  Latency Distribution
     50%   132.56ms
     75%   139.95ms
     90%   154.54ms
     95%   166.45ms
     99%   188.97ms
  HTTP codes:
    1xx - 0, 2xx - 87392, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.02MB/s
```
