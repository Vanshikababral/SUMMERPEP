from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader("Sample_doc/", glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True)
documents = loader.lazy_load()

# print(f"Number of Documents: {len(documents)}")

for idx, document in enumerate(documents, start=1):
    print(f"\nDocument {idx}")
    print("Content:\n", document.page_content)
    print("Metadata:\n", document.metadata)

