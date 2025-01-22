# AI_contract_checker

Project Description
This project is an AI-powered tool designed to automate the process of regulatory compliance checks for contracts. It extracts text from contract documents, processes the text into manageable chunks, generates embeddings using advanced NLP models, and performs similarity matching to identify compliance gaps. The system leverages Pinecone for vector storage and query matching.

Features
PDF Ingestion: Upload and extract text from PDF contracts.
Text Chunking: Split large text into manageable chunks for analysis.
Embedding Generation: Create vector representations of text using pre-trained NLP models.
Vector Storage: Store embeddings in Pinecone for efficient querying.
Compliance Query: Match user queries with stored embeddings to identify compliance gaps.
Technologies Used
Programming Language: Python
Frameworks and Libraries:
langchain for text processing and embeddings.
PyPDF2 for PDF text extraction.
sentence-transformers for embeddings.
pinecone-client for vector storage and retrieval.
dotenv for managing environment variables.
Database: Pinecone
Deployment: Can be containerized with Docker.
