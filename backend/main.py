import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.sqlprocessor import SQLProcessor

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.post("/api/chat")
async def process_chat(request: ChatRequest):
    processor = SQLProcessor(file_path=os.getenv('TITANIC_CSV_PATH'),
                             sql_path=os.getenv('SQLITE_DB_PATH'))
    is_db = processor.db_exists()
    if not is_db:
        processor.to_sql()
    response = processor.run_agent(request.message)
    return {"message": response['output']}
