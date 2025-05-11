import os
import httpx

USERS_SERVICE_HOST_URL = 'http://localhost:8000/api/v1/users/'
url = os.environ.get('USERS_SERVICE_HOST_URL') or USERS_SERVICE_HOST_URL


async def get_user(user_id: str):
    response = httpx.get(f'{url}{user_id}')
    if response.status_code == 200:
        return response.json()
    return None
