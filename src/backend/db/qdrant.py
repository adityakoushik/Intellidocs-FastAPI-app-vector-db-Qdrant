from qdrant_client import QdrantClient

# Here qdrant client is python client which is used to connect with Qdrant Database.
qdrant_client = QdrantClient(
    url = "http://localhost:6333/"
)