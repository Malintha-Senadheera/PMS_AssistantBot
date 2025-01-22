import os
import json
import requests
from dotenv import *

# Load environment variables
load_dotenv()

# Load Notion API token
NOTION_API_TOKEN = os.getenv("NOTION_TOKEN")

# Notion headers
headers = {
    "Authorization": "Bearer " + NOTION_API_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}