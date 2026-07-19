"""
Monolayer-coverage check on the TG-PD COF / PFOA adsorption claim.

Jrad, Das et al. (Trabolsi group), "Cationic covalent organic framework for the fluorescent
sensing and cooperative adsorption of perfluorooctanoic acid," Nat. Commun. 15:10490 (2024),
doi:10.1038/s41467-024-53945-4 (open access; PMC11612209).

Headline claim: >2600 mg PFOA / g of COF. Reported BET surface area: ~13 m2/g (the authors note
counter-anions block the pores). The question a first-principles check settles instantly: can a
13 m2/g material physically hold 2600 mg/g as surface adsorption?

Monolayer capacity:  q_mono = (SA / A_molecule) * (MW / N_A)

Run: python monolayer_check.py    (standard library only)
"""
NA = 6.022e23
MW_PFOA = 414.07          # g/mol
SA = 13.0                 # m2/g, TG-PD COF BET (Nat Commun 2024 / PMC11612209)
CLAIM = 2600.0            # mg/g, headline capacity
# PFOA minimum area per molecule at an interface, literature range (nm^2):
AREAS = (0.25, 0.30, 0.40)
# PFOA CMC (ES&T Lett. 2024, 10.1021/acs.estlett.4c00858): acid ~3000-3460 mg/L; APFO ~12700 mg/L
CMC_MGL = (3000, 12700)
BREAK_MGL = (500, 600)    # reported Langmuir->Freundlich transition


def monolayer_capacity(sa_m2g, area_nm2):
    a = area_nm2 * 1e-18                 # m2 per molecule
    return (sa_m2g / a) * (MW_PFOA / NA) * 1000.0   # mg/g


def sa_needed(cap_mgg, area_nm2):
    return (cap_mgg / 1000.0) * (area_nm2 * 1e-18) * NA / MW_PFOA


def main():
    print(f"TG-PD COF: BET = {SA} m2/g;  claim = {CLAIM:.0f} mg PFOA/g\n")
    print("Monolayer PFOA capacity this surface can physically hold:")
    for a in AREAS:
        q = monolayer_capacity(SA, a)
        print(f"  area {a} nm2/molecule -> {q:5.1f} mg/g   (claim is {CLAIM/q:.0f}x this monolayer)")
    print(f"\nTo hold {CLAIM:.0f} mg/g as a monolayer you would need "
          f"~{sa_needed(CLAIM, 0.30):.0f} m2/g. The material has {SA} m2/g "
          f"({sa_needed(CLAIM,0.30)/SA:.0f}x short).")

    print("\nSo the >2600 mg/g is not surface adsorption: it is PFOA-PFOA aggregation "
          "concentrated onto the cationic framework.")
    print(f"It appears only above the {BREAK_MGL[0]}-{BREAK_MGL[1]} mg/L two-phase break, which is:")
    print(f"  - ~1000x higher than environmental PFOA (ng/L to ug/L), so it is not the number "
          f"that governs real water treatment;")
    print(f"  - still BELOW PFOA's CMC (~{CMC_MGL[0]}-{CMC_MGL[1]} mg/L), so it is framework-TEMPLATED "
          f"aggregation, not bulk micellization.")
    print("\nConstructive read: the authors already invoke aggregation ('cooperative adsorption'),")
    print("so the mechanism is broadly right; the correction is that the >2600 mg/g HEADLINE is a")
    print("high-concentration aggregation artifact. The material's real, defensible value is its")
    print("fluorescent PFOA sensing (LOD 1.8 ug/L) and trace-level electrostatic capture, not the")
    print("eye-catching capacity number.")


if __name__ == "__main__":
    main()
