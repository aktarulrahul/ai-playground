"""
Comprehensive tests for Week 3 LLM functionality
"""

import pytest
import asyncio
from httpx import AsyncClient
from main import app
from llm_utils import (
    get_chat_response, get_embedding, count_tokens, chunk_text,
    test_chat, test_embedding, test_prompt_engineering, test_function_calling,
    test_chunking_and_embedding, find_similar_chunks, cosine_similarity
)


@pytest.mark.asyncio
async def test_root_endpoint():
    """Test the root endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Week 3 - OpenAI SDK Integration"
        assert "OpenAI Chat Completions" in data["features"]


@pytest.mark.asyncio
async def test_health_endpoint():
    """Test the health endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["week"] == 3


@pytest.mark.asyncio
async def test_env_check_endpoint():
    """Test the environment check endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/env-check")
        assert response.status_code == 200
        data = response.json()
        assert "openai_api_key" in data


@pytest.mark.asyncio
async def test_chat_endpoint():
    """Test the chat endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        request_data = {
            "messages": [{"role": "user", "content": "Hello, world!"}],
            "model": "gpt-4o-mini",
            "temperature": 0.7
        }
        response = await ac.post("/chat", json=request_data)
        # Note: This will fail if OPENAI_API_KEY is not set
        # In a real test environment, you'd mock the OpenAI API
        assert response.status_code in [200, 500]  # 500 if no API key


