from openai import OpenAI
import sys
from pathlib import Path
from dotenv import load_dotenv
import os

# Get the root directory dynamically (assuming `gpt.py` is at the root)
project_root = Path(__file__).parent.parent  # Adjust if `gpt.py` isn't at the root
sys.path.append(str(project_root))

# Import the root script
import config

load_dotenv()
client = OpenAI(
  api_key= os.getenv("OPEN_AI_KEY")
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "developer", "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."},
    {"role": "user", "content": "I need a vanity size 24 with white color and a ceramic sink"},
    {"role": "assistant", "content": "vanity, size 24,  white color, ceramic sink,"},
    {"role": "user", "content": "build me a composition that have a vanity with 40 inches width with a side unit of 12 inches and a your cheapest washbasin"},
    {"role": "assistant", "content": "build, composition, vanity, 40 inches width, side unit, 12 inches, cheapest washbasin"},
    {"role": "user", "content": "do you have a pastel grey side unit?"},
  ]
)

print(completion.choices[0].message)
