from fastapi import HTTPException, Request
from fastapi import Header
from jose import jwt, JWTError
import asyncio
import aiohttp
from settings import SERVICES


async def perform_get_request(url: str, headers: dict = {}):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            data['status'] = response.status

            return data


async def perform_post_request(url: str, headers: dict = {}):
    async with aiohttp.ClientSession() as session:
        data = {'name': 'John', 'age': 30}
        async with session.post(url, json=data, headers=headers) as response:
            data = await response.json()
            data['status'] = response.status

            return data


async def validate_authorization(request: Request):
    response = await perform_get_request(
        SERVICES['auth'] + '/user/me/',
        headers=dict(request.headers))

    return response
