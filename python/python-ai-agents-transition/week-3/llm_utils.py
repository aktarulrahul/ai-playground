"""
LLM Utilities Module for Week 3
OpenAI SDK integration with async support, error handling, and token-aware chunking
"""

import os
import asyncio
import logging
from typing import List, Dict, Any, Optional
from openai import AsyncOpenAI
import tiktoken
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize tiktoken encoder
try:
    enc = tiktoken.encoding_for_model("gpt-4o-mini")
except Exception as e:
    logger.warning(f"Could not initialize tiktoken encoder: {e}")
    enc = None


class LLMError(Exception):
    """Custom exception for LLM-related errors"""
    pass


async def get_chat_response(
    messages: List[Dict[str, str]], 
    model: str = "gpt-4o-mini",
    max_retries: int = 3,
    temperature: float = 0.7
) -> str:
    """
    Get chat completion response with retry logic and error handling
    
    Args:
        messages: List of message dictionaries with 'role' and 'content'
        model: OpenAI model to use
        max_retries: Maximum number of retry attempts
        temperature: Model temperature (0.0 to 2.0)
    
    Returns:
        Response content as string
    
    Raises:
        LLMError: If all retries fail
    """
    for attempt in range(max_retries):
        try:
            logger.info(f"Chat request attempt {attempt + 1}/{max_retries}")
            
            response = await client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            
            # Log usage
            if response.usage:
                logger.info(f"Usage - Tokens: {response.usage.total_tokens}, "
                          f"Prompt: {response.usage.prompt_tokens}, "
                          f"Completion: {response.usage.completion_tokens}")
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Chat request failed (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                # Exponential backoff
                wait_time = 2 ** attempt
                logger.info(f"Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                raise LLMError(f"Chat request failed after {max_retries} attempts: {e}")


async def get_embedding(
    text: str, 
    model: str = "text-embedding-3-small",
    max_retries: int = 3
) -> List[float]:
    """
    Get embedding for text with retry logic and error handling
    
    Args:
        text: Text to embed
        model: OpenAI embedding model to use
        max_retries: Maximum number of retry attempts
    
    Returns:
        Embedding vector as list of floats
    
    Raises:
        LLMError: If all retries fail
    """
    for attempt in range(max_retries):
        try:
            logger.info(f"Embedding request attempt {attempt + 1}/{max_retries}")
            
            response = await client.embeddings.create(
                model=model,
                input=text
            )
            
            # Log usage
            if response.usage:
                logger.info(f"Embedding usage - Tokens: {response.usage.total_tokens}")
            
            return response.data[0].embedding
            
        except Exception as e:
            logger.error(f"Embedding request failed (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                # Exponential backoff
                wait_time = 2 ** attempt
                logger.info(f"Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                raise LLMError(f"Embedding request failed after {max_retries} attempts: {e}")


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """
    Count tokens in text using tiktoken
    
    Args:
        text: Text to count tokens for
        model: Model to use for tokenization
    
    Returns:
        Number of tokens
    """
    try:
        if enc is None:
            # Fallback: rough estimation (1 token ≈ 4 characters)
            return len(text) // 4
        
        tokens = enc.encode(text)
        return len(tokens)
    except Exception as e:
        logger.error(f"Token counting failed: {e}")
        # Fallback: rough estimation
        return len(text) // 4


def chunk_text(text: str, max_tokens: int = 1000, model: str = "gpt-4o-mini") -> List[str]:
    """
    Split text into chunks that fit within token limits
    
    Args:
        text: Text to chunk
        max_tokens: Maximum tokens per chunk
        model: Model to use for tokenization
    
    Returns:
        List of text chunks
    """
    try:
        if enc is None:
            # Fallback: simple character-based chunking
            chunk_size = max_tokens * 4  # Rough estimation
            return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        
        tokens = enc.encode(text)
        chunks = []
        
        for i in range(0, len(tokens), max_tokens):
            chunk_tokens = tokens[i:i + max_tokens]
            chunk_text = enc.decode(chunk_tokens)
            chunks.append(chunk_text)
        
        return chunks
        
    except Exception as e:
        logger.error(f"Text chunking failed: {e}")
        # Fallback: simple character-based chunking
        chunk_size = max_tokens * 4
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


async def test_chat() -> str:
    """Test chat functionality"""
    messages = [{"role": "user", "content": "Hello, world!"}]
    return await get_chat_response(messages)


async def test_embedding() -> int:
    """Test embedding functionality"""
    text = "The quick brown fox jumps over the lazy dog"
    embedding = await get_embedding(text)
    return len(embedding)


async def test_prompt_engineering() -> str:
    """Test prompt engineering with system and user roles"""
    messages = [
        {"role": "system", "content": "You are a helpful travel guide."},
        {"role": "user", "content": "Plan a 3-day trip to Japan."}
    ]
    return await get_chat_response(messages)


async def test_function_calling() -> Dict[str, Any]:
    """Test function calling (structured outputs)"""
    messages = [
        {"role": "user", "content": "What's the weather like in Tokyo?"}
    ]
    
    functions = [
        {
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "temperature": {"type": "number"},
                    "condition": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    ]
    
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            functions=functions
        )
        
        # Check if function was called
        if response.choices[0].message.function_call:
            return {
                "function_called": True,
                "function_name": response.choices[0].message.function_call.name,
                "arguments": response.choices[0].message.function_call.arguments
            }
        else:
            return {
                "function_called": False,
                "response": response.choices[0].message.content
            }
            
    except Exception as e:
        logger.error(f"Function calling test failed: {e}")
        return {"error": str(e)}


async def test_chunking_and_embedding() -> Dict[str, Any]:
    """Test chunking and embedding workflow"""
    # Sample long text
    long_text = """
    Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines 
    that work and react like humans. Some of the activities computers with artificial intelligence are 
    designed for include speech recognition, learning, planning, and problem solving. AI has been used 
    in various applications such as virtual assistants, autonomous vehicles, medical diagnosis, and 
    financial trading. Machine learning, a subset of AI, enables computers to learn and improve from 
    experience without being explicitly programmed. Deep learning, a subset of machine learning, uses 
    neural networks with multiple layers to analyze various factors of data. The field of AI continues 
    to evolve rapidly with new breakthroughs in natural language processing, computer vision, and 
    robotics. Companies and researchers are constantly developing new AI technologies that have the 
    potential to transform industries and improve human lives.
    """ * 5  # Repeat to make it longer
    
    # Count tokens
    total_tokens = count_tokens(long_text)
    
    # Chunk the text
    chunks = chunk_text(long_text, max_tokens=100)
    
    # Get embeddings for each chunk
    embeddings = []
    for chunk in chunks:
        embedding = await get_embedding(chunk)
        embeddings.append(embedding)
    
    return {
        "total_tokens": total_tokens,
        "num_chunks": len(chunks),
        "chunk_tokens": [count_tokens(chunk) for chunk in chunks],
        "embedding_dimensions": len(embeddings[0]) if embeddings else 0,
        "sample_chunk": chunks[0][:100] + "..." if chunks else ""
    }


# Vector similarity functions (for future vector DB integration)
def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors"""
    import math
    
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same length")
    
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(a * a for a in vec2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    return dot_product / (magnitude1 * magnitude2)


async def find_similar_chunks(
    query: str, 
    chunks: List[str], 
    top_k: int = 3
) -> List[Dict[str, Any]]:
    """
    Find most similar chunks to a query using embeddings
    
    Args:
        query: Query text
        chunks: List of text chunks
        top_k: Number of top similar chunks to return
    
    Returns:
        List of dictionaries with chunk text and similarity score
    """
    # Get query embedding
    query_embedding = await get_embedding(query)
    
    # Get embeddings for all chunks
    chunk_embeddings = []
    for chunk in chunks:
        embedding = await get_embedding(chunk)
        chunk_embeddings.append(embedding)
    
    # Calculate similarities
    similarities = []
    for i, chunk_embedding in enumerate(chunk_embeddings):
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        similarities.append({
            "chunk": chunks[i],
            "similarity": similarity,
            "index": i
        })
    
    # Sort by similarity and return top_k
    similarities.sort(key=lambda x: x["similarity"], reverse=True)
    return similarities[:top_k]
