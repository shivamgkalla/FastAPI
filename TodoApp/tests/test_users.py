from http.client import responses

from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == "shivamkallatest"
    assert response.json()['email'] == "shivamkallatest@gmail.com"
    assert response.json()['first_name'] == "Shivam"
    assert response.json()['last_name'] == "Kalla"
    assert response.json()['phone_no'] == "0123456789"


def test_change_password_success(test_user):
    response = client.put('/user/password', json= {"password": "testpassword", "new_password": "newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={"password": "wrong_password", "new_password": "newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Failed to change password.'}


def test_change_phone_no_success(test_user):
    response = client.put('/user/phone_no/1234567890')
    assert response.status_code == status.HTTP_204_NO_CONTENT

