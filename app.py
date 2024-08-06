import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Title of the application
st.title("Next Word Prediction With LSTM")
st.text('Hello')

# Loading the model
model = load_model('lstm_model.h5')

# Loading the tokenizer
tokenizer = pickle.load(open('tokenizer.pickle', 'rb'))

# Function to predict the next word
def prediction_model(model, tokenizer, input_text, max_seq_len):
    input_text = input_text.lower()
    token_list = tokenizer.texts_to_sequences([input_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_seq_len-1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted = np.argmax(predicted, axis=1)
    output_word = ''
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    return output_word

# Maximum length of the sequence
max_length = 500
max_seq = model.input_shape[1] + 1

# Input text from user
input_text = st.text_input("Enter the text:", "")

# Prediction and display
if st.button("Predict Next Word"):
    if input_text:
        next_word = prediction_model(model, tokenizer, input_text, max_length)
        st.write(f"Input Text: {input_text}")
        st.write(f"Next Word Prediction: {next_word}")
    else:
        st.write("Please enter some text to predict the next word.")
