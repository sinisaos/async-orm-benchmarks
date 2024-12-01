# async-orm-benchmarks

## Simulated server-database latency

As in this [example case](https://github.com/edgedb/imdbench), we simulate the latency between the server and the database to get more realistic benchmarks.

On Linux, this latency can be simulated with `tc` tool like this:

```bash
sudo tc qdisc replace dev lo root netem delay 1ms
```

Once we finish our benchmark, it is important to delete the rule which we have set.

```bash
sudo tc qdisc delete dev lo root
```