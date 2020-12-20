from timeit import default_timer
import aiohttp
import asyncio

async def load_data(session, delay):
  print(f'starting {delay} second timer')
  async with session.get(f'https://httpbin.org/delay/{delay}') as resp:
    text = await resp.text()
    print(f'completed {delay} second timer')
    return text

async def main():
  start_time = default_timer()

  # creating a single session
  async with aiohttp.ClientSession() as session:
    # setup our tasks and get them running
    two_task = asyncio.create_task(load_data(session, 2))
    three_task = asyncio.create_task(load_data(session, 3))

    # simulate other processing
    await asyncio.sleep(1)
    print('doing other stuff')

    two_result = await two_task
    three_result = await three_task

    # results
    elapsed_time = default_timer() - start_time
    print(f'the operation took {elapsed_time:.2} seconds')

asyncio.run(main())
