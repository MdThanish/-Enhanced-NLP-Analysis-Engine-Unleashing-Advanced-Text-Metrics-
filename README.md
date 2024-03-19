# NLP Task

This Python script is designed to scrape data from a list of URLs, analyze the text content, and compute various NLP (Natural Language Processing) metrics.

## Requirements
- Python 3.x
- Libraries: requests, BeautifulSoup (bs4), pandas, nltk

## 📝 Introduction
The script starts by importing necessary Python packages such as os, re, requests, BeautifulSoup, pandas, and nltk. These packages are essential for web scraping, data manipulation, and NLP tasks.

 ## 📥 Input Data
The input data is stored in an Excel file named Input.xlsx, containing columns 'URL' and 'URL_ID'. This file is read into a pandas DataFrame (df) using pd.read_excel().

## 🌐 Web Scraping
The script iterates through each row in the DataFrame to extract data from the provided URLs. It makes HTTP requests using the requests library and parses the HTML content using BeautifulSoup. The title and text content from each URL are extracted and saved into individual text files in the titleoftext/ directory.

## 📊 Sentiment Analysis
Sentiment analysis is performed using sentiment dictionaries stored in the MasterDictionary/ directory. The script calculates positive and negative scores, polarity score, and subjectivity score for each text file based on the presence of positive and negative words.

## 📏 Readability Metrics
Readability metrics such as average sentence length, percentage of complex words, Fog Index, complex word count, word count, average syllable count per word, and personal pronouns count are calculated for each text file. This is done to assess the complexity and readability of the text.

## Usage
1. Place your input Excel file (`Input.xlsx`) in the root directory.
2. Run the Python script
3. The script will scrape the content from the URLs provided in the input file and compute various NLP metrics.
4. The output will be saved to `Output_Data.csv` in the root directory.

## Directory Structure
- `Input.xlsx`: Input file containing URLs to scrape.
- `Output_Data.csv`: Output file containing computed NLP metrics.
- `StopWords/`: Directory containing stop words lists.
- `titleoftext/`: Directory containing scraped text files.
- `MasterDictionary/`: Directory containing sentiment analysis dictionaries.

## Dependencies
- requests: For making HTTP requests to fetch web content.
- BeautifulSoup (bs4): For parsing HTML content.
- pandas: For data manipulation and analysis.
- nltk: For natural language processing tasks like tokenization and stop words removal.

## NLP Metrics Computed
1. Positive Score
2. Negative Score
3. Polarity Score
4. Subjectivity Score
5. Average Sentence Length
6. Percentage of Complex Words
7. Fog Index
8. Complex Word Count
9. Word Count
10. Average Syllable Count per Word
11. Personal Pronouns Count
12. Average Word Length

## For any issues or suggestions, please feel free to reach out to us:

- Mobile No: +919566592950
- Email ID: mohamedthanish14@gmail.com 
