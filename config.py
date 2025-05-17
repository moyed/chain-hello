import os
from dotenv import load_dotenv, find_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables
load_dotenv(find_dotenv())
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup provider and model
provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GEMINI_API_KEY
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# Run configuration
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)
