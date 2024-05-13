from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import pandas as pd

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

my_assistant = client.beta.assistants.create(
    instructions="You are an HR bot, and you have access to files to answer employee questions about company policies.",
    name="HR Helper",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "Function1",
                "description": "A description of what Function1 does",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test": {
                            "type": "string",
                            "description": "A string parameter for Function1"
                        }
                    },
                    "required": ["test"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "Function2",
                "description": "A description of what Function2 does",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test2": {
                            "type": "string",
                            "description": "A string parameter for Function2"
                        },
                        "test3": {
                            "type": "integer",
                            "description": "An integer parameter for Function2"
                        }
                    },
                    "required": ["test2", "test3"]
                }
            }
        }
    ],
    model="gpt-4-turbo",
    temperature=0.7,
    response_format={ "type": "json_object" } 
)
print(my_assistant)