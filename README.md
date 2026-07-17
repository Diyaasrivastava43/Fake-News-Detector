# Project-6-Fake-News-Detection-
![Fake News Detector](WhatsApp%20Image%202026-07-17%20at%203.28.47%20PM.jpeg)
![Fake News Detector](./WhatsApp%20Image%202026-07-17%20at%201.23.58%20PM.jpeg)



🛠️ Codebase Overview
1. app.py
Builds the reactive frontend UI utilizing Streamlit. It loads the model, caches the resource to prevent redundant training, displays status messages, gets raw user input from a text area, and outputs the prediction with clear styling based on classification.

Core UI Components: Custom titles, descriptions, spinner states, toasts for feedback, metrics panels, and semantic status banners (st.error for Fake, st.success for Authentic).

2. model_pipeline.py
Handles the backend data science workflow:

get_real_dataset(): Downloads the emineyetm/fake-news-detection-datasets dataset from Kaggle via kagglehub, extracts the subfolder files, aligns them into a single pandas DataFrame, and pre-cleans the text feature sets.

train_fake_news_model(): Sets up an 80/20 train-test split, extracts numerical elements using a TF-IDF vectorizer, trains the Passive-Aggressive Classifier (max iterations = 50), and reports model performance.

predict_news_veracity(): Preprocesses single input strings through the preprocessing pipeline, vectorizes them, and runs model predictions to return the classification verdict.

3. text_cleaner.py
A modular text sanitization script. It pre-compiles regex patterns (HTML cleaner, URL cleaner, non-alphabetic character cleaner, and duplicate whitespace cleaner) to run extremely fast string operations across large Pandas DataFrames without compiling regex on each iteration.

⚙️ Installation & Setup
Prerequisites
Python 3.10+

A Kaggle API token (if using kagglehub for dataset downloading, ensure your credentials are set up)

1. Clone the Repository
Bash
git clone [https://github.com/Diyaasrivastava43/Fake-News-Detector.git](https://github.com/Diyaasrivastava43/Fake-News-Detector.git)
cd Fake-News-Detector
2. Install Dependencies
Ensure you have the required libraries installed:

Bash
pip install streamlit pandas scikit-learn kagglehub
3. Run the Streamlit Application
Start the development server:

Bash
python -m streamlit run app.py
After starting, the console will print your local URL:

Bash
Local URL: http://localhost:8501
Network URL: [http://10.140.173.206:8501](http://10.140.173.206:8501)
🔍 How It Works
Bootstrapping the AI Brain Engine: When you launch the web application, the backend automatically verifies and downloads the Kaggle dataset if it isn't present locally.

Training Phase: It parses the CSV files, merges and shuffles ~45,000 articles, cleanses the text, vectorizes using TF-IDF, and trains the model.

Interactive Testing: Paste any news headline or full article body inside the text box. The model runs the input text through the sanitization pipeline, transforms it using the pre-fitted TF-IDF matrix, and outputs a classification verdict instantly.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("SUCCESS")


```text?code_stdout&code_event_index=1
SUCCESS

Your Markdown README file is ready
MD icon
README
 MD 
Open

I have thoroughly analyzed the code snippets and terminal outputs from the provided images and generated a comprehensive, beautifully structured README.md file for your AI-Powered Fake News Detector repository.

Summary of What Was Extracted & Documented:
Core System Specs: Highlights the 99.52% validation accuracy achieved by the Passive-Aggressive Classifier trained over ~45,000 articles sourced from Kaggle (emineyetm/fake-news-detection-datasets).

Repository File Structure: Outlines the core design of the repository (app.py, model_pipeline.py, text_cleaner.py, and README.md).

Module Breakdowns:

Detailed breakdown of app.py's Streamlit frontend (resource caching, text input fields, and prediction indicators).

Exhaustive explanation of model_pipeline.py's processes, from Kaggle integration via kagglehub to TF-IDF feature extraction.

Documentation of text_cleaner.py's regex-based pre-compilation technique for lightning-fast sanitization on large DataFrames.

Execution Instructions: Complete installation, dependency setup, and execution steps to boot up your Streamlit server.



