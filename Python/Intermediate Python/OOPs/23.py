# Asynchronous Python

# Async programming is especially useful for waiting on I/O, 
# such as API calls and network requests.
#  It doesn't automatically make CPU-heavy calculations faster.

# The async def keyword defines a coroutine function.
import asyncio


async def greet():
    await asyncio.sleep(2) # Asynchronously waits for 2 seconds
    print("Hello, Loveleen!")


asyncio.run(greet())