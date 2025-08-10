import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_register_login():
    """Test user registration and login with unique credentials"""
    # Generate unique data for each test run
    unique_id = str(uuid.uuid4())[:8]
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        # Test user registration
        register_data = {
            'username': f'test_{unique_id}',
            'email': f'test_{unique_id}@example.com',
            'password': 'secret123'
        }
        
        register_response = await ac.post('/auth/register', json=register_data)
        assert register_response.status_code == 200
        
        # Test user login (using form data instead of JSON)
        login_data = {
            'username': register_data['username'],
            'password': register_data['password']
        }
        
        login_response = await ac.post('/auth/login', data=login_data)
        
        # Debug login response
        print(f"\nLogin Status Code: {login_response.status_code}")
        try:
            print(f"Login Response Body: {login_response.json()}")
        except:
            print(f"Login Response Text: {login_response.text}")
            
        assert login_response.status_code == 200
        
        # Verify login response contains expected data (adjust as needed)
        login_result = login_response.json()
        assert 'access_token' in login_result or 'token' in login_result