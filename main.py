from dotenv import load_dotenv
from src.controllers.ingestion_controller import IngestionController
from src.controllers.chunk_controller import ChunkController
from src.controllers.embedding_controller import EmbeddingController
from src.Services.pinecone_service import PineconeService
import os

# Load environment variables
load_dotenv()

def main():
    # Initialize controllers
    ingestion_controller = IngestionController()
    chunk_controller = ChunkController()
    embedding_controller = EmbeddingController()
    pinecone_service = PineconeService()

    # PDF File Path
    file_path = "data/sample_contract.pdf"

    # Step 1: Extract Text from PDF
    extracted_text = ingestion_controller.process_pdf(file_path)
    if not extracted_text:
        print("No text extracted from the PDF. Exiting.")
        return

    # Step 2: Split Text into Chunks
    text_chunks = chunk_controller.split_text_into_chunks(extracted_text)

    # Step 3: Generate Embeddings for Chunks
    embeddings = embedding_controller.generate_embeddings(text_chunks)

    # Step 4: Store Embeddings in Pinecone
    for i, embedding in enumerate(embeddings):
        pinecone_service.upsert_embedding(
            id=f"chunk_{i}",
            embedding=embedding,
            metadata={"text": text_chunks[i]}
        )

    print("Embeddings have been stored successfully.")

    # Example Query
    query = "Check for GDPR compliance."
    query_embedding = embedding_controller.generate_embedding(query)
    results = pinecone_service.query(query_embedding, top_k=5)

    # Display Results
    for match in results["matches"]:
        print(f"Match: {match['metadata']['text']} (Score: {match['score']})")

if __name__ == "__main__":
    main()