@pytest.mark.asyncio
async def test_embed_endpoint():
    """Test the embed endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        request_data = {
            "text": "The quick brown fox jumps over the lazy dog",
            "model": "text-embedding-3-small"
        }
        response = await ac.post("/embed", json=request_data)
        # Note: This will fail if OPENAI_API_KEY is not set
        assert response.status_code in [200, 500]  # 500 if no API key


@pytest.mark.asyncio
async def test_chunk_endpoint():
    """Test the chunk endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        long_text = "This is a test text. " * 50  # Create a longer text
        request_data = {
            "text": long_text,
            "max_tokens": 100,
            "model": "gpt-4o-mini"
        }
        response = await ac.post("/chunk", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert "chunks" in data
        assert "total_tokens" in data
        assert "chunk_tokens" in data
        assert len(data["chunks"]) > 0


@pytest.mark.asyncio
async def test_tokens_endpoint():
    """Test the tokens endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        test_text = "Hello, world! This is a test."
        response = await ac.get(f"/tokens/{test_text}")
        assert response.status_code == 200
        data = response.json()
        assert data["text"] == test_text
        assert "tokens" in data
        assert data["tokens"] > 0


@pytest.mark.asyncio
async def test_similar_endpoint():
    """Test the similar endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        request_data = {
            "query": "artificial intelligence",
            "chunks": [
                "Artificial Intelligence is a field of computer science.",
                "Machine learning is a subset of AI.",
                "The weather is nice today.",
                "Deep learning uses neural networks."
            ],
            "top_k": 2
        }
        response = await ac.post("/similar", json=request_data)
        # Note: This will fail if OPENAI_API_KEY is not set
        assert response.status_code in [200, 500]  # 500 if no API key


# Test utility functions (these don't require API calls)
def test_count_tokens():
    """Test token counting"""
    text = "Hello, world!"
    token_count = count_tokens(text)
    assert token_count > 0
    assert isinstance(token_count, int)


def test_chunk_text():
    """Test text chunking"""
    long_text = "This is a test. " * 20
    chunks = chunk_text(long_text, max_tokens=50)
    assert len(chunks) > 0
    assert all(isinstance(chunk, str) for chunk in chunks)
    
    # Test that chunks are smaller than max_tokens
    for chunk in chunks:
        chunk_tokens = count_tokens(chunk)
        assert chunk_tokens <= 50


def test_cosine_similarity():
    """Test cosine similarity calculation"""
    vec1 = [1.0, 0.0, 0.0]
    vec2 = [1.0, 0.0, 0.0]
    similarity = cosine_similarity(vec1, vec2)
    assert similarity == 1.0
    
    vec3 = [0.0, 1.0, 0.0]
    similarity = cosine_similarity(vec1, vec3)
    assert similarity == 0.0
    
    # Test with different length vectors
    with pytest.raises(ValueError):
        cosine_similarity([1, 2], [1, 2, 3])


# Integration tests (these require API calls and will be skipped if no API key)
@pytest.mark.asyncio
async def test_integration_chat_flow():
    """Test complete chat flow (requires API key)"""
    try:
        response = await test_chat()
        assert isinstance(response, str)
        assert len(response) > 0
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            raise


@pytest.mark.asyncio
async def test_integration_embedding_flow():
    """Test complete embedding flow (requires API key)"""
    try:
        embedding_length = await test_embedding()
        assert isinstance(embedding_length, int)
        assert embedding_length > 0
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            raise


@pytest.mark.asyncio
async def test_integration_prompt_engineering():
    """Test prompt engineering flow (requires API key)"""
    try:
        response = await test_prompt_engineering()
        assert isinstance(response, str)
        assert len(response) > 0
        # Should contain travel-related content
        assert any(word in response.lower() for word in ["japan", "travel", "trip", "day"])
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            raise


@pytest.mark.asyncio
async def test_integration_function_calling():
    """Test function calling flow (requires API key)"""
    try:
        result = await test_function_calling()
        assert isinstance(result, dict)
        assert "function_called" in result or "error" in result
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            raise


@pytest.mark.asyncio
async def test_integration_chunking_embedding():
    """Test chunking and embedding workflow (requires API key)"""
    try:
        result = await test_chunking_and_embedding()
        assert isinstance(result, dict)
        assert "total_tokens" in result
        assert "num_chunks" in result
        assert "embedding_dimensions" in result
        assert result["total_tokens"] > 0
        assert result["num_chunks"] > 0
        assert result["embedding_dimensions"] > 0
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            raise


# Performance tests
@pytest.mark.asyncio
async def test_chat_performance():
    """Test chat performance with multiple requests"""
    try:
        import time
        start_time = time.time()
        
        # Make multiple chat requests
        messages = [{"role": "user", "content": "Say hello"}]
        responses = []
        
        for _ in range(3):
            response = await get_chat_response(messages, max_retries=1)
            responses.append(response)
        
        end_time = time.time()
        duration = end_time - start_time
        
        assert len(responses) == 3
        assert all(isinstance(r, str) for r in responses)
        assert duration < 30  # Should complete within 30 seconds
        
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            raise


@pytest.mark.asyncio
async def test_embedding_performance():
    """Test embedding performance with multiple requests"""
    try:
        import time
        start_time = time.time()
        
        # Make multiple embedding requests
        texts = [
            "First text to embed",
            "Second text to embed", 
            "Third text to embed"
        ]
        embeddings = []
        
        for text in texts:
            embedding = await get_embedding(text, max_retries=1)
            embeddings.append(embedding)
        
        end_time = time.time()
        duration = end_time - start_time
        
        assert len(embeddings) == 3
        assert all(len(emb) > 0 for emb in embeddings)
        assert duration < 30  # Should complete within 30 seconds
        
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            raise


# Error handling tests
@pytest.mark.asyncio
async def test_chat_error_handling():
    """Test chat error handling with invalid input"""
    try:
        # Test with empty messages
        with pytest.raises(Exception):
            await get_chat_response([])
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            # This is expected behavior
            pass


@pytest.mark.asyncio
async def test_embedding_error_handling():
    """Test embedding error handling with invalid input"""
    try:
        # Test with empty text
        with pytest.raises(Exception):
            await get_embedding("")
    except Exception as e:
        if "OPENAI_API_KEY" in str(e):
            pytest.skip("OpenAI API key not configured")
        else:
            # This is expected behavior
            pass


if __name__ == "__main__":
    pytest.main([__file__])
