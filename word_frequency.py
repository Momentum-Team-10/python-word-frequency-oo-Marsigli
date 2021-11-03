STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename, 'r') as text:
        # this reads the entire file and puts this into text string
            text_string = text.read()
        text.close()
        
        return text_string


class WordList:
    def __init__(self, text):
        self.text_string = text
        self.words_list = []
        self.no_stop_words = {}

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        # this removes the specified characters from the text string
        self.text_string = self.text_string.replace(",", "")
        self.text_string = self.text_string.replace(".", "")
        self.text_string = self.text_string.replace("—", " ")
        self.text_string = self.text_string.replace("-", " ")
        self.text_string = self.text_string.replace("?", "")
        self.text_string = self.text_string.replace(":", "")
        self.text_string = self.text_string.replace("'", "")
        self.text_string = self.text_string.replace("\\n", "")
        self.text_string = self.text_string.replace("’", "")
        self.text_string = self.text_string.replace("]", "")
        self.text_string = self.text_string.replace("[", "")
        self.text_string = self.text_string.replace("\"", "")
        self.words_list = self.text_string.split()
        

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        for word in self.words_list:
            # checking to see if the word is stop words
            if word not in STOP_WORDS:
                # if the word is already in the dictionary no stop words increment the value by 1
                if word in self.no_stop_words:
                    self.no_stop_words[word] += 1
                # if the word is not in the dictionary no stop words add this to the dictionary and give it a value of 1
                else:
                    self.no_stop_words[word] = 1
                

    def get_freqs(self):
        sorted_dict = {}
        sorted_keys = sorted(self.no_stop_words, key=self.no_stop_words.get, reverse=True)  
        for w in sorted_keys:
            sorted_dict[w] = self.no_stop_words[w]
        return sorted_dict


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        counter = 0        
        for key in self.freqs:
            counter += 1
            print(f"{key:>15} | {self.freqs[key]:2} {'*' * self.freqs[key]}")
            if counter > 10:
                break


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
