📰 Project: Fake News Detection
🛠️ Codebase Overview
1. app.py
Builds the reactive frontend UI utilizing Streamlit. It loads the model, caches resources to prevent redundant training, displays status messages, accepts raw user input via a text area, and outputs the prediction with clear, color-coded styling based on the classification.

Core UI Components: Custom titles, descriptions, spinner states, toasts for user feedback, metrics panels, and semantic status banners (st.error for Fake, st.success for Authentic).
2. model_pipeline.py
Handles the backend data science workflow:

get_real_dataset(): Downloads the emniyetm/fake-news-detection-datasets dataset from Kaggle via kagglehub, extracts the subfolder files, aligns them into a single pandas DataFrame, and pre-cleans the text feature sets.
train_fake_news_model(): Sets up an 80/20 train-test split, extracts numerical features using a TF-IDF vectorizer, trains a Passive-Aggressive Classifier (max iterations = 50), and reports model performance metrics.
predict_news_veracity(): Preprocesses single input strings through the sanitization pipeline, vectorizes them, and runs model predictions to return the final classification verdict.
