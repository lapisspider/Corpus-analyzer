from pathlib import Path

def scanner(folder_path):
    folder = Path(folder_path)
    return list(folder.rglob("*.txt"))