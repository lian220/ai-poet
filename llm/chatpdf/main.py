from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

#Loader
loader = PDFPlumberLoader("unsu.pdf")
pages = loader.load_and_split()


#Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
    length_function = len,
    is_separator_regex = False,
)
texts = text_splitter.split_documents(pages)
print(texts[0])

#Embedding
embeddings_model = OpenAIEmbeddings()

# load it into Chroma
db = Chroma.from_documents(texts, embeddings_model)

#Question
question = "아내가 먹고 싶어하는 음식은 무엇이야?"
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm,retriever=db.as_retriever())
result = qa_chain({"query": question})
print(result)
