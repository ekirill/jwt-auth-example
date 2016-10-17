# -*- coding: utf-8 -*-
def test_app_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'OK'


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
