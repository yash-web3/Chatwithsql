# Chatwith Database POC

## Overview
This project is a proof-of-concept (POC) application that allows users to interact with a SQLite database using natural language queries. The application utilizes Google's Gemini API for natural language processing (NLP) to convert English questions into SQL queries, which are then executed on a SQLite database containing information about Classic Models, a fictional company with offices worldwide.

## Features
- **Natural Language Processing:** Users can input English questions related to the database, and the application will generate corresponding SQL queries.
- **Database Integration:** The application interacts with a SQLite database named `ClassicModels.db`, which contains information about Classic Models, its employees, and customers.
- **Streamlit UI:** The user interface is built using Streamlit, providing a simple and intuitive experience for users to input questions and view database details.

## Project Structure
- `main.py`: The main Python script containing the Streamlit application code.
- `ClassicModels.db`: SQLite database file containing the company's information.
- `Gemini.py`: Module for interfacing with Google's Gemini API for NLP.
- `requirements.txt`: List of Python dependencies required to run the project.

## Setup
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/chatwith-database-poc.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Obtain a Google API key for Gemini API and set it as `GOOGLE_API_KEY` in your environment variables.

4. Run the application:

    ```bash
    streamlit run main.py
    ```

## Usage
1. Upon running the application, you will be presented with a user interface.
2. Enter your English query in the input field provided.
3. Click on the "Ask the question" button to generate the corresponding SQL query.
4. The generated SQL query will be displayed, and the database details corresponding to the query will be shown below.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
