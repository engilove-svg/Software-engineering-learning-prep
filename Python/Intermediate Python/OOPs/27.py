# Async Task Manager

# Create three asynchronous tasks:
# Download a file
# Fetch user data
# Send an email
# Each task will take a different amount of time.


import asyncio


async def download_file():
    print("Downloading file...")
    await asyncio.sleep(3)
    print("File downloaded!")


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched!")


async def send_email():
    print("Sending email...")
    await asyncio.sleep(1)
    print("Email sent!")


async def main():
    await asyncio.gather(
        download_file(),
        fetch_data(),
        send_email()
    )

asyncio.run(main())