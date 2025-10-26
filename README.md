📑 Project Proposal: Programming Language Classification from Code Snippets

🎯 Objective
The goal of this project is to build an NLP-based system that automatically classifies the programming language of a given code snippet. This system will help in tasks such as code search, plagiarism detection, and organizing large repositories of mixed-language code.

🧩 Problem Statement
With the rapid growth of open-source projects and online coding platforms, developers often encounter code snippets without clear language labels. Manually identifying the language is inefficient and error-prone. Our project addresses this by training machine learning and deep learning models to automatically detect the programming language from raw code.

🛠️ Methodology

1. Dataset
- Use publicly available datasets we used  Kaggle’s Programming Language Classification datasets.
- Each snippet will be labeled with its programming language.
- FIND THE DATASET FROM THE LINK DRIVE
- https://drive.google.com/drive/u/0/folders/1mFji6jasE_mRvx_S2wt0qWxoMvYBtJtZ
  
2. Preprocessing
- Clean code (remove comments, normalize whitespace).
- Tokenize code (identifiers, keywords, operators).
- Feature extraction:
- TF-IDF (character n-grams for language detection).
- Word embeddings (optional for neural networks).
3. Models
We will train and compare 6 models:
we choose the 6 models we will do a vote


(If you want to stick strictly to 6 models, use the 4 ML + 2 neural networks. If you want to extend, add transformers as bonus models.)
4. Evaluation
- Metrics: Accuracy, F1-score, confusion matrix.
- Compare models on the same test set.
5. Deployment
- Build a simple web interface where users paste a code snippet and get the predicted programming language.

📊 Visualization Plan
Visualization will be used in two phases:
1\Problem Exploration Phase:
- Show dataset distribution (bar chart of languages).
- Example snippets per language.
- Token frequency visualization (word cloud or bar chart of keywords).
2\ Model Comparison Phase:
- Confusion matrices for each model.
- Bar charts comparing accuracy/F1 across models.
- Training curves (for neural networks).
- Radar chart comparing models on multiple metrics (accuracy, F1, training time).
Tools: Matplotlib, Seaborn, Plotly, Yellowbrick.


🚀 FINALY 
what will get ?
- A trained system that can accurately classify the programming language of unseen code snippets.
- A comparative study of 6 models, highlighting trade-offs between classical ML, neural networks, and transformers.
what we will add ?
- A web-APP demo showcasing real-time predictions.
- Clear visualizations of dataset insights and model performance.

- here is a web app that can be really good with our project  it is just a demo used gemini ai to do it  https://gemini.google.com/share/b1a880c72e05
