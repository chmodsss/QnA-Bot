# Titanic Dataset AI Assistant 🚢🤖

## Project Overview
A simple LLM-powered assistant for exploring the Titanic dataset using Q&A.

## 🌟 Key Features
- **Natural Language SQL Querying**: Leverage Langchain's SQL Agent to query Titanic dataset
- **FastAPI Backend**: Robust Python-based API for data processing
- **Vue.js Frontend**: Reactive, modern web interface
- **SQLite Database**: Efficient data storage and retrieval

## 🛠 Tech Stack
- **Backend**: 
  - FastAPI
  - Langchain
  - SQLite
- **Frontend**: 
  - Vue.js 3
  - Axios
- **Data Processing**: 
  - Pandas
  - SQLAlchemy

## 📦 Prerequisites
- Python 3.9+
- Node.js 16+
- pip
- npm

## 🚀 Installation & Setup

### Environment Variables Setup
```
# In a bash terminal export them, or add them in .env file in backend directory
export OPENAI_API_KEY='your_openai_api_key'
export SQLITE_DB_PATH='path/to/titanic.db'
export TITANIC_CSV_PATH='path/to/titanic.csv'
```

### Backend Setup
```
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```


### Frontend Setup

```
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

## 🔧 Running the Application

### Start Backend (FastAPI)

```
# In backend directory
uvicorn main:app --reload
```

### Start Frontend (Vue.js)
```
# In frontend directory
npm run serve
```

## 💬 Usage

1. Launch the web application
2. Type natural language queries about the Titanic dataset
3. Receive instant, intelligent responses
