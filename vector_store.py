from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()

doc1 = Document(
    page_content="Albert Einstein was a theoretical physicist known for developing the theory of relativity, one of the two pillars of modern physics.",
    metadata={"field": "Physics", "country": "Germany"}
)

doc2 = Document(
    page_content="Mahatma Gandhi was a leader of India’s non-violent independence movement against British rule and is celebrated for his philosophy of peaceful resistance.",
    metadata={"field": "Politics", "country": "India"}
)

doc3 = Document(
    page_content="Marie Curie was a pioneering scientist who conducted groundbreaking research on radioactivity and was the first woman to win a Nobel Prize.",
    metadata={"field": "Chemistry", "country": "Poland"}
)

doc4 = Document(
    page_content="Leonardo da Vinci was a Renaissance artist and inventor, best known for masterpieces like the Mona Lisa and The Last Supper.",
    metadata={"field": "Art", "country": "Italy"}
)

doc5 = Document(
    page_content="Martin Luther King Jr. was an American civil rights leader who advocated for equality through non-violent civil disobedience.",
    metadata={"field": "Civil Rights", "country": "USA"}
)

docs=[doc1,doc2,doc3,doc4,doc5]

vector_store=Chroma(
  embedding_function = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY")), # which embedding model is used 
  persist_directory='my_file_db', #directory in which all embedding vectors will be stores
  collection_name='sample' #collection inside the directory
)
#add documents
vector_store.add_documents(docs)

#view documents (includes will print all the included element from docs)
# print(vector_store.get(include=['embeddings','documents','metadatas']))

#search documents
# print(vector_store.similarity_search(
#   query='Who among these are a physicist',
#   k=2 # number of outcome you want (means if there are 3 physicist then 2 with high similarity score will be returned as k is 2
# ))

# # search with similarity score. This will print the same as above but with similarity score
# print(vector_store.similarity_search_with_score(
#     query='Who among these are a physicist',
#     k=2
# ))

# #meta data filtering
# vector_store.similarity_search_with_score(
#   query="",
#   filter={'country': 'India'}
# )

# #updating document
# updated_doc1 = Document(
#     page_content="Albert Einstein revolutionized modern physics with his contributions to quantum mechanics and the theory of general relativity. Beyond science, he was a passionate advocate for civil rights and a vocal critic of authoritarianism.",
#     metadata={"field": "Physics", "country": "Germany", "notable_for": "Relativity & Humanitarianism"}
# )

# print(vector_store.update_document(
#     document_id="08a39dc6-3ba6-4ea7-927e-fdda501da5e4",
#     document=updated_doc1
# ))

#delete document
# vector_store.delete(ids=['01a39dc6-3ba6-4ea9-927e-fdda591da5e4'])

