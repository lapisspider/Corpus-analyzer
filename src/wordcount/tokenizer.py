     count = 0
        print(f"-- {file.name} ---")
        with file.open("r", encoding="utf-8") as f:
            words = f.read().split()
            count += len(words)
            for word in words:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
        print(f"Word count: {count}")
        print(file.read_text())
        print(dictionary)
    return count, dictionary
