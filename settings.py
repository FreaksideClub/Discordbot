import os
from dotenv import load_dotenv

DEBUG = os.getenv("DEBUG", True)

if DEBUG:
    print("We are in debug")
    from pathlib import Path
    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)
    from config.development import *
else:
    print("We are in production")
    from pathlib import Path
    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)
    from config.product import *
