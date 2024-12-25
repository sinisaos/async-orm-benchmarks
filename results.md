# Piccolo ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       742.92     145.32    1295.95
  Latency      264.89ms    31.99ms   613.22ms
  Latency Distribution
     50%   254.06ms
     75%   275.26ms
     90%   295.41ms
     95%   342.96ms
     99%   369.54ms
  HTTP codes:
    1xx - 0, 2xx - 7600, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.06MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       762.99     183.76    1307.53
  Latency      257.95ms    24.22ms   561.17ms
  Latency Distribution
     50%   255.50ms
     75%   267.18ms
     90%   282.35ms
     95%   288.85ms
     99%   318.02ms
  HTTP codes:
    1xx - 0, 2xx - 7808, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   168.32KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       308.44     118.42     524.97
  Latency      622.33ms   100.43ms   832.93ms
  Latency Distribution
     50%   627.31ms
     75%   694.24ms
     90%   735.60ms
     95%   760.51ms
     99%   820.19ms
  HTTP codes:
    1xx - 0, 2xx - 3279, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    16.77MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       564.74     143.88    1213.15
  Latency      345.81ms    37.95ms   623.24ms
  Latency Distribution
     50%   338.49ms
     75%   367.00ms
     90%   379.41ms
     95%   390.39ms
     99%   500.22ms
  HTTP codes:
    1xx - 0, 2xx - 5830, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   734.37KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       258.74     148.33     527.11
  Latency      734.14ms    79.98ms      1.15s
  Latency Distribution
     50%   739.79ms
     75%   772.68ms
     90%   785.89ms
     95%   792.30ms
     99%      0.95s
  HTTP codes:
    1xx - 0, 2xx - 2781, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.11MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       244.48      92.72     591.71
  Latency      772.06ms   287.81ms      3.22s
  Latency Distribution
     50%   756.69ms
     75%      0.88s
     90%      1.16s
     95%      1.28s
     99%      1.64s
  HTTP codes:
    1xx - 0, 2xx - 2637, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   184.12KB/s
