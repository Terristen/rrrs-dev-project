from dotenv import load_dotenv
load_dotenv()  # Load environment variables first

import openai
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

from utils import debug_print

class APIInteraction:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        openai.base_url = os.getenv("OPENAI_API_BASE")

    def send_prompt(self, prompt, max_tokens=100, temperature=0.7):
        try:
            response = openai.chat.completions.create(
                model="text-davinci-003",  # Placeholder for your server's model
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                          {"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return "An error occurred while processing your request."

    async def send_prompt_async(self, prompt, max_tokens=100, temperature=0.7):
        loop = asyncio.get_event_loop()
        # Use ThreadPoolExecutor to run the synchronous OpenAI call in a separate thread
        with ThreadPoolExecutor() as pool:
            try:
                response = await loop.run_in_executor(
                    pool,
                    lambda: openai.chat.completions.create(
                        model="text-davinci-003",  # Ensure you're using the correct model for your setup
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=max_tokens,
                        temperature=temperature
                    )
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                print(f"An error occurred: {e}")
                return "An error occurred while processing your request."

