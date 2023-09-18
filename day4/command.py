import sys
from word_count import word_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python command.py <apple.txt>")
    else:
        file_name = sys.argv[1]
        word_counts = word_count(file_name)

        for word, count in word_counts.items():
            print(f"{word}: {count}")
