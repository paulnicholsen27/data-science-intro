from wannabe import lyrics
import string
import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
init_notebook_mode(connected=True)

lyrics = lyrics.replace("\n", " ")

for punctuation_mark in string.punctuation:
    if punctuation_mark == "'":
        pass
    else:
        lyrics = lyrics.replace(punctuation_mark, "")
lyrics = lyrics.lower()
list_of_lyrics = lyrics.split(" ")
unique_words = set(list_of_lyrics)
print "test"
word_count = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    # word_count[word] = word_count[word] + 1
    word_count[word] += 1


trace = {'type': 'bar', 'x': list(word_count.keys()), 'y': list(word_count.values())}

plotly.offline.iplot({'data': [trace]})