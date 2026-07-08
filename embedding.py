from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    dimensions=300

)

docs = [
    """New Delhi is the capital city of India and serves as the country's political and administrative center. It is home to important government buildings, historical landmarks such as India Gate and the Red Fort, and numerous museums. The city has a rich blend of modern infrastructure and ancient heritage, attracting millions of tourists every year.""",

    """Mumbai, located on the western coast of India, is the financial capital of the country. It is home to the Bombay Stock Exchange, numerous multinational companies, and the Bollywood film industry. The city is famous for landmarks like the Gateway of India, Marine Drive, and Chhatrapati Shivaji Maharaj Terminus.""",

    """Bengaluru, often called the Silicon Valley of India, is a major hub for information technology and innovation. It hosts the headquarters of many technology companies and startups. The city is also known for its pleasant climate, green parks such as Cubbon Park, and prestigious educational institutions.""",

    """Chennai is the capital of Tamil Nadu and is well known for its cultural heritage, classical music, and traditional dance forms. The city has one of the largest urban beaches in the world, Marina Beach, and serves as an important center for automobile manufacturing, healthcare, and higher education.""",


    """Kolkata, the capital of West Bengal, is often referred to as the City of Joy because of its vibrant culture and warm hospitality. The city is famous for the Howrah Bridge, Victoria Memorial, and its rich literary and artistic traditions. Kolkata is also renowned for its delicious cuisine, especially sweets like Rasgulla and Sandesh."""
]

results = embeddings.embed_documents(docs)
# print(results)

query = "What is the capital of India?"
query_embedding = embeddings.embed_query(query)

similarities = cosine_similarity([query_embedding], results)
print("Similarities:", similarities)

best_index = similarities.argmax()
print("Best Index")
print(docs[best_index])

print("Similarity Score")
print(similarities[0][best_index])  
