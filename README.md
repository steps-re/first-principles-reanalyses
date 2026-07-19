# First-principles reanalyses

Independent, reproducible rechecks of *encouraging-but-limited* published results. One bounded
physics question per paper, worked from first principles, offered collegially to the authors.

**📄 Read:** https://steps-re.github.io/first-principles-reanalyses/

By Michael German (Steps Ventures). Not peer-reviewed. Each entry pulls the real numbers from a
paper (or its open SI), computes the relevant ceiling or model, and reports honestly — including
when a tempting angle fails on contact with a real number.

## Entries

| # | Status | Paper | Question | Finding |
|---|---|---|---|---|
| 01 | ✅ done | Trabolsi COF / PFOA, *Nat. Commun.* 2024 ([10.1038/s41467-024-53945-4](https://doi.org/10.1038/s41467-024-53945-4)) | Can a 13 m²/g material hold 2600 mg/g of PFOA as adsorption? | No — it's ~80× the monolayer capacity; the number is framework-templated PFOA aggregation, not a working capacity. See `cof-pfoa/`. |
| 02 | 🔄 in progress | Dupla ERW, *Environ. Sci. Technol.* 2025 ([10.1021/acs.est.5c09820](https://doi.org/10.1021/acs.est.5c09820)) | Where does the "missing" alkalinity go when Na proves dissolution but the MRV proxies show nothing? | Na-tracer mass balance — needs the porewater SI pulled. See `erw-dupla/`. |

## Reproduce

```bash
python cof-pfoa/monolayer_check.py   # 2600 mg/g is 73–116× the monolayer on 13 m²/g
```
Standard library only. No dependencies.

## Method & honesty

The goal is a more useful reading of a promising result, not a takedown. Numbers are cited to the
source (not redistributed); calculations are rerunnable; failed angles are reported, not buried
(e.g., the "the isotherm break is PFOA's CMC" shortcut is wrong — PFOA's CMC is ~3,000–12,700 mg/L,
far above the 500–600 mg/L break — so it is stated as a correction, not used).

Text CC BY 4.0; code MIT. Reported experimental values remain the authors' property.
