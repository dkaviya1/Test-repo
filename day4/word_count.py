import sys

def word_count(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            text = file.read()

            # Split the text into words using whitespace as a delimiter
            words = text.split()

            # Initialize a dictionary to store word counts
            word_counts = {}

            # Count the occurrence of each word
            for word in words:
                word = word.lower()  # Convert to lowercase to count words case-insensitively
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

            return word_counts

    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <file_name>")
    else:
        file_name = sys.argv[1]
        word_counts = word_count(file_name)

        for word, count in word_counts.items():
            print(f"{word}: {count}")
