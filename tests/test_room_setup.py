import random

from werewolf_langgraph.state import Player, Role, create_initial_state, state_to_graph_state
from werewolf_langgraph.web import AI_NAMES, DEFAULT_ROLES, Room, _make_players, _serialize_room


def test_make_players_builds_nine_named_seats(monkeypatch):
    monkeypatch.setattr(random, "shuffle", lambda items: None)
    monkeypatch.setattr(random, "sample", lambda items, k: list(items)[:k])

    players = _make_players("鎵撴憜瀛愮殑瀹朵紮", 4)

    assert len(players) == 9
    assert [player.id for player in players] == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    assert players[3].is_human
    assert players[3].name == "鎵撴憜瀛愮殑瀹朵紮"
    assert [player.name for player in players if not player.is_human] == AI_NAMES


def test_default_roles_use_three_villagers_three_wolves_and_three_specials():
    assert DEFAULT_ROLES.count(Role.VILLAGER) == 3
    assert DEFAULT_ROLES.count(Role.WEREWOLF) == 3
    assert DEFAULT_ROLES.count(Role.WITCH) == 1
    assert DEFAULT_ROLES.count(Role.SEER) == 1
    assert DEFAULT_ROLES.count(Role.HUNTER) == 1


def test_serialize_room_exposes_wolf_teammates_to_a_werewolf_human():
    players = [
        Player(id="1", name="甲", role=Role.WEREWOLF, is_human=True),
        Player(id="2", name="乙", role=Role.WEREWOLF),
        Player(id="3", name="丙", role=Role.VILLAGER),
    ]
    state = state_to_graph_state(create_initial_state(players))
    room = Room("room1", state, human_id="1", graph=None)

    payload = _serialize_room(room)

    assert payload["wolf_teammates"] == [{"id": "2", "name": "乙"}]


def test_serialize_room_reveals_dead_hunter_role_only_before_game_over():
    players = [
        Player(id="1", name="human", role=Role.VILLAGER, is_human=True),
        Player(id="2", name="hunter", role=Role.HUNTER, is_alive=False),
        Player(id="3", name="villager", role=Role.VILLAGER, is_alive=False),
    ]
    state = state_to_graph_state(create_initial_state(players))
    room = Room("room1", state, human_id="1", graph=None)

    payload = _serialize_room(room)
    roles_by_id = {player["id"]: player["role"] for player in payload["players"]}

    assert roles_by_id["2"] == "hunter"
    assert roles_by_id["3"] == "hidden"
