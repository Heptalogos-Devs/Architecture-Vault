# Nous Wave Documentation Instructions

This scope owns the Nous Wave target design and its accepted design decisions, rationale, research evidence, and open design questions.

- Keep `main.tex` and its included chapters limited to the target Nous Wave system. Do not describe current code status, implementation gaps, active plans, repository changes, historical designs, or algorithm comparisons there.
- Put accepted conclusions in `DECISIONS.md`, comparisons and consequences in `rationale/`, experiments and source evidence in `research/`, and unresolved design questions in `OPEN_QUESTIONS.md`.
- Keep Heptalogos behavior authority outside Nous Wave. Use `docs/integration/cognition-agency.md` as the canonical source for shared semantics; this target design may state Nous Wave's local responsibilities.
- Keep current implementation architecture, Specs, Plans, and qualification evidence in the Nous-Wave code repository.
- Follow `BUILD.md` and visually inspect all pages after changing the LaTeX source.
