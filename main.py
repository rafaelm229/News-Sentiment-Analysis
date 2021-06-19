from textblob import TextBlob, blob
from newspaper import Article
import nltk

print("\n Downloading packages... \n")
nltk.download('punkt')

# News Link
url = "https://www.bbc.com/sport/football/57534430"
article = Article(url)

# Extrating data 
article.download()
article.parse()
article.nlp()

text = article.summary
print("\n====== Article Summary =======\n")
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print("\n======= Result ========\n")
print(sentiment)