# Hunter Role Design

## Goal

Change the 9-player role setup to three villagers, three werewolves, one witch, one seer, and one hunter. The hunter belongs to the good camp and may take one living player with them whenever the hunter dies.

## Rules

- Role pool: 3 villagers, 3 werewolves, 1 witch, 1 seer, 1 hunter.
- The hunter is a good-camp role.
- If the hunter dies at night, by wolf attack or witch poison, the hunter action resolves before winner calculation.
- If the hunter is voted out during the day, the hunter action resolves before winner calculation.
- The hunter can target any currently living player except the hunter.
- A human hunter creates a `hunter_shot` interrupt and chooses the target in the browser.
- An AI hunter chooses one valid target automatically.
- After the shot resolves, winner calculation runs against the updated player list.

## Data Model

Add `Role.HUNTER` and a pending death marker for hunter resolution. The marker records the dead hunter id and the stage where the death happened, so the resume step can return to the correct result screen.

## Frontend

The existing night-action choice UI can render hunter shot targets. The hunter prompt appears in the currently relevant result stage: night result for night deaths, vote result for daytime execution.

