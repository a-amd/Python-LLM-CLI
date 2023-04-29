#!/usr/bin/env python3

# import OpenAI chatbot
from openai_api import GPT35Turbo
from colorama import Fore, Style

# list of exit words to stop the program
exit_words = ["exit", "quit", "stop", "bye", "goodbye", "done", "end"]

gpt = GPT35Turbo()

def prompt_loop():
    while True:
        # Take user input
        prompt = input(f"\n{Fore.BLUE}input >{Style.RESET_ALL} ")

        # ignore empty input and clear the current line
        if len(prompt.strip()) == 0:
            print("\r", end="")
            continue
        
        # check exit words
        if prompt.lower() in exit_words:
            break

        # generate the token length
        user_input = prompt.strip()
        #print(f"User Input: {user_input}, prompt: {prompt}")

        token_length = gpt.generate_token_length(user_input)

        if(token_length < 10):
            print(f"{Fore.RED}Token length is too short, please try again. {Style.RESET_ALL}")
            continue

        response = gpt.generate_text(user_input)
        print(f"\n{Fore.CYAN}GPT-3.5-Turbo >{Style.RESET_ALL}\n{Fore.GREEN}{response}{Style.RESET_ALL}")

# setup the main method
def main():
    prompt_loop()

# call the main method
if __name__ == "__main__":
    main()