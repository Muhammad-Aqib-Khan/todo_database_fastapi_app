from sqlmodel import SQLModel, create_engine
import os

# Load the environment variables
from dotenv import load_dotenv
load_dotenv()

# Fetch the connection string from the environment variable
connection_string = os.getenv('DB_URI')
print(f"Database connection string: {connection_string}")

# Create the database engine
engine = create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully.")
