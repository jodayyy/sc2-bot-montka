---
name: Add comments for maintainability
description: When implementing features in this project, always add comments so any developer can understand and maintain the code
type: feedback
originSessionId: 7558c67f-9622-468f-801f-9d9342dd4dc1
---
Always add comments when implementing things in this project — not just docstrings, but inline comments explaining what each section does and why.

**Why:** The user wants the code to be maintainable by anyone, not just the original author.

**How to apply:** Add clear comments to every non-trivial block of logic: what the behavior does, why it's registered, what conditions trigger a branch, etc. This applies to all bot files (macro, production, combat, defense, micro, builds).
