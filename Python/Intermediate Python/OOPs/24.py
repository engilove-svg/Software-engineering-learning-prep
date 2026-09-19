
import asyncio


async def study():
    print("Starting study...")
    

    await asyncio.sleep(2) # wait for 2 seconds
    

    print("Study Completed!")


asyncio.run(study())