# Cartoon Werewolf Opening Design

## Goal

Rename the opening experience to "卡通狼人杀" and make the first screen immediately show eight cartoon character slots: 蜡笔小新, 哆啦A梦, 奶龙, 海绵宝宝, 猪猪侠, 懒羊羊, 小猪佩奇, and 柯南.

## Scope

This change only affects the opening screen and visual styling. It does not change room creation, role assignment, player count, night actions, voting, or backend game rules.

## Layout

Use the approved A layout: an equal-weight two-by-four character grid on the start screen. Each card shows a colorful avatar-style tile and the character name. The cards are placeholders that can later be replaced with image assets without changing game logic.

The existing player name input, start button, and status message remain available beneath the character grid.

## Visual Direction

Move the opening background from a serious dark werewolf tone toward a cartoon night-party tone:

- Deep blue night base to preserve the werewolf setting.
- Cyan, warm yellow, red, and pink accents to make the page feel playful.
- A brighter moon and softer decorative shapes.
- Button styling remains clear and high contrast.

## Testing

Add frontend source tests that verify:

- The HTML title and H1 use "卡通狼人杀".
- The start screen contains all eight requested character names.
- The start screen includes a character grid class.
- The stylesheet includes the character-grid and card styles.
