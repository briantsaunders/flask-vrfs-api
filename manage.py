# import std libs
import os

# import third party libs
from dotenv import load_dotenv

# import app libs
from app import create_app

load_dotenv()

app = create_app(os.getenv("FLASK_ENV", "default"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
