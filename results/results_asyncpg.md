# Asyncpg
### Small table (50 rows)
```bash
Bombarding http://localhost:8000/small-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       933.73     138.84    1327.34
  Latency      211.96ms    14.70ms   398.13ms
  Latency Distribution
     50%   210.26ms
     75%   216.93ms
     90%   231.91ms
     95%   239.97ms
     99%   246.88ms
  HTTP codes:
    1xx - 0, 2xx - 9496, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.33MB/s
```
### Small table (single row)
```bash
Bombarding http://localhost:8000/small-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       857.71     203.28    1434.40
  Latency      229.79ms    45.89ms   685.18ms
  Latency Distribution
     50%   213.04ms
     75%   246.05ms
     90%   285.95ms
     95%   303.95ms
     99%   407.78ms
  HTTP codes:
    1xx - 0, 2xx - 8759, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   189.05KB/s
```
### Mega table (50 rows)
```bash
Bombarding http://localhost:8000/mega-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       270.51     134.45     527.10
  Latency      705.98ms   195.84ms      1.82s
  Latency Distribution
     50%   699.19ms
     75%   809.36ms
     90%      0.90s
     95%      0.95s
     99%      1.33s
  HTTP codes:
    1xx - 0, 2xx - 2902, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    14.65MB/s
```
### Mega table (single row)
```bash
Bombarding http://localhost:8000/mega-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       798.76     182.49    1050.18
  Latency      247.41ms    40.16ms   578.04ms
  Latency Distribution
     50%   234.43ms
     75%   257.73ms
     90%   301.50ms
     95%   330.70ms
     99%   409.94ms
  HTTP codes:
    1xx - 0, 2xx - 8176, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     1.00MB/s
```
### Related table (50 rows)
```bash
Bombarding http://localhost:8000/related-table/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       320.68     155.42    1190.33
  Latency      602.96ms   188.93ms      1.68s
  Latency Distribution
     50%   590.39ms
     75%   688.05ms
     90%   834.85ms
     95%      0.86s
     99%      1.34s
  HTTP codes:
    1xx - 0, 2xx - 3366, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     5.40MB/s
```
### Related table (single row)
```bash
Bombarding http://localhost:8000/related-table/1/ for 10s using 200 connection(s)
Statistics        Avg      Stdev        Max
  Reqs/sec       723.63     194.84    1323.64
  Latency      271.64ms    77.07ms   821.38ms
  Latency Distribution
     50%   231.29ms
     75%   317.18ms
     90%   373.35ms
     95%   388.12ms
     99%   494.41ms
  HTTP codes:
    1xx - 0, 2xx - 7415, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   544.33KB/s
```
