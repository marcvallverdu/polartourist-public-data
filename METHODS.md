# Methods and reproducibility

1. Read the existing public PolarTourist compilation and the current NOAA official scale table.
2. Retain only the five geomagnetic level names, descriptions and Kp display labels. Preserve `9−`; NOAA also writes `9-`.
3. Store ascending categorical order, source owner/URL and check date in CSV and JSON.
4. Validate exact expected scale mapping, provenance, row count and CSV/JSON parity. Validation does not establish continuous freshness or scientific independence.
5. Render an accessible SVG text table, not a bar chart of string Kp values; ordinal severity is not a linear quantitative magnitude.
6. Execute notebook code cells offline in order and assert the crucial G4/G5 distinction.

No inference, interpolation, forecasting, observation sampling, sighting model or external runtime API call. No costs or accounts needed. The notebook runner executes this repository's code cells, not arbitrary untrusted notebooks, and does not emulate a Jupyter kernel.

Sunspot summaries are outside this release because of upstream non-commercial licence scope. Their concepts are explained without redistributing values. The originally proposed SILSO comparison remains rights-gated rather than silently claimed complete.
