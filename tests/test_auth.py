import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_register_login():
    """Test user registration and login flow"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        # Generate unique user data to avoid conflicts
        import uuid
        unique_id = str(uuid.uuid4())[:8]
        
        # Test user registration
        register_data = {
            'username': f'testuser_{unique_id}',
            'email': f'test_{unique_id}@example.com', 
            'password': 'testpassword123'
        }
        
        # Register user
        register_response = await ac.post('/auth/register', json=register_data)
        assert register_response.status_code == 200
        
        user_data = register_response.json()
        assert user_data['username'] == register_data['username']
        assert user_data['email'] == register_data['email']
        assert 'id' in user_data
        
        # Test user login
        login_data = {
            'username': register_data['username'],
            'password': register_data['password']
        }
        
        # Login with form data (as discovered from debug)
        login_response = await ac.post('/auth/login', data=login_data)
        assert login_response.status_code == 200
        
        token_data = login_response.json()
        assert 'access_token' in token_data
        assert 'token_type' in token_data
        
        print(f"✅ Test passed! User {register_data['username']} registered and logged in successfully")