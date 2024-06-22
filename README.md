# Text Summarizer
This project implements a text summarization system using the Samsum dataset. The system is built with Python, utilizing the Hugging Face Transformers library and a Pegasus model fine-tuned on the Samsum dataset. The project includes data ingestion, data transformation, model training, and a Flask web application for text summarization.

## Table of Contents
- [Project Description](#project-description)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Description
This Text Summarizer project aims to generate concise and coherent summaries of dialogues. The Samsum dataset, which contains chat dialogues and their corresponding summaries, is used to train a Pegasus model. The project is divided into several modules:
1. *Data Ingestion*: Downloads and extracts the dataset.
2. *Data Transformation*: Prepares the data for training.
3. *Model Trainer*: Fine-tunes the Pegasus model on the prepared dataset.
4. *Flask App*: Provides a web interface to input text and get summaries.

## Setup Instructions
### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/text-summarizer.git
    cd text-summarizer
    ```
    

3. **Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
     ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt`
     ```

7. Set up the project structure and download the dataset:
    ```bash
    python src/data_ingestion.py
     ```

9. Transform the data:
    ```bash
   python src/data_transformation.py
     ```
    
11. Train the model:
    ```bash
    python src/model_trainer.py
     ```

13. Run the Flask web application:
    ```bash
    python app.py
     ```

## Usage

To use the web application, follow these steps:

1. Navigate to the URL provided by the Flask app, typically `http://0.0.0.0:5000`.
2. Enter the dialogue text you want to summarize in the input field.
3. Click the "Summarize" button to get the summary.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions.
