<h3 align="center">mini-RAG</h3>
<div align="center">
  
  [![GitHub contributors](https://img.shields.io/github/contributors/LamaMoustafa/mini-RAG)](https://github.com/LamaMoustafa/mini-RAG/contributors)
  [![GitHub forks](https://img.shields.io/github/forks/LamaMoustafa/mini-RAG)](https://github.com/LamaMoustafa/mini-RAG/network)
  [![GitHub stars](https://img.shields.io/github/stars/LamaMoustafa/mini-RAG)](https://github.com/LamaMoustafa/mini-RAG/stargazers)
  [![GitHub license](https://img.shields.io/github/license/LamaMoustafa/mini-RAG)](https://github.com/LamaMoustafa/mini-RAG/blob/main/LICENSE)
  <img src="https://img.shields.io/github/languages/count/LamaMoustafa/mini-RAG" />
  <img src="https://img.shields.io/github/languages/top/LamaMoustafa/mini-RAG" />

</div>

## Table of Contents

- [About the Project](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Running](#running)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Important Note
> This is a work-in-progress implementation of the RAG model for question answering. Feedback is welcome to help improve it!

## About

**mini-RAG** is a minimal implementation of the Retrieval-Augmented Generation (RAG) model designed to demonstrate question-answering capabilities by combining information retrieval with generative responses.

### Built With
- [Python 3.8+](https://www.python.org/)
- [FAISS](https://github.com/facebookresearch/faiss) - For efficient similarity search and clustering
- [Transformers](https://huggingface.co/transformers) - For model handling

## Getting Started

To set up this project locally, follow these steps.

### Requirements

- **Python 3.8** or later

#### Install Python using MiniConda

1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install).
2. Create a new environment:

    ```bash
    conda create -n mini-rag python=3.8
    ```

3. Activate the environment:

    ```bash
    conda activate mini-rag
    ```

### Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/LamaMoustafa/mini-RAG.git
    ```

2. **Navigate to the project directory**

    ```sh
    cd mini-RAG
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```
4. **Setup the environment variables**

    ```sh
    cp .env.example .env
    ```

set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

### Running

1. **Start the FastAPI server**

    ```sh
    uvicorn main:app --reload
    ```
### Postman Collection

To test the API endpoints with Postman, download the Postman collection from the [assets folder](https://github.com/LamaMoustafa/mini-RAG/blob/main/assets/mini-RAG.postman_collection.json).

## Features

- Retrieval and Generation-based Question Answering
- Simple architecture for demonstration and experimentation

## Contributing

Contributions are welcome! Please:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/LamaMoustafa/mini-RAG/blob/main/LICENSE) file for more details.
