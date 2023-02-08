import string

def remove_punctuation(input_string):
    # Make a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Use this table to remove punctuation from the input string
    no_punct = input_string.translate(translator)

    return no_punct
