import nltk

# Make sure your NLTK looks in your virtual environment folder
nltk_data_dir = r'D:\AI\nlp_env\nltk_data'
nltk.data.path = [nltk_data_dir] + nltk.data.path

# Download the correct POS tagger
nltk.download('averaged_perceptron_tagger_eng', download_dir=nltk_data_dir)