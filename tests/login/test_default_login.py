def test_default_login(app, client):
    response_json = client.get('/login').json
    assert 'default_provider' in response_json
    assert 'providers' in response_json
    response_default = response_json['default_provider']
    response_providers = response_json['providers']
    idps = app.config['IDENTITY_PROVIDERS']['providers']
    default_idp_id = app.config['IDENTITY_PROVIDERS']['default']
    # Check default IDP is correct.
    assert response_default['id'] == default_idp_id
    assert response_default['name'] == idps[default_idp_id]['name']
    # Check all providers in response: expected ID, expected name, URL actually
    # maps correctly to the endpoint on fence.
    for response_idp in response_providers:
        assert response_idp['id'] in idps
        assert response_idp['name'] == idps[response_idp['id']]['name']
        assert client.get(response_idp['url']).status_code < 400
