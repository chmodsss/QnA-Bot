import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy.engine import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


class SQLProcessor:
    def __init__(self, file_path, sql_path):
        self.sql_path = sql_path
        self.file_path = file_path
        self.engine = create_engine(f"sqlite:///{self.sql_path}")

    def db_exists(self):
        if os.path.exists(self.sql_path):
            return True
        else:
            return False

    def to_sql(self):
        df = pd.read_csv(self.file_path)
        table_name = os.path.basename(self.file_path).split(".")[0]
        try:
            df.to_sql(table_name, self.engine, index=False)
            return True
        except ValueError as e:
            print(e)
            return False

    def process(self):
        self.db = SQLDatabase(engine=self.engine)
        table_names = self.db.get_usable_table_names()
        print(f"Table names : {table_names}")
        return table_names

    def run_db(self, query):
        self.db = SQLDatabase(engine=self.engine)
        return self.db.run(query)

    def run_agent(self, user_input):
        self.db = SQLDatabase(engine=self.engine)
        llm = ChatOpenAI()
        agent = create_sql_agent(
            llm=llm, db=self.db, agent_type="openai-tools", verbose=False
        )
        result = agent.invoke({"input": user_input})
        print(f"Result : {result}")
        return result

    def run_chain(self):
        pass
