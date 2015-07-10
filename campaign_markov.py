import sys
from random import choice


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    chains = {}

    line = corpus.split()
  
    for word in range(len(line)-2):
        key = (line[word], line[word + 1])
        value = line[word + 2]
        
        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    chain_keys = chains.keys()
    key = chain_keys[0]
    words = [key[0], key[1]]
    count = 0

    # Keep doing this until we reach the end or until we go too
    # long for a Twitter message
    while key in chains and count < 140:

        word = choice(chains[key])
        count += len(word)
        words.append(word)
        key = (key[1], word)

    return " ".join(words)


input_path = sys.argv[1]
input_text = open(input_path).read()

chains = make_chains(input_text)

random_text = make_text(chains)

print random_text
