import asyncio

import requests


async def get_file(file_id: int):
    response = requests.get(f'http://localhost:5000/test/{file_id}')
    return response.json()


def get_data_async():
    async def get_data():
        async def get_tasks():
            tasks = [get_file(i) for i in range(1, 4)]
            return await asyncio.gather(*tasks)

        return await get_tasks()

    loop = asyncio.new_event_loop()

    results = loop.run_until_complete(get_data())
    loop.close()

    data = []
    for r in results:
        data += [*r['data']]
    return sorted(data, key=lambda x: x['id'])
