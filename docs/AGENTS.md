# Documentation Instructions

This scope contains maintained human-facing design knowledge and directly authored target-design sources.

- Use Chinese for human-facing documents and concise technical English for agent instructions.
- Keep the ownership boundaries in `DOCUMENT_MODEL.md`; do not move current implementation facts or active plans into this repository.
- Treat `Heptalogos/TARGET_DESIGN.md` and `Nous-Wave/TARGET_DESIGN.md` as the canonical directly authored target designs for their respective systems. Keep implementation status, history, repository migration progress, unresolved questions, and option comparisons in their designated owners.
- Treat `integration/cognition-agency.md` as the canonical cross-system contract. System target designs may project its requirements into their local boundaries; keep those summaries synchronized with the contract.
- Update `INDEX.md` when maintained documents are added, removed, or moved. Update the relevant scope README when its reading path changes.
- No target-design PDF workflow is currently active. Markdown target-design changes require semantic and link validation; create a publication build only under an explicit publication task.
