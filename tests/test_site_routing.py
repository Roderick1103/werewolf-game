from fastapi.testclient import TestClient

from werewolf_langgraph.web import create_app


def test_root_domain_serves_game_hub():
    client = TestClient(create_app())

    response = client.get("/", headers={"Host": "roderickdev.cn"})

    assert response.status_code == 200
    assert "RoderickDev" in response.text
    assert "werewolf.roderickdev.cn" in response.text


def test_werewolf_subdomain_serves_game():
    client = TestClient(create_app())

    response = client.get("/", headers={"Host": "werewolf.roderickdev.cn"})

    assert response.status_code == 200
    assert "id=\"startScreen\"" in response.text
    assert "RoderickDev" not in response.text
