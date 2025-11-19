# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Key
# The API key is loaded from the .env file.
# Make sure to create a .env file with your API key.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Database Settings
# Define the path and name for your SQLite database.
DATABASE_NAME = "civic_pulse.db"
