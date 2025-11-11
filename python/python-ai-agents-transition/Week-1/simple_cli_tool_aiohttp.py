import asyncio
import aiohttp
import argparse
import json

async def make_request(url, method="GET", data=None):
    async with aiohttp.ClientSession() as session:
        if method == "GET":
            async with session.get(url) as response:
                return {
                    "status": response.status,
                    "data": await response.text()
                }
        elif method == "POST":
            async with session.post(url, json=data) as response:
                return {
                    "status": response.status,
                    "data": await response.text()
                }

def setup_parser():
    parser = argparse.ArgumentParser(description="Simple HTTP client")
    parser.add_argument("url", help="URL to request")
    parser.add_argument("--method", default="GET", choices=["GET", "POST"], help="HTTP method")
    parser.add_argument("--data", help="JSON data for POST")
    return parser

async def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    data = None
    if args.data:
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError:
            print("Error: Invalid JSON data")
            return
    
    try:
        result = await make_request(args.url, args.method, data)
        print(f"Status: {result['status']}")
        print(f"Data: {result['data'][:200]}...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 