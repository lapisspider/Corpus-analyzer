import scanner


def main():
    print("Input the folder path to scan for text files:")
    folder_path = input().strip()
    files = scanner.scanner(folder_path)
    print(f"Found {len(files)} text files in {folder_path}:")
    print(f" File names:")
    for file in files:
        print(f"{file.name:<25}, Path: {file}")

if __name__ == "__main__":
    main()