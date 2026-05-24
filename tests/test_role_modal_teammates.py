from pathlib import Path


APP_JS = Path(__file__).resolve().parents[1] / "src" / "werewolf_langgraph" / "static" / "app.js"
INDEX_HTML = APP_JS.with_name("index.html")


def test_werewolf_role_modal_shows_teammates_from_room_payload():
    source = APP_JS.read_text(encoding="utf-8")
    index_html = INDEX_HTML.read_text(encoding="utf-8")

    assert "room.wolf_teammates || []" in source
    assert "roleTeammates" in source
    assert "你的狼队友：" in source
    assert 'id="roleTeammates"' in index_html
