"""
Spam/Scam Detection - Text Preprocessing Script
This script provides complete text preprocessing pipeline for spam detection
including cleaning, stopword removal, lemmatization, and TF-IDF vectorization.
"""

# ============================================================================
# IMPORTS
# ============================================================================
import re
import pickle
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# ============================================================================
# NLTK DOWNLOADS (Safe with try-except)
# ============================================================================
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Downloading NLTK stopwords...")
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    print("Downloading NLTK wordnet...")
    nltk.download('wordnet', quiet=True)

try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    print("Downloading NLTK omw-1.4...")
    nltk.download('omw-1.4', quiet=True)

print("All NLTK resources loaded successfully!\n")

# ============================================================================
# TEXT CLEANING FUNCTION
# ============================================================================
def clean_text(text):
    """
    Clean text by removing URLs, emails, numbers, and special characters.
    
    Args:
        text (str): Input text to clean
        
    Returns:
        str: Cleaned text in lowercase
    """
    # Convert to string (handle non-string inputs)
    text = str(text)
    
    # Remove URLs (http, https, www)
    text = re.sub(r'http\S+|https\S+|www\.\S+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove special characters (keep only letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# ============================================================================
# STOPWORDS REMOVAL FUNCTION
# ============================================================================
def remove_stopwords(text):
    """
    Remove stopwords from text using NLTK stopwords list.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with stopwords removed
    """
    stop_words = set(stopwords.words('english'))
    
    # Split text into words
    words = text.split()
    
    # Filter out stopwords
    filtered_words = [word for word in words if word not in stop_words]
    
    # Join words back into string
    return ' '.join(filtered_words)

# ============================================================================
# LEMMATIZATION FUNCTION
# ============================================================================
def lemmatize_text(text):
    """
    Lemmatize text using WordNetLemmatizer.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Lemmatized text
    """
    lemmatizer = WordNetLemmatizer()
    
    # Split text into words
    words = text.split()
    
    # Lemmatize each word
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join words back into string
    return ' '.join(lemmatized_words)

# ============================================================================
# COMPLETE PREPROCESSING PIPELINE
# ============================================================================
def preprocess_pipeline(text):
    """
    Complete preprocessing pipeline that applies all cleaning steps.
    
    Args:
        text (str): Raw input text
        
    Returns:
        str: Fully preprocessed text
    """
    # Step 1: Clean text
    text = clean_text(text)
    
    # Step 2: Remove stopwords
    text = remove_stopwords(text)
    
    # Step 3: Lemmatize
    text = lemmatize_text(text)
    
    return text

# ============================================================================
# TF-IDF VECTORIZATION
# ============================================================================
def create_tfidf_features(texts, max_features=3000, save_path='tfidf_vectorizer.pkl'):
    """
    Create TF-IDF features from preprocessed texts.
    
    Args:
        texts (list): List of preprocessed text strings
        max_features (int): Maximum number of features for TF-IDF
        save_path (str): Path to save the fitted vectorizer
        
    Returns:
        tuple: (tfidf_matrix, vectorizer)
    """
    print(f"Creating TF-IDF features with max_features={max_features}...")
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(max_features=max_features)
    
    # Fit and transform the texts
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Save the vectorizer using pickle
    with open(save_path, 'wb') as f:
        pickle.dump(vectorizer, f)
    print(f"Vectorizer saved to: {save_path}")
    
    return tfidf_matrix, vectorizer

# ============================================================================
# LOAD SAVED VECTORIZER
# ============================================================================
def load_tfidf_vectorizer(path='tfidf_vectorizer.pkl'):
    """
    Load a saved TF-IDF vectorizer.
    
    Args:
        path (str): Path to the saved vectorizer
        
    Returns:
        TfidfVectorizer: Loaded vectorizer
    """
    with open(path, 'rb') as f:
        vectorizer = pickle.load(f)
    print(f"Vectorizer loaded from: {path}")
    return vectorizer

# ============================================================================
# EXAMPLE USAGE
# ============================================================================
if __name__ == "__main__":
    print("="*70)
    print("SPAM/SCAM DETECTION - PREPROCESSING EXAMPLE")
    print("="*70)
    
    # Example texts (simulating spam/ham messages)
    example_texts = [
        "WINNER!! You have won a $1000 prize! Call 123-456-7890 now!",
        "Hey, are we still meeting for lunch tomorrow at 2pm?",
        "FREE entry to win! Text WIN to 12345. Visit http://example.com",
        "Can you pick up some milk on your way home? Thanks!",
        "Congratulations! You've been selected for a FREE iPhone. Email us at spam@example.com",
        "Meeting rescheduled to 3pm. See you in the conference room.",
        "URGENT: Your account will be closed! Click here: www.phishing.com",
        "Happy birthday! Hope you have a wonderful day!",
        "Get 50% OFF on all products! Limited time offer! Call 999-888-7777",
        "Don't forget to submit your report by Friday."
    ]
    
    print(f"\nProcessing {len(example_texts)} example texts...\n")
    
    # Step 1: Preprocess all texts
    print("Step 1: Preprocessing texts...")
    print("-" * 70)
    preprocessed_texts = []
    
    for i, text in enumerate(example_texts, 1):
        cleaned = preprocess_pipeline(text)
        preprocessed_texts.append(cleaned)
        print(f"{i}. Original: {text[:60]}...")
        print(f"   Cleaned:  {cleaned[:60]}...\n")
    
    # Step 2: Create TF-IDF features
    print("\n" + "="*70)
    print("Step 2: Creating TF-IDF Features...")
    print("-" * 70)
    tfidf_matrix, vectorizer = create_tfidf_features(
        preprocessed_texts, 
        max_features=3000,
        save_path='tfidf_vectorizer.pkl'
    )
    
    # Step 3: Display results
    print("\n" + "="*70)
    print("RESULTS")
    print("="*70)
    print(f"TF-IDF Matrix Shape: {tfidf_matrix.shape}")
    print(f"  - Number of documents: {tfidf_matrix.shape[0]}")
    print(f"  - Number of features: {tfidf_matrix.shape[1]}")
    print(f"\nVocabulary size: {len(vectorizer.vocabulary_)}")
    print(f"\nFirst 10 features: {list(vectorizer.vocabulary_.keys())[:10]}")
    
    # Step 4: Load CSV files and preprocess
    print("\n" + "="*70)
    print("PROCESSING CSV FILES")
    print("="*70)
    
    try:
        # Load email.csv
        print("\nLoading email.csv...")
        df_email = pd.read_csv('email.csv')
        print(f"Loaded {len(df_email)} messages from email.csv")
        print(f"Columns: {df_email.columns.tolist()}")
        
        # Preprocess email.csv
        df_email['cleaned_message'] = df_email['Message'].apply(preprocess_pipeline)
        print(f"Preprocessed {len(df_email)} messages from email.csv")
        
    except FileNotFoundError:
        print("email.csv not found!")
    
    try:
        # Load spam.csv (try different encodings)
        print("\nLoading spam.csv...")
        try:
            df_spam = pd.read_csv('spam.csv', encoding='utf-8')
        except UnicodeDecodeError:
            df_spam = pd.read_csv('spam.csv', encoding='latin-1')
        
        print(f"Loaded {len(df_spam)} messages from spam.csv")
        print(f"Columns: {df_spam.columns.tolist()}")
        
        # Preprocess spam.csv (v2 contains the message)
        df_spam['cleaned_message'] = df_spam['v2'].apply(preprocess_pipeline)
        print(f"Preprocessed {len(df_spam)} messages from spam.csv")
        
    except FileNotFoundError:
        print("spam.csv not found!")
    
    print("\n" + "="*70)
    print("PREPROCESSING COMPLETE!")
    print("="*70)
    print("\nYou can now use the preprocessed data for model training.")
    print("The TF-IDF vectorizer has been saved to 'tfidf_vectorizer.pkl'")
