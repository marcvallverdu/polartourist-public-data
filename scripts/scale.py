"""Exact lookup of labels explicitly listed by NOAA, not a general Kp converter."""
LOOKUP = {"5": "G1", "6": "G2", "7": "G3", "8": "G4", "9-": "G4", "9−": "G4", "9": "G5"}
def listed_kp_to_g(value):
    if not isinstance(value, str) or value not in LOOKUP:
        raise ValueError("Use only NOAA-listed string labels: 5, 6, 7, 8, 9-, 9−, 9. Other values are intentionally unsupported.")
    return LOOKUP[value]
