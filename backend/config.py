"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "meta-llama/llama-4-maverick",
    "x-ai/grok-4.1-fast",
    "deepseek/deepseek-chat-v3.1",
    "qwen/qwen2.5-vl-3b-instruct"
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "x-ai/grok-4.1-fast"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
