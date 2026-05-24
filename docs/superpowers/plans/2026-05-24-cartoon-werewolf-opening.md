# Cartoon Werewolf Opening Implementation Plan

> **For AI agents:** Use TDD for the frontend source assertions, then implement the smallest HTML/CSS change that satisfies them.

**Goal:** Update the start screen to present the project as "卡通狼人杀" with eight cartoon character cards and a brighter cartoon-night palette.

**Architecture:** Keep the current static frontend structure. Modify `index.html` for semantic content and `styles.css` for layout and color treatment. Add tests to `tests/test_frontend_start_feedback.py` because it already checks static frontend source behavior.

**Tech Stack:** FastAPI static frontend, vanilla HTML/CSS/JS, pytest source checks.

---

## Files

- Modify `src/werewolf_langgraph/static/index.html`: title, H1, and character grid markup.
- Modify `src/werewolf_langgraph/static/styles.css`: start-screen background, content layout, character grid, and responsive behavior.
- Modify `tests/test_frontend_start_feedback.py`: source tests for title, character names, and CSS hooks.

## Tasks

- [ ] Add failing pytest assertions for the new opening copy and character grid.
- [ ] Run the targeted pytest file and confirm the new test fails before implementation.
- [ ] Add the approved A layout markup to the start screen while preserving input, button, status, and element ids.
- [ ] Update start-screen CSS for the brighter cartoon-night palette and responsive two-by-four grid.
- [ ] Run the targeted pytest file.
- [ ] Run the broader test suite.
