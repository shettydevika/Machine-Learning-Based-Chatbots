# Machine Learning-Based Chatbot

A chatbot built using machine learning and natural language processing (NLP) techniques. This project uses Python, TensorFlow, scikit-learn, NLTK, and SpaCy to create a chatbot capable of understanding and responding to user queries.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description

This chatbot is designed to assist users with tasks like booking appointments, answering FAQs, or providing recommendations. The bot leverages machine learning models to understand and process natural language inputs, providing accurate and relevant responses.

## Technologies Used

- **Programming Language**: Python
- **Machine Learning**: TensorFlow, Keras, scikit-learn
- **Natural Language Processing**: NLTK, SpaCy
- **Data Handling**: Pandas
- **Development Environment**: Visual Studio Code

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/shettydevika/Machine-Learning-Based-Chatbots.git
   cd Machine-Learning-Based-Chatbots

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt

4. **Prepare the data**:
   
   Place your data.csv file in the chatbot directory. Ensure it is correctly formatted according to the project specifications.

## Usage

To use the chatbot, follow these steps:

1. **Data Preprocessing**:
   Start by preprocessing the data to prepare it for model training.

   ```sh
   python chatbot/data_preprocessing.py

This script reads the data.csv file, processes the text data (such as tokenization and vectorization), and saves the cleaned data for model training.

2. **Train the Model**:
   Train the machine learning model using the preprocessed data. This step involves defining and training the model architecture.
      ```sh
      python chatbot/train_model.py

This script will:

- **Load the preprocessed data.**
- **Define the neural network architecture using TensorFlow and Keras.**
- **Train the model on the dataset.**
- **Save the trained model to a file for later use.**

3. **Start the Chatbot**:
   After training the model, you can start the chatbot interface. 

   ```sh
   python chatbot/chatbot.py

4. **Interacting with the Chatbot**:
   Once the appropriate interface is running, you can begin interacting with the chatbot. Use natural language queries to ask questions or make requests, and the chatbot will respond accordingly.

5. **Customization and Extensions**:
You can customize the chatbot's behavior, improve its accuracy, or add new features by:

- **Modifying the data.csv file with new queries and responses.**
- **Updating the data preprocessing steps or model architecture.**
- **Enhancing the NLP capabilities with additional libraries or techniques.**

## Data

The data.csv file contains the training data for the chatbot. The file should be structured with two columns:

- **query: The user input or question.**
- **response: The chatbot's response.**

Example:
     
            query,response
            "What is your name?", "I am a chatbot created to assist you."
            "Where are you located?", "We are located at 123 Main Street, Anytown, USA."


## Model Training

To train the chatbot's machine learning model, use the provided training scripts. Details on model architecture and training procedures can be found in the training directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

Thanks to the open-source community for providing the tools and libraries that made this project possible.