```
# Tortoise ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       579.70     142.57    1192.13
  Latency      337.09ms    75.25ms      0.96s
  Latency Distribution
     50%   329.12ms
     75%   353.80ms
     90%   441.42ms
     95%   481.19ms
     99%   577.80ms
  HTTP codes:
    1xx - 0, 2xx - 5977, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   852.43KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       666.87      83.63    1280.31
  Latency      294.28ms    24.72ms   615.79ms
  Latency Distribution
     50%   293.41ms
     75%   299.57ms
     90%   310.86ms
     95%   316.19ms
     99%   369.34ms
  HTTP codes:
    1xx - 0, 2xx - 6846, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   147.47KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       295.86      59.74     465.37
  Latency      647.37ms    64.77ms      0.86s
  Latency Distribution
     50%   654.22ms
     75%   673.18ms
     90%   700.46ms
     95%   712.68ms
     99%   776.87ms
  HTTP codes:
    1xx - 0, 2xx - 3155, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    16.09MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       425.93      96.52    1075.37
  Latency      454.46ms    76.14ms      1.00s
  Latency Distribution
     50%   456.07ms
     75%   497.36ms
     90%   525.68ms
     95%   537.87ms
     99%   671.40ms
  HTTP codes:
    1xx - 0, 2xx - 4438, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   557.97KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        37.90      46.04     207.28
  Latency         4.25s      3.53s     10.01s
  Latency Distribution
     50%      1.94s
     75%      8.50s
     90%     10.00s
     95%     10.01s
     99%     10.01s
  HTTP codes:
    1xx - 0, 2xx - 515, 3xx - 0, 4xx - 0, 5xx - 0
    others - 63
  Errors:
       timeout - 63
  Throughput:   595.64KB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       117.00      66.58     407.29
  Latency         1.53s   793.26ms      6.65s
  Latency Distribution
     50%      1.38s
     75%      1.77s
     90%      2.37s
     95%      3.42s
     99%      4.30s
  HTTP codes:
    1xx - 0, 2xx - 1369, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    87.24KB/s
```
# SqlAlchemy ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       229.81     255.91     939.29
  Latency      827.08ms   281.59ms      2.79s
  Latency Distribution
     50%   750.47ms
     75%   787.09ms
     90%   835.64ms
     95%      1.57s
     99%      1.94s
  HTTP codes:
    1xx - 0, 2xx - 2493, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   341.21KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       407.82     275.21     955.48
  Latency      475.78ms   134.95ms      1.28s
  Latency Distribution
     50%   436.52ms
     75%   482.81ms
     90%   497.37ms
     95%   534.66ms
     99%      1.16s
  HTTP codes:
    1xx - 0, 2xx - 4257, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    90.79KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        10.48      60.40     650.50
  Latency         7.16s      3.87s     10.02s
  Latency Distribution
     50%     10.00s
     75%     10.01s
     90%     10.02s
     95%     10.02s
     99%     10.02s
  HTTP codes:
    1xx - 0, 2xx - 113, 3xx - 0, 4xx - 0, 5xx - 0
    others - 191
  Errors:
       timeout - 191
  Throughput:   371.42KB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       361.74     273.91     973.46
  Latency      532.53ms   154.82ms      1.41s
  Latency Distribution
     50%   482.49ms
     75%   532.81ms
     90%   650.65ms
     95%   791.26ms
     99%      1.32s
  HTTP codes:
    1xx - 0, 2xx - 3815, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   474.51KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec         7.19      41.20     468.81
  Latency         7.81s      3.60s     10.02s
  Latency Distribution
     50%     10.00s
     75%     10.01s
     90%     10.01s
     95%     10.01s
     99%     10.02s
  HTTP codes:
    1xx - 0, 2xx - 78, 3xx - 0, 4xx - 0, 5xx - 0
    others - 193
  Errors:
       timeout - 193
  Throughput:    80.18KB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       113.86     129.64     519.85
  Latency         1.60s   392.48ms      3.61s
  Latency Distribution
     50%      1.50s
     75%      1.73s
     90%      1.82s
     95%      1.86s
     99%      3.54s
  HTTP codes:
    1xx - 0, 2xx - 1338, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    83.84KB/s
