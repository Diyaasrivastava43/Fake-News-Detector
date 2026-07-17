import os
import pandas as pd
import kagglehub
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, classification_report
from text_cleaner import clean_news_text

def get_real_dataset():
    """
    Downloads the dataset via kagglehub, steps into the 'News _dataset' subfolder,
    and combines True and Fake DataFrames into a single training set.
    """
    print("📥 Downloading/Verifying dataset from Kaggle...")
    base_path = kagglehub.dataset_download("emineyetm/fake-news-detection-datasets")
    
    # Target the actual subfolder where the files reside
    path = os.path.join(base_path, "News _dataset")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Expected subfolder 'News _dataset' not found inside: {base_path}")
        
    files_in_dir = os.listdir(path)
    
    fake_filename = next((f for f in files_in_dir if f.lower() == 'fake.csv'), None)
    true_filename = next((f for f in files_in_dir if f.lower() == 'true.csv'), None)
    
    if not fake_filename or not true_filename:
        raise FileNotFoundError(f"Could not locate CSV files inside subfolder: {path}")
        
    fake_df_path = os.path.join(path, fake_filename)
    true_df_path = os.path.join(path, true_filename)
    
    print("📖 Parsing CSV datasets...")
    fake_df = pd.read_csv(fake_df_path)
    true_df = pd.read_csv(true_df_path)
    
    fake_df['label'] = 'FAKE'
    true_df['label'] = 'REAL'
    
    df = pd.concat([fake_df, true_df], ignore_index=True)
    df['text'] = df['title'].fillna('') + " " + df['text'].fillna('')
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    print(f"✅ Loaded {len(df)} total news articles successfully!")
    return df

def train_fake_news_model():
    """ Trains the pipeline on the parsed real dataset. """
    df = get_real_dataset()
    
    print("🧹 Cleaning raw text feature sets...")
    df['cleaned_text'] = df['text'].apply(clean_news_text)
    
    X_train, X_test, y_train, y_test = train_test_split(
        df['cleaned_text'], df['label'], test_size=0.20, random_state=42
    )
    
    print("📈 Extracting numerical elements using TF-IDF...")
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    
    tfidf_train = tfidf_vectorizer.fit_transform(X_train)
    tfidf_test = tfidf_vectorizer.transform(X_test)
    
    print("🧠 Optimizing Passive-Aggressive Classifier weights...")
    pac = PassiveAggressiveClassifier(max_iter=50, random_state=42)
    pac.fit(tfidf_train, y_train)
    
    y_pred = pac.predict(tfidf_test)
    score = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Real Data Validation Accuracy: {round(score * 100, 2)}%\n")
    return tfidf_vectorizer, pac

def predict_news_veracity(news_item, vectorizer, model):
    """ Cleans, transforms, and evaluates input strings. """
    cleaned = clean_news_text(news_item)
    vectorized_input = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized_input)
    return prediction[0]