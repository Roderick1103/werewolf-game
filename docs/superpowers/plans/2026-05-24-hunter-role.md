# Hunter Role Implementation Plan

> **For AI agents:** Use focused TDD. Implement the role pool first, then death-triggered hunter shot resolution.

**Goal:** Add the hunter role and update the 9-player setup to 3 villagers, 3 werewolves, 1 witch, 1 seer, and 1 hunter.

**Architecture:** Extend the core role enum and graph state with a pending hunter-shot marker. Route both night deaths and day execution through a shared hunter-death resolver before winner calculation. Reuse the existing interrupt/resume shape for human target selection.

**Tech Stack:** Python dataclasses and LangGraph state, FastAPI room serialization, static JavaScript frontend, pytest tests.

---

## Files

- Modify `src/werewolf_langgraph/state.py` for `Role.HUNTER` and pending hunter shot fields.
- Modify `src/werewolf_langgraph/web.py` for the new default role pool and payload resume field.
- Modify `src/werewolf_langgraph/game_graph.py` for hunter death detection, interrupt, target resolution, and winner timing.
- Modify `src/werewolf_langgraph/agents.py` so AI hunter can choose a shot target and role prompts understand hunter as good camp.
- Modify `src/werewolf_langgraph/static/app.js` so role names and `hunter_shot` choices render.
- Modify tests in `tests/test_room_setup.py`, `tests/test_vote_turn_order.py`, and `tests/test_frontend_start_feedback.py`.

## Tasks

- [ ] Add failing tests for the new role pool counts.
- [ ] Add failing tests that a human hunter killed at night creates a `hunter_shot` interrupt before winner calculation.
- [ ] Add failing tests that a hunter shot can kill the final wolf and produce a good-camp winner.
- [ ] Add failing frontend source tests for hunter display and `hunter_shot` target UI.
- [ ] Implement role enum, labels, role pool, and state fields.
- [ ] Implement shared hunter-shot helpers in the graph.
- [ ] Wire night and day death resolution through the helper.
- [ ] Add frontend rendering for hunter choices.
- [ ] Run targeted tests and the full suite.

