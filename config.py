from dotenv import dotenv_values
from pathlib import Path
import os

# BASE_DIR = Path.cwd()
# ENV_VARIABLES = {
#     **dotenv_values(str(BASE_DIR / ".env")),  
    
# }
# OPENAI_API_KEY = ENV_VARIABLES["IGERENCIA_ALEGION_API"]

# if ENV_VARIABLES:
#     print("cargó")
# else:
#     OPENAI_API_KEY = os.getenv("IGERENCIA_ALEGION_API")
#     print("tocó OS")
    

OPENAI_API_KEY = os.getenv("IGERENCIA_ALEGION_API")