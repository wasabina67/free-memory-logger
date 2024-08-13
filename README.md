# free-memory-logger
Logging free memory in CSV and graph it

## Run

### aaa

```bash
bash src/log_free_memory.sh 
```

### output.csv

```csv
timestamp,free_memory
2024-08-13T11:10:02+09:00,6294
2024-08-13T11:10:03+09:00,6290
...
2024-08-13T11:10:41+09:00,6290
```

### aaa

```bash
python src/graph.py 
```
