# -*- coding: utf-8 -*-
def test_app_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'status': 'ALIVE'}
