import string

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""


def clean_text(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text


def process_text(text):
    words = text.split()
    count = len(words)

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    if not freq:
        return count, None, 0

    max_word = max(freq, key=freq.get)
    return count, max_word, freq[max_word]


def main():
    filename = input("Enter filename: ")
    text = read_file(filename)

    text = clean_text(text)

    count, max_word, max_count = process_text(text)

    print("Word count:", count)

    if max_word:
        print(f"Most frequent word: '{max_word}' ({max_count} times)")
    else:
        print("No words found.")


if __name__ == "__main__":
    main()
