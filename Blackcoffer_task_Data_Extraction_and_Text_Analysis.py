#import necessary packages
import os
import re

import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_excel('C:/Thanish Projects/blackCoffer_nlp_task/Input.xlsx')
df.head(4)


#read the url file into the pandas object
df = pd.read_excel('C:/Thanish Projects/blackCoffer_nlp_task/Input.xlsx')

#loop throgh each row in the df
for index, row in df.iterrows():
  url = row['URL']
  url_id = row['URL_ID']

  # make a request to url
  header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
  try:
    response = requests.get(url,headers=header)
  except:
    print("can't get response of {}".format(url_id))

  #create a beautifulsoup object
  try:
    soup = BeautifulSoup(response.content, 'html.parser')
  except:
    print("can't get page of {}".format(url_id))
  #find title
  try:
    title = soup.find('h1').get_text()
  except:
    print("can't get title of {}".format(url_id))
    continue
  #find text
  article = ""
  try:
    for p in soup.find_all('p'):
      article += p.get_text()
  except:
    print("can't get text of {}".format(url_id))

  #write title and text to the file
  file_name = 'C:/Thanish Projects/blackCoffer_nlp_task/titleoftext/' + str(url_id) + '.txt'
  with open(file_name, 'w', encoding='utf-8') as file:
    file.write(title + '\n' + article)


# Directories
text_dir = "C:/Thanish Projects/blackCoffer_nlp_task/titleoftext"
stopwords_dir = "C:/Thanish Projects/blackCoffer_nlp_task/StopWords"
sentment_dir = "C:/Thanish Projects/blackCoffer_nlp_task/MasterDictionary"

# load all stop wors from the stopwords directory and store in the set variable
stop_words = set()
for files in os.listdir(stopwords_dir):
  with open(os.path.join(stopwords_dir,files),'r',encoding='ISO-8859-1') as f:
    stop_words.update(set(f.read().splitlines()))

# load all text files  from the  directory and store in a list(docs)
docs = []
for text_file in os.listdir(text_dir):
  with open(os.path.join(text_dir, text_file), 'r', encoding='utf-8') as f:
    text = f.read()
#tokenize the given text file
    words = word_tokenize(text)
# remove the stop words from the tokens
    filtered_text = [word for word in words if word.lower() not in stop_words]
# add each filtered tokens of each file into a list
    docs.append(filtered_text)
# store positive, Negative words from the directory
pos=set()
neg=set()

for files in os.listdir(sentment_dir):
  if files =='positive-words.txt':
    with open(os.path.join(sentment_dir,files),'r',encoding='ISO-8859-1') as f:
      pos.update(f.read().splitlines())
  else:
    with open(os.path.join(sentment_dir,files),'r',encoding='ISO-8859-1') as f:
      neg.update(f.read().splitlines())

# now collect the positive  and negative words from each file
# calculate the scores from the positive and negative words 
positive_words = []
Negative_words =[]
positive_score = []
negative_score = []
polarity_score = []
subjectivity_score = []

#iterate through the list of docs
for i in range(len(docs)):
  positive_words.append([word for word in docs[i] if word.lower() in pos])
  Negative_words.append([word for word in docs[i] if word.lower() in neg])
  positive_score.append(len(positive_words[i]))
  negative_score.append(len(Negative_words[i]))
  polarity_score.append((positive_score[i] - negative_score[i]) / ((positive_score[i] + negative_score[i]) + 0.000001))
  subjectivity_score.append((positive_score[i] + negative_score[i]) / ((len(docs[i])) + 0.000001))

text_dir = "C:/Thanish Projects/blackCoffer_nlp_task/titleoftext"
stopwords_dir = "C:/Thanish Projects/blackCoffer_nlp_task/StopWords"

# Load all stopwords from the stopwords directory and store in the stopwords_set variable
stopwords_set = set()
for filename in os.listdir(stopwords_dir):
    with open(os.path.join(stopwords_dir, filename), 'r', encoding='ISO-8859-1') as f:
        stopwords_set.update(set(f.read().splitlines()))

# Function to measure readability metrics
def measure(file):
    with open(os.path.join(text_dir, file), 'r', encoding='utf-8') as f:
        text = f.read()
        
    # Remove punctuations 
    text = re.sub(r'[^\w\s.]', '', text)
    
    # Tokenize the given text file
    words = word_tokenize(text)
    
    # Remove stopwords from the tokens
    filtered_text = [word for word in words if word.lower() not in stopwords_set]
    
    # Complex words having syllable count greater than 2
    complex_words = [word for word in filtered_text if len(word) > 2]
    
    # Syllable count per word
    syllable_count = sum(1 for word in filtered_text for letter in word if letter.lower() in 'aeiou')
    
    # Average sentence length
    avg_sentence_len = len(filtered_text)
    
    # Percentage of complex words
    percent_complex_words = len(complex_words) / len(filtered_text) if len(filtered_text) > 0 else 0
    
    # Fog Index
    fog_index = 0.4 * (avg_sentence_len + percent_complex_words)
    
    return avg_sentence_len, percent_complex_words, fog_index, len(complex_words), syllable_count

