# Custom Human Name Design

## Goal

Let the human player type a custom display name before creating a Werewolf room.

## Current State

The backend `CreateRoomRequest` already accepts `human_name`, trims it, and falls back to the default name when the submitted value is blank. The frontend currently sends a hard-coded default name from `startGame()`.

## Design

Add a single name input to the start screen. When the player clicks the create-room button, `startGame()` reads the input value, trims whitespace, and sends it as `human_name` in the existing `/api/rooms` request. If the input is empty, the frontend sends the existing default name.

The backend data model and room serialization stay unchanged.

## Validation

Add frontend source tests that assert:

- The start page contains a `humanNameInput` field.
- `startGame()` reads from `#humanNameInput`.
- The room creation payload uses the trimmed custom value with the default fallback.

