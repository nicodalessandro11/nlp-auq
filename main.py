import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFacePipeline
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.prompts import PromptTemplate
from huggingface_hub import login
from transformers import pipeline

# 1. Load environment variables
load_dotenv()
SUPABASE_URI = os.getenv("SUPABASE_URI")
HF_TOKEN = os.getenv("HF_TOKEN")

# 2. Log in to Hugging Face
login(token=HF_TOKEN)

# 3. Load DeepSeek model from Hugging Face
pipe = pipeline(
    "text-generation",
    model="deepseek-ai/deepseek-coder-6.7b-instruct",
    max_new_tokens=512,
    temperature=0.3,
)

llm = HuggingFacePipeline(pipeline=pipe)

# 4. Connect to Supabase PostgreSQL database
db = SQLDatabase.from_uri(SUPABASE_URI)

# 5. Load custom prompt
with open("custom_prompt.txt", "r") as f:
    prompt_content = f.read()

custom_prompt = PromptTemplate.from_template(prompt_content)

# 6. Create agent with custom prompt
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True, prompt=custom_prompt)

# 7. Example natural language question
question = "Where do more young people live in Barcelona?"
response = agent.run(question)

print("\n🧠 Agent response:\n", response)
