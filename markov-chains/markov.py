"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # your code goes here
    file = open(file_path).read()

    return file

# print(open_and_read_file("green-eggs.txt"))

def make_chains(text_string):

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    

    words = text_string.split()
    words.append(None)
    
    for i in range(len(words)-2):    
        key = (words[i],words[i+1])   
        value = words[i+2]         

        # if key not in chains:
        #     chains[key] = chains.get(key,[value])
        # elif key in chains:
        #     chains[key].append(value)

        if key not in chains:
            chains[key] = []

        chains[key].append(value) 
    

    # for key,value in chains.items():
    #     print(f'{key}: {value}')
    return chains

#print(make_chains(open_and_read_file("green-eggs.txt")))


def make_text(chains):
    """Return text from chains."""
    
    random_key = choice(list(chains.keys()))    # A random key from a list of keys 
    words = [random_key[0], random_key[1]]      
    random_value = choice(chains[random_key])    # A random value from the random_key

    # create a loop until we reach a None for value
    # Make a new key out of the second word in the first key and the random word 
    # you pulled out from the list of words that followed it.
    # Look up that new key in the dictionary, and pull a new random word out 
    # of the resulting list.
    
    while True:           # while there is a random value 
        random_key = (random_key[1], random_value)             
        words.append(random_value)
        random_value = choice(chains[random_key])   

        if random_value is None:
            break
    
    return " ".join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print("====")
print(random_text)
