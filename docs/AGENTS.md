# Documentation Instructions

This scope contains maintained human-facing design knowledge and generated target-design sources.

- Use Chinese for human-facing documents and concise technical English for agent instructions.
- Keep the ownership boundaries in `DOCUMENT_MODEL.md`; do not move current implementation facts or active plans into this repository.
- Treat the Nous Wave and Heptalogos LaTeX sources as target designs. Keep implementation status, history, repository migration progress, unresolved questions, and option comparisons in their designated owners.
- Treat `integration/cognition-agency.md` as the canonical cross-system contract. System target designs may project its requirements into their local boundaries; keep those summaries synchronized with the contract.
- Update `INDEX.md` when maintained documents are added, removed, or moved. Update the relevant scope README when its reading path changes.
- Build and visually inspect every affected PDF after source changes. Use the scope's `BUILD.md` instructions.
