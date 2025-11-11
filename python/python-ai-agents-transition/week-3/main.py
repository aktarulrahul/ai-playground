# type: ignore
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import asyncio
import os
from dotenv import load_dotenv

# Import our LLM utilities
from llm_utils import (
    get_chat_response, get_embedding, count_tokens, chunk_text,
    test_chat, test_embedding, test_prompt_engineering, test_function_calling,
    test_chunking_and_embedding, find_similar_chunks, LLMError
)

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Week 3 - OpenAI SDK Integration", 
    version="1.0.0",
    description="FastAPI backend with OpenAI SDK integration for chat, embeddings, and prompt engineering"
)

# Pydantic models for request/response
class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    model: str = "gpt-4o-mini"
    temperature: float = 0.7

class ChatResponse(BaseModel):
    response: str
    usage: Optional[Dict[str, int]] = None

class EmbeddingRequest(BaseModel):
    text: str
    model: str = "text-embedding-3-small"

class EmbeddingResponse(BaseModel):
    embedding: List[float]
    dimensions: int
    usage: Optional[Dict[str, int]] = None

class ChunkingRequest(BaseModel):
    text: str
    max_tokens: int = 1000
    model: str = "gpt-4o-mini"

class ChunkingResponse(BaseModel):
    chunks: List[str]
    total_tokens: int
    chunk_tokens: List[int]

class SimilarityRequest(BaseModel):
    query: str
    chunks: List[str]
    top_k: int = 3

class SimilarityResponse(BaseModel):
    similar_chunks: List[Dict[str, Any]]

@app.get("/")
async def root():
    return {
        "message": "Week 3 - OpenAI SDK Integration", 
        "status": "running",
        "features": [
            "OpenAI Chat Completions",
            "OpenAI Embeddings", 
            "Prompt Engineering",
            "Function Calling",
            "Token-aware Chunking",
            "Vector Similarity Search"
        ]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "week": 3}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Chat completion endpoint"""
    try:
        response = await get_chat_response(
            messages=request.messages,
            model=request.model,
            temperature=request.temperature
        )
        return ChatResponse(response=response)
    except LLMError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.post("/embed", response_model=EmbeddingResponse)
async def embed_endpoint(request: EmbeddingRequest):
    """Text embedding endpoint"""
    try:
        embedding = await get_embedding(text=request.text, model=request.model)
        return EmbeddingResponse(
            embedding=embedding,
            dimensions=len(embedding)
        )
    except LLMError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.post("/chunk", response_model=ChunkingResponse)
async def chunk_endpoint(request: ChunkingRequest):
    """Text chunking endpoint"""
    try:
        total_tokens = count_tokens(request.text, request.model)
        chunks = chunk_text(request.text, request.max_tokens, request.model)
        chunk_tokens = [count_tokens(chunk, request.model) for chunk in chunks]
        
        return ChunkingResponse(
            chunks=chunks,
            total_tokens=total_tokens,
            chunk_tokens=chunk_tokens
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chunking error: {str(e)}")

@app.post("/similar", response_model=SimilarityResponse)
async def similarity_endpoint(request: SimilarityRequest):
    """Find similar chunks endpoint"""
    try:
        similar_chunks = await find_similar_chunks(
            query=request.query,
            chunks=request.chunks,
            top_k=request.top_k
        )
        return SimilarityResponse(similar_chunks=similar_chunks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Similarity search error: {str(e)}")

# Test endpoints
@app.get("/test/chat")
async def test_chat_endpoint():
    """Test basic chat functionality"""
    try:
        response = await test_chat()
        return {"test": "chat", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test/embedding")
async def test_embedding_endpoint():
    """Test basic embedding functionality"""
    try:
        embedding_length = await test_embedding()
        return {"test": "embedding", "embedding_length": embedding_length}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test/prompt-engineering")
async def test_prompt_engineering_endpoint():
    """Test prompt engineering with system/user roles"""
    try:
        response = await test_prompt_engineering()
        return {"test": "prompt_engineering", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test/function-calling")
async def test_function_calling_endpoint():
    """Test function calling (structured outputs)"""
    try:
        result = await test_function_calling()
        return {"test": "function_calling", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test/chunking-embedding")
async def test_chunking_embedding_endpoint():
    """Test chunking and embedding workflow"""
    try:
        result = await test_chunking_and_embedding()
        return {"test": "chunking_embedding", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tokens/{text}")
async def count_tokens_endpoint(text: str):
    """Count tokens in text"""
    try:
        token_count = count_tokens(text)
        return {"text": text, "tokens": token_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Environment check endpoint
@app.get("/env-check")
async def environment_check():
    """Check if OpenAI API key is configured"""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return {
            "openai_api_key": "configured",
            "key_length": len(api_key),
            "key_preview": api_key[:8] + "..." if len(api_key) > 8 else "***"
        }
    else:
        return {
            "openai_api_key": "not_configured",
            "message": "Please set OPENAI_API_KEY environment variable"
        } 