"""Starter P3 — lengkapi training TF-IDF + classifier dan simpan artifact."""

from pathlib import Path

DATA = Path(__file__).with_name("training_samples.csv")


def main() -> None:
    print(f"Dataset tersedia di: {DATA}")
    print("TODO: baca CSV -> split/evaluasi -> fit pipeline -> serialisasi model.")


if __name__ == "__main__":
    main()
