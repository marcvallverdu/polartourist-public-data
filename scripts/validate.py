import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def validate():
    rows=json.loads((ROOT/'data/noaa_geomagnetic_scale.json').read_text())
    with (ROOT/'data/noaa_geomagnetic_scale.csv').open(newline='') as f: flat=list(csv.DictReader(f))
    assert len(rows)==len(flat)==5
    expected=list(zip(['G1','G2','G3','G4','G5'],['Minor','Moderate','Strong','Severe','Extreme'],['5','6','7','8 or 9−','9']))
    assert [(r['level'],r['label'],r['kp_display']) for r in rows]==expected
    for i,(a,b) in enumerate(zip(rows,flat),1):
        b['sort_order']=int(b['sort_order']); assert a==b
        assert a['sort_order']==i
        assert a['source_url']=='https://www.spaceweather.gov/noaa-scales-explanation'
        assert a['source_owner']=='NOAA / NWS Space Weather Prediction Center'
        assert a['checked_date']=='2026-10-21'
    return rows
if __name__=='__main__': print(f'PASS: {len(validate())} NOAA rows; exact mapping, provenance, CSV/JSON parity')
