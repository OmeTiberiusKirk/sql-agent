import os
from dotenv import load_dotenv
import psycopg2
from ollama import chat
from ollama import ChatResponse


load_dotenv()


class AIAgent:
    def __init__(self):
        # Database connection
        self.db_connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        self.create_tables()
        self.insert_documents()

    def create_tables(self):
        """Ensure required tables exist"""
        with self.db_connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS documents (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    content TEXT,
                    embedding VECTOR(384)
                );
                """
            )
            self.db_connection.commit()

    def insert_documents(self):
        cur = self.db_connection.cursor()
        cur.execute("SELECT COUNT(*) from documents")
        if cur.fetchone()[0]:
            print(cur.fetchone()[0])

    def generate_response(self, user_input: str):
        stream = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
            stream=True,
        )

        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)

        print("\n")

    def close(self):
        """Clean up resources"""
        self.db_connection.close()


documents = [
    {
        "title": "Seoul Tower",
        "content": "Seoul Tower is a communication and observation tower located on Namsan Mountain in central Seoul, South Korea.",
    },
    {
        "title": "Gwanghwamun Gate",
        "content": "Gwanghwamun is the main and largest gate of Gyeongbokgung Palace, in Jongno-gu, Seoul, South Korea.",
    },
    {
        "title": "Bukchon Hanok Village",
        "content": "Bukchon Hanok Village is a Korean traditional village in Seoul with a long history.",
    },
    {
        "title": "Myeong-dong Shopping Street",
        "content": "Myeong-dong is one of the primary shopping districts in Seoul, South Korea.",
    },
    {
        "title": "Dongdaemun Design Plaza",
        "content": "The Dongdaemun Design Plaza is a major urban development landmark in Seoul, South Korea.",
    },
]
