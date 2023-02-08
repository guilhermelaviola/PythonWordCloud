# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Text path
text = ("../data/toto-africa.txt")

# Image path
image = ("../images/Africa.png")

# Setting stopwords
stopwords = set(STOPWORDS)
africa = np.array(Image.open(image))
# Creating the WordlCloud and defining its stopwords, maximum font size,
# maximum number of words and background color presented in the cloud
wordcloud = WordCloud(stopwords=stopwords,
                      max_font_size=40,
                      max_words=20,
                      background_color="red",
                      mask=africa).generate(' '.join(df['text_without_stopwords']))

# Displaying the generated wordcloud
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

# Storing to file
plt.savefig("africa.png", format="png")
plt.show()