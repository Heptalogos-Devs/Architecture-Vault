# Heptalogos Documentation Instructions

This scope owns the Heptalogos target design, accepted design decisions, rationale, and unresolved design questions.

- `TARGET_DESIGN.md` is the canonical, directly authored target-design source. Keep it limited to intended product semantics, architecture, authority, invariants, cross-system obligations, and accepted target physical structure.
- Do not describe current code status, implementation gaps, active Plans, qualification results, repository migration, or dependency-version details in the target design.
- Keep Nous Wave cognition objects and lifecycle under Nous Wave authority. Use `../integration/cognition-agency.md` as canonical for shared semantics; this target design may state Heptalogos's local responsibilities.
- Put accepted conclusions in `DECISIONS.md`, design choices and consequences in `rationale/`, and unresolved design work in `OPEN_QUESTIONS.md`.
- PDF or other publication artifacts, if introduced by a separate publication workflow, are derivatives of `TARGET_DESIGN.md` and must not add semantics. Do not maintain a second manually authored LaTeX source.
- Verify semantic coverage, local links, and `git diff --check` after changes.
