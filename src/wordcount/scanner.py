from pathlib import Path

folder = Path("src")
count = 0
for file in folder.rglob("*.txt"):
    print(f"-- {file.name} ---")
    with file.open("r", encoding="utf-8") as f:
        words = f.read().split()
        count += len(words)
    print(f"Word count: {count}")
    print(file.read_text())