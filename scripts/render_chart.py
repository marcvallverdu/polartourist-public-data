from pathlib import Path
from html import escape
from validate import validate, ROOT
rows=validate()
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="600" viewBox="0 0 1000 600" role="img" aria-labelledby="title desc">','<title id="title">NOAA geomagnetic storm scale: Kp is not a sighting probability</title>','<desc id="desc">G1 Minor Kp 5; G2 Moderate 6; G3 Strong 7; G4 Severe 8 or 9 minus; G5 Extreme 9. Source NOAA SWPC. Text reference, no forecast.</desc>','<rect width="1000" height="600" fill="#081827"/>','<g fill="#ffffff" font-family="Arial, sans-serif">','<text x="45" y="58" font-size="29">Geomagnetic storms: read the label, not a probability</text>','<text x="45" y="94" font-size="18">NOAA G scale • reference thresholds, not current conditions</text>']
for i,r in enumerate(rows):
 y=160+i*65
 parts += [f'<text x="55" y="{y}" font-size="26">{escape(r["level"])}</text>',f'<text x="180" y="{y}" font-size="26">{escape(r["label"])}</text>',f'<text x="530" y="{y}" font-size="26">Kp {escape(r["kp_display"])}</text>']
parts+=['<text x="45" y="490" font-size="18">9− belongs to G4; exact 9 belongs to G5. Neither guarantees visible aurora.</text>','<text x="45" y="525" font-size="16">Source: NOAA / NWS SWPC • spaceweather.gov/noaa-scales-explanation</text>','<text x="45" y="552" font-size="16">Layout: PolarTourist, CC BY 4.0 • NOAA facts public domain • checked 2026-10-21</text>','<text x="45" y="578" font-size="14">polartourist.com/blog/northern-lights-statistics-resource-2026 • no NOAA endorsement</text>','</g></svg>']
(ROOT/'charts').mkdir(exist_ok=True)
(ROOT/'charts/noaa-g-scale.svg').write_text('\n'.join(parts)+'\n')
print('Rendered charts/noaa-g-scale.svg')
