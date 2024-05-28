from dotenv import dotenv_values
from pathlib import Path

BASE_DIR = Path.cwd()
ENV_VARIABLES = {
    **dotenv_values(str(BASE_DIR / ".env")),  
    
}


OPENAI_API_KEY = ENV_VARIABLES["IGERENCIA_ALEGION_API"]