import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_login():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        r = await ac.post('/auth/register', json={'username':'test','email':'t@test.com','password':'secret'})
        assert r.status_code == 200
        r2 = await ac.post('/auth/login', data={'username':'test','password':'secret'})
        assert r2.status_code == 200
        assert 'access_token' in r2.json()
