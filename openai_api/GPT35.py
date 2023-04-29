# Class file openai\GPT35.py that contains the GPT3.5-turbo class.
# This class is used to generate responses from the GPT-3.5 Turbo model.
# Should export the class as a python module using the __init__.py file.

# Import the required modules
import random
import os
import openai
from dotenv import load_dotenv

# Define the minimum and maximum token lengths
MIN_TOKENS = 10
MAX_TOKENS = 2048

# Define temperature constant
TEMPERATURE = 0.9

# Define the GPT-3.5 Turbo model
# Allows for easy changing of the model
MODEL = "gpt-3.5-turbo"

# Load the .env file
load_dotenv()
# Get API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the GPT3.5-turbo class
class GPT35Turbo:
    """
    The GPT-3.5 Turbo class that is used to generate responses from the GPT-3.5 Turbo model.
    This python class is exported as a module using the __init__.py file.
    """

    def __init__(self) -> None:
        self.prompt = "" # initialize the prompt to an empty string
        self.response = "" # initialize the response to an empty string
        self.token_length = 0 # initialize the token length to 0
        self.temperature = TEMPERATURE # initialize the temperature to the constant
        self.stop = "\n" # initialize the stop to a new line
        self.model = MODEL # set the model to the GPT-3.5 Turbo model

    def generate_text(self, prompt: str) -> str:
        """
        Generate a response from the GPT-3.5 Turbo model.

        Args:
            prompt (str): The prompt to generate the response for.\n
            token_length (int): The length of the token prompt.

        Returns:
            str: The response from the GPT-3.5 Turbo model.
        """
        self.prompt = prompt # Set the prompt

            # Generate the response
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=self.token_length,
        )

        self.response = response["choices"][0]["message"]["content"] # Set the response
        return self.response # Return the response
    
    def generate_token_length(self, prompt: str) -> int:
        """
        Generate the length of the token prompt that is porportional to the length of the prompt.

        Args:
            prompt (str): The prompt to generate the token length for.\n
            max_tokens (int): The maximum number of tokens to generate.

        Returns:
            int: The length of the token prompt.
        """
        self.prompt = prompt # Set the prompt

        min_tokens = int(len(prompt) * 0.075) + MIN_TOKENS # Add minimum tokens to the 0.075 of the prompt length
        prompt_propotion = len(prompt) / MAX_TOKENS # Get the proportion of the prompt length to the maximum tokens
        proportial_tokens = round(MAX_TOKENS * prompt_propotion) # Get the proportial tokens

        min_tokens = min(MIN_TOKENS, proportial_tokens) # Get the minimum tokens
        proportial_tokens = max(MAX_TOKENS, proportial_tokens) # Get the maximum tokens

        self.token_length = random.randint(min_tokens, proportial_tokens) # Set the token length
        return self.token_length # Return the token length