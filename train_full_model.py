"""
Spam/Scam Detection - Complete Training Script
This script trains a full model with TF-IDF vectorizer built from the entire dataset.
"""

# ============================================================================
# IMPORTS
# ============================================================================
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score,
    classification_report,
    confusion_matrix
)

# Import preprocessing function
from preprocessing import preprocess_pipeline

# ============================================================================
# LOAD AND PREPARE DATASET
# ============================================================================
def load_and_prepare_data(csv_files=['email.csv', 'spam.csv']):
    """Load datasets from CSV files."""
    all_texts = []
    all_labels = []
    
    for csv_file in csv_files:
        try:
            print(f"Loading dataset: {csv_file}")
            
            # Try different encodings
            try:
                df = pd.read_csv(csv_file, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(csv_file, encoding='latin-1')
            
            print(f"  Loaded {len(df)} records")
            
            # Handle different CSV formats
            if 'email.csv' in csv_file:
                texts = df['Message'].tolist()
                labels = [1 if label == 'spam' else 0 for label in df['Category']]
            elif 'spam.csv' in csv_file:
                texts = df['v2'].tolist()
                labels = [1 if label == 'spam' else 0 for label in df['v1']]
            
            all_texts.extend(texts)
            all_labels.extend(labels)
            
            spam_count = sum(labels)
            ham_count = len(labels) - spam_count
            print(f"  ✓ Spam: {spam_count}, Ham: {ham_count}\n")
            
        except Exception as e:
            print(f"  ✗ Error: {str(e)}\n")
            continue
    
    print(f"Total: {len(all_texts)} messages (Spam: {sum(all_labels)}, Ham: {len(all_labels) - sum(all_labels)})\n")
    return all_texts, all_labels

# ============================================================================
# MAIN TRAINING PIPELINE
# ============================================================================
def main():
    print("="*70)
    print("SPAM/SCAM DETECTION - FULL MODEL TRAINING")
    print("="*70)
    print()
    
    # Load data
    texts, labels = load_and_prepare_data(['email.csv', 'spam.csv'])
    
    if len(texts) == 0:
        print("Error: No data loaded.")
        return
    
    # Preprocess all texts
    print("Preprocessing all texts...")
    cleaned_texts = [preprocess_pipeline(text) for text in texts]
    print(f"✓ Preprocessed {len(cleaned_texts)} texts\n")
    
    # Split data first (80% train, 20% test)
    print("Splitting data (80/20)...")
    X_train_text, X_test_text, y_train, y_test = train_test_split(
        cleaned_texts, labels, test_size=0.2, random_state=42, stratify=labels
    )
    print(f"✓ Training: {len(X_train_text)} samples")
    print(f"✓ Test: {len(X_test_text)} samples\n")
    
    # Create and fit TF-IDF vectorizer on training data only
    print("Creating TF-IDF vectorizer (max_features=3000)...")
    vectorizer = TfidfVectorizer(max_features=3000)
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)
    print(f"✓ Training matrix: {X_train.shape}")
    print(f"✓ Test matrix: {X_test.shape}")
    print(f"✓ Vocabulary size: {len(vectorizer.vocabulary_)}\n")
    
    # Save vectorizer
    with open('tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    print("✓ Vectorizer saved to: tfidf_vectorizer.pkl\n")
    
    # Train model
    print("Training Logistic Regression...")
    model = LogisticRegression(
        max_iter=1000,
        random_state=42,
        class_weight='balanced',
        solver='liblinear'
    )
    model.fit(X_train, y_train)
    print("✓ Training complete!\n")
    
    # Evaluate
    print("="*70)
    print("MODEL EVALUATION")
    print("="*70)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"\nAccuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"Precision: {precision:.4f} ({precision*100:.2f}%)")
    print(f"Recall:    {recall:.4f} ({recall*100:.2f}%)")
    print(f"F1-Score:  {f1:.4f} ({f1*100:.2f}%)")
    
    print("\n" + "-"*70)
    print("CONFUSION MATRIX")
    print("-"*70)
    cm = confusion_matrix(y_test, y_pred)
    print(f"\n                Predicted")
    print(f"              Ham    Spam")
    print(f"Actual Ham    {cm[0][0]:<6} {cm[0][1]:<6}")
    print(f"       Spam   {cm[1][0]:<6} {cm[1][1]:<6}")
    
    print("\n" + "-"*70)
    print("CLASSIFICATION REPORT")
    print("-"*70)
    print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))
    
    # Save model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("-"*70)
    print("✓ Model saved to: model.pkl\n")
    
    print("="*70)
    print("TRAINING COMPLETE!")
    print("="*70)
    
    # Test predictions
    print("\n" + "="*70)
    print("EXAMPLE PREDICTIONS")
    print("="*70)
    
    test_messages = [
        "Congratulations! You've won a FREE iPhone! Click here now!",
        "Hey, can we meet for coffee tomorrow at 3pm?",
        "URGENT: Your account will be suspended. Call now!",
        "Thanks for the meeting. I'll send the report by Friday.",
        "Win $1000 cash! Text WIN to 12345! Limited offer!"
    ]
    
    for i, msg in enumerate(test_messages, 1):
        cleaned = preprocess_pipeline(msg)
        X = vectorizer.transform([cleaned])
        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0]
        
        label = "SPAM" if pred == 1 else "HAM"
        confidence = prob[pred] * 100
        
        print(f"\n{i}. {msg[:55]}...")
        print(f"   → {label} (confidence: {confidence:.2f}%)")

if __name__ == "__main__":
    main()
