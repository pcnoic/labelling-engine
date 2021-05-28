import nltk
import pandas as pd

# Accepts data as string
# Returns array of tokens
def data_tokenize(data):
    data = "".join(d for d in data if d not in ("?", ".", ";", ":", "!", "-", "&", "#"))
    return nltk.word_tokenize(data)

# Accepts array of data
# Returns DataFrames of bigrams and trigrams based on Filtered Frequency Counter
def frequency_extraction(data_array):
    
    # Creating our bigrams and trigrams structures
    bigrams = nltk.collocations.BigramAssocMeasures()
    trigrams = nltk.collocations.TrigramAssocMeasures()
    
    # Creating a bigram_finder object by using tokenized data
    bigram_finder = nltk.collocations.BigramCollocationFinder.from_words(data_array)
    trigram_finder = nltk.collocations.TrigramCollocationFinder.from_words(data_array)
    
    # Creating frequency tables with pandas DataGram structure
    bigram_freq = bigram_finder.ngram_fd.items()
    bigram_freq_table = pd.DataFrame(list(bigram_freq), columns=['bigram','freq']).sort_values(by='freq', ascending=False)
    
    trigram_freq = trigram_finder.ngram_fd.items()
    trigram_freq_table = pd.DataFrame(list(trigram_freq), columns=['trigram', 'freq']).sort_values(by='freq', ascending=False)
    
    return bigram_freq_table, trigram_freq_table