```
# Asyncpg
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       838.88     204.85    1376.75
  Latency      235.01ms    54.71ms   780.39ms
  Latency Distribution
     50%   210.28ms
     75%   251.76ms
     90%   305.24ms
     95%   359.74ms
     99%   388.23ms
  HTTP codes:
    1xx - 0, 2xx - 8564, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.19MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       950.76     157.47    1392.81
  Latency      207.75ms    29.50ms   573.79ms
  Latency Distribution
     50%   200.12ms
     75%   209.42ms
     90%   228.55ms
     95%   286.73ms
     99%   322.67ms
  HTTP codes:
    1xx - 0, 2xx - 9690, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   209.05KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       361.71     145.51     525.06
  Latency      537.75ms    67.04ms      1.22s
  Latency Distribution
     50%   534.66ms
     75%   556.39ms
     90%   593.41ms
     95%   642.67ms
     99%   727.46ms
  HTTP codes:
    1xx - 0, 2xx - 3810, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    19.35MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       856.60     163.34    1443.19
  Latency      230.32ms    29.54ms   382.07ms
  Latency Distribution
     50%   223.35ms
     75%   230.70ms
     90%   252.95ms
     95%   290.24ms
     99%   375.10ms
  HTTP codes:
    1xx - 0, 2xx - 8740, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.08MB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       492.51     100.19     804.24
  Latency      396.78ms    65.49ms      1.12s
  Latency Distribution
     50%   379.74ms
     75%   394.16ms
     90%   435.00ms
     95%   538.16ms
     99%   669.73ms
  HTTP codes:
    1xx - 0, 2xx - 5113, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.21MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       788.93     130.04    1035.87
  Latency      250.37ms    42.98ms      0.92s
  Latency Distribution
     50%   235.17ms
     75%   268.44ms
     90%   284.85ms
     95%   332.62ms
     99%   372.77ms
  HTTP codes:
    1xx - 0, 2xx - 8075, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   591.40KB/s
```
# PSQLPy
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec      1003.55     164.36    1570.91
  Latency      197.22ms    20.12ms   362.35ms
  Latency Distribution
     50%   190.88ms
     75%   197.53ms
     90%   223.59ms
     95%   231.26ms
     99%   267.19ms
  HTTP codes:
    1xx - 0, 2xx - 10204, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.43MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       926.14     209.27    1556.24
  Latency      213.03ms    33.19ms   350.26ms
  Latency Distribution
     50%   196.95ms
     75%   237.37ms
     90%   252.39ms
     95%   269.46ms
     99%   339.05ms
  HTTP codes:
    1xx - 0, 2xx - 9444, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   204.12KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       350.91      77.31     509.91
  Latency      551.81ms   110.39ms      0.91s
  Latency Distribution
     50%   521.83ms
     75%   538.73ms
     90%   711.37ms
     95%   809.20ms
     99%      0.90s
  HTTP codes:
    1xx - 0, 2xx - 3702, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    18.87MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       938.27     146.32    1564.17
  Latency      210.30ms    25.33ms   365.10ms
  Latency Distribution
     50%   203.95ms
     75%   207.94ms
     90%   228.96ms
     95%   278.04ms
     99%   320.06ms
  HTTP codes:
    1xx - 0, 2xx - 9565, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.18MB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       494.49      88.35     677.75
  Latency      397.64ms    51.53ms   593.72ms
  Latency Distribution
     50%   382.08ms
     75%   400.54ms
     90%   464.88ms
     95%   500.81ms
     99%   585.15ms
  HTTP codes:
    1xx - 0, 2xx - 5139, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.15MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       794.26     185.43    1422.81
  Latency      248.11ms    46.15ms   432.43ms
  Latency Distribution
     50%   224.59ms
     75%   270.53ms
     90%   290.61ms
     95%   354.94ms
     99%   412.60ms
  HTTP codes:
    1xx - 0, 2xx - 8106, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   598.16KB/s
