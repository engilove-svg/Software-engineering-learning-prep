import asyncio


async def get_expense(name, amount):
    print(f"Checking {name}...")
    await asyncio.sleep(1)
    return amount


async def main():
    expenses = await asyncio.gather(
        get_expense("Groceries", 75),
        get_expense("Transportation", 40)
    )

    total = sum(expenses)

    print(f"Total expenses: ${total}")


asyncio.run(main())