import asyncio
import time

async def simple_task(name):
    print(f"Starting {name}")
    await asyncio.sleep(1)
    print(f"Finished {name}")
    return f"Result from {name}"

async def run_concurrent():
    task1 = asyncio.create_task(simple_task("Task 1"))
    task2 = asyncio.create_task(simple_task("Task 2"))
    
    results = await asyncio.gather(task1, task2)
    print(f"All results: {results}")

async def async_generator():
    for i in range(3):
        await asyncio.sleep(0.5)
        yield i

async def process_generator():
    async for item in async_generator():
        print(f"Got: {item}")

async def timeout_example():
    try:
        await asyncio.wait_for(asyncio.sleep(3), timeout=1.0)
    except asyncio.TimeoutError:
        print("Operation timed out")

async def main():
    print("=== Async Demo ===\n")
    
    print("1. Simple async task:")
    result = await simple_task("Single Task")
    print(f"Result: {result}\n")
    
    print("2. Concurrent tasks:")
    await run_concurrent()
    print()
    
    print("3. Async generator:")
    await process_generator()
    print()
    
    print("4. Timeout example:")
    await timeout_example()

if __name__ == "__main__":
    asyncio.run(main()) 