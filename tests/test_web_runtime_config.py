import sys

from werewolf_langgraph import web


def test_main_uses_environment_defaults(monkeypatch):
    monkeypatch.setenv("WEREWOLF_HOST", "0.0.0.0")
    monkeypatch.setenv("WEREWOLF_PORT", "9000")
    monkeypatch.setattr(sys, "argv", ["werewolf-web"])

    captured = {}

    def fake_run(app, **kwargs):
        captured["kwargs"] = kwargs

    monkeypatch.setattr(web.uvicorn, "run", fake_run)

    web.main()

    assert captured["kwargs"]["host"] == "0.0.0.0"
    assert captured["kwargs"]["port"] == 9000
    assert captured["kwargs"]["proxy_headers"] is True
    assert captured["kwargs"]["forwarded_allow_ips"] == "*"


def test_main_allows_cli_overrides(monkeypatch):
    monkeypatch.setenv("WEREWOLF_HOST", "0.0.0.0")
    monkeypatch.setenv("WEREWOLF_PORT", "9000")
    monkeypatch.setattr(sys, "argv", ["werewolf-web", "--host", "127.0.0.1", "--port", "8123"])

    captured = {}

    def fake_run(app, **kwargs):
        captured["kwargs"] = kwargs

    monkeypatch.setattr(web.uvicorn, "run", fake_run)

    web.main()

    assert captured["kwargs"]["host"] == "127.0.0.1"
    assert captured["kwargs"]["port"] == 8123
