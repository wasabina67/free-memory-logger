# free-memory-logger
Logging free memory in CSV and Graph it

## Setup

```bash
pipenv shell
```

```bash
pipenv sync
```

## Run

### Create output.csv

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

### Create output.png

```bash
python src/graph.py
```

### output.png

![output](https://github.com/user-attachments/assets/fa09ff1d-f256-4180-9159-4551fdca06c1)
