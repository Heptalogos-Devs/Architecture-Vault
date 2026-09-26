# Nous Wave Documentation Instructions

This scope owns the Nous Wave target design, accepted design decisions, rationale, research evidence, and open design questions.

- Treat TARGET_DESIGN.md as the sole directly authored Nous Wave Target Design Authority.
- Keep TARGET_DESIGN.md limited to target semantics, ownership, boundaries, invariants, and durable contracts. Do not add current code status, implementation gaps, active plans, repository migration state, historical designs, provider versions, or algorithm comparisons.
- Put accepted conclusions in DECISIONS.md, comparisons and consequences in rationale/, experiments and source evidence in research/, and unresolved design questions in OPEN_QUESTIONS.md.
- Keep Heptalogos behavior authority outside Nous Wave. Use ../integration/cognition-agency.md as the canonical cross-system contract; project only Nous Wave responsibilities into the target design.
- Keep current implementation architecture, Specs, Plans, and qualification evidence in the Nous-Wave code repository.
- Do not create or restore a parallel LaTeX authoring source or an automatic PDF workflow without an explicit publication decision and a deterministic Markdown-derived pipeline.
- Update the relevant README and docs/INDEX.md when maintained documents are added, removed, or moved. Run the repository Markdown-link checks and git diff --check before completion.
