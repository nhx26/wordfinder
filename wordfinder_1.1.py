#A.Gopee
#word_finder_1.1

#Use:
#Input words and stop input with the word "end"
#note: words not on merriam-webster will not load a webpage

#v1.1: added delay to display web pages in correct order

import webbrowser
import time
words = []
count = 1
while True:
    word = raw_input("Input word " + str(count) + ": ")
    if word <> "end":
        
        words.append(str(word))
        count = count + 1
    else:
        break
for word in words:
    
    url = "https://www.merriam-webster.com/dictionary/" + word
    webbrowser.open_new_tab(url)
    time.sleep(0.2)
    
