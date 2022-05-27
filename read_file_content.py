# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here
    lines = []
with open('story.txt') as f:
    lines = f.read()

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' # all punctuations
 
 
no_punc = ""
for char in lines:
   if char not in punctuations:
       no_punc = no_punc + char   

lines = no_punc.split()  
store = {}  
for line in lines:
    current = lines.count(line)
    
    store[line] = current
print(store)

read_file_content('story.txt')
count_words()