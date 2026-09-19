# Async API Stimulation

#Now let's practice a real-world backend scenario: fetching user data from an API.

# Imagine you're building an appointment booking system like your Driveway Docs project.
# You need to retrieve user information without blocking other async work.


import asyncio


async def fetch_user(user_id):
    print(f"Fetching user {user_id}...")

    await asyncio.sleep(2)

    return f"User {user_id} data received"


async def main():
    results = await asyncio.gather(
        fetch_user(101),
        fetch_user(102)
    )

    for result in results:
        print(result)


asyncio.run(main())