import matplotlib.pyplot as plt
import pandas as pd  # type: ignore


def main():
    df = pd.read_csv("output.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    plt.figure(figsize=(10, 6))
    plt.plot(df["timestamp"], df["free_memory"])

    plt.title("free-memory-logger")
    plt.xlabel("Time")
    plt.ylabel("Free Memory (MB)")
    plt.grid(True)
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig("output.png")


if __name__ == "__main__":
    main()
