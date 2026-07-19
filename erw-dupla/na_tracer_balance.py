"""
Na-tracer stoichiometric balance for the Dupla et al. (2025) basalt ERW vineyard trial.

Dupla, Bertagni, Grand, "Three Years of Field Trials Indicate a Sustained Enhanced Rock Weathering
Signal with Limited CO2 Removal," Environ. Sci. Technol. 59:25751 (2025), doi:10.1021/acs.est.5c09820.

The anomaly: porewater sodium ran ~3x higher in treated plots (dissolution is unambiguous), yet
pH, DIC, Ca, and Mg -- the standard ERW-MRV proxies -- showed no significant increase. Where did
the alkalinity go?

The key insight needs no absolute concentrations, only the ratio in which basalt releases cations.
Na is a conservative tracer: it barely sorbs to exchange sites and is not a plant macronutrient, so
it stays in solution and reveals dissolution. Ca and Mg are strongly retained (cation exchange +
plant uptake) in a base-poor, biologically active vineyard soil. Basalt releases Ca+Mg at many
times the equivalents of Na, and those divalent cations carry most of the weathering alkalinity. So
if Na rises but Ca/Mg/alkalinity do not, most of the alkalinity signal is being intercepted before
it reaches the porewater probes -- the proxies systematically under-detect the dissolution.

Run: python na_tracer_balance.py   (standard library only)
Caveat: uses TYPICAL basalt composition (the paper's specific basalt and exact porewater Na are in
the paywalled SI; the RATIO below is robust across basalts, so the conclusion is not sensitive to
it). Order-of-magnitude reframing, not a plant mass balance.
"""

# Typical basalt oxide composition (wt %), mid-literature:
NA2O, CAO, MGO = 3.0, 10.0, 7.0
# oxide -> element mass fraction
NA = NA2O/100 * (2*22.99)/(2*22.99+16.00)
CA = CAO/100 * 40.08/(40.08+16.00)
MG = MGO/100 * 24.31/(24.31+16.00)
# equivalent weights (g/eq): Na+ =23.0, Ca2+ =20.04, Mg2+ =12.15
APPLIED_T_HA = 20.0
CO2_MEASURED_KG_HA_YR = 100.0


def per_ha(frac):  # kg element per ha from the applied basalt (if fully dissolved)
    return frac * APPLIED_T_HA * 1000.0


def eq_per_kg(frac, eqwt):  # charge equivalents per kg basalt
    return (frac * 1000.0) / eqwt


def main():
    na_eq = eq_per_kg(NA, 23.00)
    ca_eq = eq_per_kg(CA, 20.04)
    mg_eq = eq_per_kg(MG, 12.15)
    div_eq = ca_eq + mg_eq
    tot_eq = na_eq + div_eq

    print(f"Typical basalt: Na2O {NA2O}%, CaO {CAO}%, MgO {MGO}%  (Na {NA*100:.1f}%, Ca {CA*100:.1f}%, Mg {MG*100:.1f}% by mass)")
    print(f"Applied: {APPLIED_T_HA} t/ha  ->  Na {per_ha(NA):.0f}, Ca {per_ha(CA):.0f}, Mg {per_ha(MG):.0f} kg/ha (full-dissolution inventory)\n")

    print("Charge equivalents released per kg basalt dissolved:")
    print(f"  Na+  {na_eq:.2f} eq   Ca2+ {ca_eq:.2f} eq   Mg2+ {mg_eq:.2f} eq")
    print(f"  -> Ca+Mg release is {div_eq/na_eq:.1f}x the Na release (by charge equivalents)")
    print(f"  -> divalent cations carry {div_eq/tot_eq*100:.0f}% of the total cation-equivalent (=alkalinity) signal\n")

    print("So a porewater signature of '3x Na, flat Ca/Mg/alkalinity' means the Ca+Mg dissolved")
    print(f"alongside the Na (~{div_eq/na_eq:.0f}x its equivalents) is being retained by soil exchange")
    print(f"+ plant uptake, taking ~{div_eq/tot_eq*100:.0f}% of the weathering alkalinity with it. The")
    print("standard DIC/Ca/Mg porewater proxies therefore UNDER-DETECT the dissolution; Na (or another")
    print("conservative tracer) is the correct anchor for the mass balance in base-poor cropland.\n")

    print("The decisive open question (which this reframes, not resolves):")
    print("  Retained is not the same as durably removed. If the exchange-held / plant-cycled Ca+Mg")
    print("  eventually leaches as bicarbonate to the ocean, the ~100 kg CO2/ha/yr DIC estimate")
    print("  under-counts durable CDR. If it is held indefinitely in the soil or respired back with")
    print("  CO2, the pessimistic number may be right. Measuring the FATE of the retained alkalinity")
    print("  (exchangeable-cation pools + deep drainage flux), not just porewater DIC, is the study")
    print("  the Na anomaly calls for.")


if __name__ == "__main__":
    main()
