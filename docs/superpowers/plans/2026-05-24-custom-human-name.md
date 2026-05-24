# Custom Human Name Implementation Plan

> **For AI agents:** Use focused TDD steps. Keep this change limited to the start screen and existing room creation request.

**Goal:** Let the player customize their own display name before creating a room.

**Architecture:** The frontend owns the input and request payload. The backend already accepts and sanitizes `human_name`, so no API contract change is required.

**Tech Stack:** Static HTML/CSS/JavaScript frontend, FastAPI backend, pytest source-level tests.

---

## Files

- Modify `tests/test_frontend_start_feedback.py` to describe the expected name input and payload behavior.
- Modify `src/werewolf_langgraph/static/index.html` to add the name input on the start screen.
- Modify `src/werewolf_langgraph/static/styles.css` to style the compact start form.
- Modify `src/werewolf_langgraph/static/app.js` to read the input and send the selected name.

## Tasks

- [ ] Add a failing pytest test for the start-screen name input and `startGame()` payload.
- [ ] Run the targeted pytest test and confirm it fails because the input/payload behavior is missing.
- [ ] Add the input markup and minimal styling.
- [ ] Update `startGame()` to read, trim, and fall back to the default human name.
- [ ] Run the targeted pytest tests and then the full test suite.

