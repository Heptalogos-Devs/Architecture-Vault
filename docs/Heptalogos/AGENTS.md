# Heptalogos Documentation Instructions

This scope owns the Heptalogos target design, accepted design decisions, rationale, and unresolved design questions.

- Keep `main.tex` and its included chapters limited to the target Heptalogos system. Do not describe current code status, implementation gaps, active plans, repository changes, historical designs, or comparisons there.
- Keep Nous Wave's cognition objects and lifecycle under Nous Wave authority. Use `docs/integration/cognition-agency.md` as the canonical source for shared semantics; this target design may state Heptalogos's local responsibilities.
- `Pursuit` is a target behavior concept. Do not imply that a Spec or implementation exists unless that is verified in the Heptalogos code repository.
- Put accepted conclusions in `DECISIONS.md`, design choices and consequences in `rationale/`, and unresolved design work in `OPEN_QUESTIONS.md`.
- Follow `BUILD.md` and visually inspect all pages after changing the LaTeX source.