# Lists to store results
avg_sentence_length = []
percent_complex_words = []
fog_index = []
complex_word_count = []
avg_syllable_word_count = []

# Iterate through each file
for file in os.listdir(text_dir):
    x, y, z, a, b = measure(file)
    avg_sentence_length.append(x)
    percent_complex_words.append(y)
    fog_index.append(z)
    complex_word_count.append(a)
    avg_syllable_word_count.append(b)

# Word Count and Average Word Length Sum of the total number of characters in each word/Total number of words
# We count the total cleaned words present in the text by 
# removing the stop words (using stopwords class of nltk package).
# removing any punctuations like ? ! , . from the word before counting.

def cleaned_words(file):
    with open(os.path.join(text_dir, file), 'r', encoding='utf-8') as f:
        text = f.read()
        text = re.sub(r'[^\w\s]', '', text)
        words = [word for word in text.split() if word.lower() not in stopwords_set]
        length = sum(len(word) for word in words)
        average_word_length = length / len(words) if len(words) > 0 else 0
    return len(words), average_word_length

word_count = []
average_word_length = []
for file in os.listdir(text_dir):
  x, y = cleaned_words(file)
  word_count.append(x)
  average_word_length.append(y)


# To calculate Personal Pronouns mentioned in the text, we use regex to find 
# the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken
#  so that the country name US is not included in the list.
def count_personal_pronouns(file):
  with open(os.path.join(text_dir, file), 'r', encoding='utf-8') as f:
    text = f.read()
    personal_pronouns = ["I", "we", "my", "ours", "us"]
    count = 0
    for pronoun in personal_pronouns:
      count += len(re.findall(r"\b" + pronoun + r"\b", text)) # \b is used to match word boundaries
  return count

pp_count = []
for file in os.listdir(text_dir):
  x = count_personal_pronouns(file)
  pp_count.append(x)


# Function to calculate Percentage_of_Complex_words and Fog_Index
def calculate_complexity(file):
    with open(os.path.join(text_dir, file), 'r', encoding='utf-8') as f:
        text = f.read()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuations
        words = word_tokenize(text)  # Tokenize the text
        filtered_text = [word for word in words if word.lower() not in stopwords_set]  # Remove stopwords
        complex_words = [word for word in filtered_text if len(word) > 2]  # Complex words (syllable count > 2)
        percent_complex_words = len(complex_words) / len(filtered_text) if len(filtered_text) > 0 else 0  # Percentage of complex words
        avg_sentence_length = len(filtered_text)  # Average sentence length
        fog_index = 0.4 * (avg_sentence_length + percent_complex_words)  # Fog Index
    return percent_complex_words, fog_index

# Lists to store results
Percentage_of_Complex_words = []
Fog_Index = []

# Iterate through each file to calculate Percentage_of_Complex_words and Fog_Index
for file in os.listdir(text_dir):
    pcw, fog = calculate_complexity(file)
    Percentage_of_Complex_words.append(pcw)
    Fog_Index.append(fog)

# Read the output data structure from Excel
output_df = pd.read_excel('C:/Thanish Projects/blackCoffer_nlp_task/Output Data Structure.xlsx')

# URL_ID 44, 57, 144 does not exist, i.e., the page does not exist and throws a 404 error
# Drop these rows from the table
output_df.drop([7, 20, 107], axis=0, inplace=True)

# Define the required parameters
variables = [positive_score,
             negative_score,
             polarity_score,
             subjectivity_score,
             avg_sentence_length,
             Percentage_of_Complex_words,
             Fog_Index,
             complex_word_count,
             word_count,
             avg_syllable_word_count,
             pp_count,
             average_word_length]

for i, var in enumerate(variables):
    if len(var) != len(output_df):
        print(f"Length mismatch for variable {i+2} ({output_df.columns[i+2]}): Expected {len(output_df)} values, but got {len(var)}")
    else:
        output_df.iloc[:, i+2] = var

# Add average_word_length to the DataFrame
output_df['AVG WORD LENGTH'] = average_word_length
output_df['PERSONAL PRONOUNS'] = pp_count

# Save the DataFrame to CSV
try:
    output_df.to_csv('C:/Thanish Projects/blackCoffer_nlp_task/Output_Data.csv', index=False)
    print("Data saved successfully to 'Output_Data.csv'")
except Exception as e:
    print(f"An error occurred while saving the data: {e}")

