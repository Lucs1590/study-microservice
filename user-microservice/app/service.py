import os
import httpx

PEOPLE_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/people/'
url = os.environ.get('CAST_SERVICE_HOST_URL') or PEOPLE_SERVICE_HOST_URL


def is_cast_present(cast_id: int):
    response = httpx.get(f'{url}{cast_id}')
    return response.status_code == 200
