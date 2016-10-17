# -*- coding: utf-8 -*-
import json
from mock import patch


def test_app_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'OK'


def test_login(client, credentials_checker):
    with patch('app_example.auth.credentials_checker', credentials_checker):
        response = client.post(
            '/login',
            content_type='application/json',
            data=json.dumps({
                'login': 'ekirill',
                'password': 'asdasd',
            })
        )
        assert response.status_code == 200
        assert response.json['status'] == 'FAIL'

        response = client.post(
            '/login',
            content_type='application/json',
            data=json.dumps({
                'login': 'ekirill',
                'password': 'ekirill',
            })
        )
        assert response.status_code == 200
        assert response.json['status'] == 'OK'
        assert response.json['data']['token']


def test_app_resource_01(client):
    response = client.get('/api/v1/resource_01.json')
    assert response.status_code == 200
    assert response.json['status'] == 'OK'
    assert response.json['data']['juicy_data'] == 42


def test_app_resource_02(client):
    response = client.get('/api/v1/resource_02.json')
    assert response.status_code == 200
    assert response.json['status'] == 'OK'
    assert response.json['data']['sugar_data'] == 24
