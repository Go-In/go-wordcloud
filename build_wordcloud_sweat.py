from os import path
from wordcloud import WordCloud

text = open('tocloud_sweat.txt').read()
wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt
import deepcut

wordcloud = WordCloud(font_path='THSarabunNew.ttf',
                      background_color="white",
                      width=1024, # กว้าง
                      height=768, # ยาว
                      collocations=False,
                      regexp=r"[\u0E00-\u0E7Fa-zA-Z']+"
                      ).generate(' '.join(deepcut.tokenize(text)))
plt.imshow(wordcloud, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()