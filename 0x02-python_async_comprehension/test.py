#!/usr/bin/env python3
async def data_source():
    for i in range(5):
        await asyncio.sleep(1)
        yield f"Data {i}"

async def main():
    async for data in data_source():
        print(data)

asyncio.run(main())

