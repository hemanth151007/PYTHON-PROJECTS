def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""

def count_words(sentence):
    words=sentence.split()
    return len(words)
def frequent_words(sentence):
    words=sentence.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    max_word=max(freq,key=freq.get)
    return max_word,freq[max_word]
def main():
    filename=input("Enter the filename: ")
    sentence=read_file(filename)
    words_count=count_words(sentence)
    print(f"The number of words in the sentence is: {words_count}")
    max_word,max_count=frequent_words(sentence)
    print(f"The most frequent word is '{max_word}' which appears {max_count} times.")
if __name__=="__main__":
    main()