```
# Psycopg
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       581.59     156.12     944.81
  Latency      336.66ms    60.79ms   573.16ms
  Latency Distribution
     50%   318.58ms
     75%   363.84ms
     90%   411.21ms
     95%   478.86ms
     99%   549.72ms
  HTTP codes:
    1xx - 0, 2xx - 6000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   851.94KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       662.98     173.64    1027.95
  Latency      297.32ms    32.28ms   439.46ms
  Latency Distribution
     50%   288.98ms
     75%   309.29ms
     90%   331.92ms
     95%   381.97ms
     99%   398.41ms
  HTTP codes:
    1xx - 0, 2xx - 6811, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   145.16KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       236.43     157.50     520.26
  Latency      806.40ms   134.15ms      1.24s
  Latency Distribution
     50%   774.68ms
     75%      0.86s
     90%      0.96s
     95%      1.08s
     99%      1.15s
  HTTP codes:
    1xx - 0, 2xx - 2561, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    12.77MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       640.49     162.84    1045.31
  Latency      306.63ms    23.96ms   390.88ms
  Latency Distribution
     50%   307.22ms
     75%   317.84ms
     90%   330.14ms
     95%   338.32ms
     99%   360.58ms
  HTTP codes:
    1xx - 0, 2xx - 6590, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   826.04KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       332.98      90.33     501.65
  Latency      580.66ms    62.85ms   694.47ms
  Latency Distribution
     50%   597.75ms
     75%   608.40ms
     90%   614.86ms
     95%   621.20ms
     99%   640.90ms
  HTTP codes:
    1xx - 0, 2xx - 3525, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     5.57MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       586.71     104.02     821.03
  Latency      334.50ms    29.87ms   489.58ms
  Latency Distribution
     50%   324.73ms
     75%   339.60ms
     90%   382.90ms
     95%   393.74ms
     99%   403.03ms
  HTTP codes:
    1xx - 0, 2xx - 6053, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   440.91KB/s
```
# Django ORM
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       115.43      72.76     259.80
  Latency         1.55s      0.87s      3.96s
  Latency Distribution
     50%      1.15s
     75%      1.44s
     90%      3.59s
     95%      3.75s
     99%      3.90s
  HTTP codes:
    1xx - 0, 2xx - 1350, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   210.23KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       232.66     168.35     601.41
  Latency      804.81ms   171.91ms      1.36s
  Latency Distribution
     50%   782.99ms
     75%      0.86s
     90%      1.04s
     95%      1.13s
     99%      1.28s
  HTTP codes:
    1xx - 0, 2xx - 2530, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    62.37KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec        10.88      32.48     203.75
  Latency         6.97s      4.18s     10.04s
  Latency Distribution
     50%     10.01s
     75%     10.03s
     90%     10.03s
     95%     10.03s
     99%     10.03s
  HTTP codes:
    1xx - 0, 2xx - 107, 3xx - 0, 4xx - 0, 5xx - 0
    others - 200
  Errors:
       timeout - 200
  Throughput:   529.40KB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       202.49     176.89     520.76
  Latency         0.92s   229.99ms      1.95s
  Latency Distribution
     50%      0.90s
     75%      0.91s
     90%      1.11s
     95%      1.50s
     99%      1.86s
  HTTP codes:
    1xx - 0, 2xx - 2220, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   298.33KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec         5.58      21.58     151.45
  Latency         8.14s      3.61s     10.03s
  Latency Distribution
     50%     10.01s
     75%     10.02s
     90%     10.02s
     95%     10.02s
     99%     10.03s
  HTTP codes:
    1xx - 0, 2xx - 54, 3xx - 0, 4xx - 0, 5xx - 0
    others - 200
  Errors:
       timeout - 200
  Throughput:    80.51KB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec         6.33     141.40    3164.85
  Latency        10.03s     9.54ms     10.06s
  Latency Distribution
     50%     10.03s
     75%     10.04s
     90%     10.05s
     95%     10.05s
     99%     10.05s
  HTTP codes:
    1xx - 0, 2xx - 0, 3xx - 0, 4xx - 0, 5xx - 0
    others - 200
  Errors:
       timeout - 200
  Throughput:     7.57KB/s
```
# Mayim
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       441.71     104.23     635.62
  Latency      440.94ms    74.50ms   775.13ms
  Latency Distribution
     50%   412.03ms
     75%   444.72ms
     90%   581.99ms
     95%   611.34ms
     99%   664.26ms
  HTTP codes:
    1xx - 0, 2xx - 4603, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   646.50KB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       593.78     127.12     862.39
  Latency      330.65ms    52.91ms   488.14ms
  Latency Distribution
     50%   304.14ms
     75%   368.98ms
     90%   406.28ms
     95%   420.05ms
     99%   482.01ms
  HTTP codes:
    1xx - 0, 2xx - 6123, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   130.46KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       136.03      52.87     344.27
  Latency         1.35s   624.12ms      3.78s
  Latency Distribution
     50%      1.17s
     75%      1.21s
     90%      1.90s
     95%      3.40s
     99%      3.55s
  HTTP codes:
    1xx - 0, 2xx - 1556, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     7.48MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       587.40      78.30     810.47
  Latency      333.84ms    24.12ms   472.59ms
  Latency Distribution
     50%   334.85ms
     75%   340.67ms
     90%   346.59ms
     95%   360.62ms
     99%   374.29ms
  HTTP codes:
    1xx - 0, 2xx - 6063, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   757.67KB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       232.98      55.01     366.11
  Latency      837.01ms   140.67ms      1.19s
  Latency Distribution
     50%   826.98ms
     75%      0.85s
     90%      0.98s
     95%      1.14s
     99%      1.17s
  HTTP codes:
    1xx - 0, 2xx - 2527, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     3.64MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       486.46     131.15     740.69
  Latency      400.68ms    87.31ms      0.88s
  Latency Distribution
     50%   356.18ms
     75%   445.95ms
     90%   502.61ms
     95%   549.90ms
     99%   713.90ms
  HTTP codes:
    1xx - 0, 2xx - 5062, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   346.00KB/s
```
