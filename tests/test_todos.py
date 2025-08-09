import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_todo_crud():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        await ac.post('/auth/register', json={'username':'todo','email':'a@a.com','password':'pwd'})
        r = await ac.post('/auth/login', data={'username':'todo','password':'pwd'})
        token = r.json()['access_token']
        headers = {'Authorization': f'Bearer {token}'}
        r = await ac.post('/todos/', json={'title':'t1','description':'d'}, headers=headers)
        assert r.status_code == 200
        todo = r.json()
        tid = todo['id']
        r = await ac.get('/todos/', headers=headers)
        assert r.status_code == 200
        r = await ac.get(f'/todos/{tid}', headers=headers)
        assert r.status_code == 200
        r = await ac.put(f'/todos/{tid}', json={'title':'t1u','description':'d'}, headers=headers)
        assert r.status_code == 200
        r = await ac.delete(f'/todos/{tid}', headers=headers)
        assert r.status_code == 200
