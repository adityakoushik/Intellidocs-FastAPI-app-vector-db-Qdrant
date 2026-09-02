from fastapi import FastAPI
from backend.db.qdrant import qdrant_client
from qdrant_client.models import Distance, VectorParams

# Now here creating object of FastAPI class
app = FastAPI(
    title="IntelliDocs API",
    description="AI-powered document knowledge base using Vector Database",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "IntelliDocs API is running"
    }
    
@app.get("/health")
def health_check():
    # Here we are checking the health of Qdrant Database by getting the collections from it.
    collections = qdrant_client.get_collections()
    return {
        "status": "healthy",
        "qdrant": "connected",
        "collections": len(collections.collections)
    }
    
@app.get("/collections")
def get_collections():
    collections = qdrant_client.get_collections()
    
    # collections_name = []
    # for collection in collections.collections:
    #     collections_name.append(collection.name)
    # return {
    #     "collections": collections_name
    # }
    
    # Now Using list comprehension in python to get the collections name from the collections object.
    return{
        "collections" : [
            collection.name for collection in collections.collections
        ]
    }
    
@app.post("/collections/documents")
def create_documents_collection():
    qdrant_client.create_collection(
        collection_name="documents",
        # VectorParams is decided that how the collection of vectors will be stored in the Qdrant database. It has two parameters size and distance. 
        # Size is the dimension of the vector and distance is the distance metric used to calculate the similarity between vectors.
        vectors_config = VectorParams(
            size = 3,
            distance = Distance.COSINE
        )
    )
    return {
        "message": "Documents collection created successfully"
    }