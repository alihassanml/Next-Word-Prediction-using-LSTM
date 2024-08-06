# Next Word Prediction using LSTM

This repository contains a Streamlit application for predicting the next word in a given text input using an LSTM model. The application leverages TensorFlow and a pre-trained LSTM model to generate word predictions.

## Features

- **User Input:** Enter a partial sentence or phrase to get a prediction for the next word.
- **Real-time Prediction:** The application provides real-time predictions based on the input text.
- **Streamlit Interface:** Easy-to-use web interface built with Streamlit.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7 or later
- TensorFlow
- Streamlit
- Numpy
- Pickle

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/alihassanml/next-word-prediction-using-lstm.git
    cd next-word-prediction-using-lstm
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the `lstm_model.h5` and `tokenizer.pickle` files are in the root directory of the project.

### Running the Application

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can interact with the application through your web browser.

## Usage

1. Open the application in your web browser.
2. Enter a partial sentence or phrase in the input text box.
3. Click the "Predict Next Word" button to get the predicted next word.
4. The predicted next word will be displayed below the input box.

## File Structure

- `app.py`: The main Streamlit application file.
- `lstm_model.h5`: The pre-trained LSTM model file.
- `tokenizer.pickle`: The tokenizer used to preprocess the text data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [Numpy](https://numpy.org/)

## Contact

For any questions or suggestions, feel free to contact me at [alihassanml](https://alihassanml.vercel.app/)
