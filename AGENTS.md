# Repository Instructions

Architecture-Vault owns long-term target design, accepted design decisions, design rationale, research evidence, and cross-system semantic contracts for Nous Wave and Heptalogos.

## Ownership

- Follow `docs/DOCUMENT_MODEL.md` when deciding where a fact belongs.
- Target-design sources describe the system's intended semantics and architecture. Keep current implementation status, executable specifications, active plans, qualification evidence, and temporary repository-migration progress in the owning code repositories or task records.
- `docs/integration/cognition-agency.md` is the canonical cross-system contract. System target designs may project its requirements into each system's local boundary; keep those summaries synchronized with the contract.
- Keep accepted decisions, rationale, research evidence, and open questions in their existing roles. Do not present unresolved research as an accepted design decision.

## Language and editing

- Write human-facing documents in Chinese. Preserve technical identifiers and established English terms where translation would reduce precision.
- Write agent instructions in concise technical English.
- Do not preserve obsolete active documents solely for history; Git history retains their prior contents.
- Generated PDFs and LaTeX intermediates are build outputs. Do not commit them unless a repository policy explicitly changes.

## Verification

- For target-design sources with an active PDF workflow, follow the local build guide, check references and warnings, render every page, and inspect the rendered pages. This currently applies to Nous Wave.
- Heptalogos is authored in `docs/Heptalogos/TARGET_DESIGN.md`; verify its semantics and local links. The current workflow does not generate Heptalogos PDFs or use the retired LaTeX source.
- Check local Markdown links and run `git diff --check` before finishing documentation changes.
