from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)
# files = client.files.list()

# file = client.files.create(
#   file=open("unsu.pdf", "rb"),
#   purpose="assistants"
# )

#file_ids file-XxL3eqQKHgXq3pMttYEu43

my_assistant = client.beta.assistants.create(
    instructions="당신은 소설 운수 좋은 날을 집필한 현진건 작가입니다.",
    name="현진건 작가님2",
    model="gpt-4o",
    # 사용하고자 하는 툴 설정
    tools=[
        {"type": "file_search", "knowledge_files": ["file-XxL3eqQKHgXq3pMttYEu43"]}
    ]
)

file = client.files.retrieve("file-XxL3eqQKHgXq3pMttYEu43")
print(file)

