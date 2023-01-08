# Introduction
Online classified ads are an essential component of every business' digital marketing strategy. Due to the platform's enormous potential, fraudsters have been drawn to it, which has hampered the growth of online advertising. Because of this, spotting fake advertisements on such platforms is a critical problem that has to be efficiently filtered out. The solution will provide a creative approach to develop a scam detection program that will mark an advertisement as potentially fraudulent based on particular criteria. This project also discovered characteristics that are most frequently found in fake advertising based on a few study publications, for example, phone and email not provided in the listings and price-based heuristics.

The project scope is limited to cars and pickup trucks which are one the most sold items on craigslist and the range of these items being sold is within 60-mile radius of Chicago. The goal of this project is multi-fold.

• First, the aim is to gain the trust of the audience and increase the credibility of the platform.

• Second, craigslist should able to sell more quickly as genuine ads gather more traction from the buyers.

• Finally, this will save people from getting scammed and increase awareness among the customers.

# Methodology

## Data Extraction
Scrape the required data about all the listings from Craigslist. Used the following python libraries - BeautifulSoup, NumPy and Pandas.

## Data Pre-processing

Before feeding the textual columns into the models we had to perform the following preprocessing steps on the “Clean Description” columns:
- Removal of HTML Tags such as ‘/a’,</br>
- Removal of Punctuations
- Removal of most common words occurring across all the documents
- Tokenization of sentences
- Lemmatization of tokens (this step was not followed for topic modelling)
- Stopwords removal
- TF-IDF vectorization to finally convert the textual data into numerical vectors

The above pre-processing steps were performed for feeding the data into classical ML Models. For preparing the data for advanced modelling techniques such as Recurrent LSTM NN, we had to perform further pre-processing on the textual data such as:
- Converting text to sequence (Instead of TF-IDF vectorization implemented for Classical models)
- Pre-Padding the sequences

## Classification Models

Since the data was highly imbalanced (4% Probable Scam labelled as True), data had to be stratified and split it into training and testing. The split in vectorized data was in a ratio of 80-20 of training and validation. 

7 machine learning algorithms :

-Random Forest

-Extra TreeClassifier

-Support VectorClassifier

-XGBoost RFClassifier

-Voting Classifier

-LSTM Neural Network

## Results

20% test data was set kept aside to validate the performance of different models. The evaluation metric chosen for selection of best model out of all the models implemented was AUC ROC score or “The Area Under ROC Curve”. I wanted to maintain a balance between both False Positive Rate and True Positive Rate, as the genuine ad listings being predicted as scam (False Positive) would prove to be an impairment to the craigslist’s business. Based on all the models trained, LSTM gives us the best validation ROC AUC Score of 0.7398 on test data set.

## Recommendation and Conclusion
There is a need for Craiglist to implement effective scam filters in their website so that they don’t lose their credibility and gain the trust of audience. They could employ other state-ofthe-art techniques like text mining on the description and recognize trends in image/text posts to identify scams. This a vast domain of research and one could apply different business rules for scam identification. Although Craiglist offers guidelines for potential buyers to save themselves from getting scammed but clearly it is not enough. FTC reported that ~2.8 million people were scammed in the year 2021 alone. Out of these, Auto related scams also amounted to ~137k reports being filed. This brings in a need for Craigslist to not only host credible sellers but also regularly scrutinize the ads posted on the platform

