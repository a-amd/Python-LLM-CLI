# Python Command Line Interface (CLI) for the Large Language Models

## Description

This is a Python Command Line Interface (CLI) for Large Language Models. It is meant to be used as a
wrapper around accessing large language models, such as GPT-2, GPT-3, and BERT via public APIs. It is meant to be used as a standalone application from the standard web applications.

So far it supports OpenAI's models, but it can be extended to support other models as well.

## Setup

Get an API key from your AI provider of choice. Currently, only OpenAI is supported. You can get an API key from [OpenAI](https://openai.com/).

Create a .env file in the root directory of the project and add the following:

```.env
OPENAI_API_KEY=<your-api-key>
```

Install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 app.py --help
```

## Using Docker Build to Create an Image and Run the Container

```bash
docker build -t python-chat-cli .
docker run -it --rm --name python-chat-cli python-chat-cli
```
