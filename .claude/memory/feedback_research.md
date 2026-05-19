---
name: Research before implementing
description: Always research the most efficient implementation independently before coding, don't just copy from Mont'ka
type: feedback
originSessionId: 7558c67f-9622-468f-801f-9d9342dd4dc1
---
When implementing features for either bot, research the most efficient approach independently (web search, SC2 strategy resources, ares-sc2 docs) before writing any code. This applies to both Mont'ka and Kau'yon.

**Why:** Each bot has a distinct playstyle and race matchup context. Copying between bots or skipping research leads to wrong strategic decisions (e.g. the gateway hold-at-2 issue in Kau'yon).

**How to apply:** Before implementing any feature, research SC2 strategy for the relevant race/matchup first, then consult ares-sc2 docs for API usage. Only cross-reference the other bot for ares API patterns, never for strategic decisions.
