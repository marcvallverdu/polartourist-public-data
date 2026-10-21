# Data dictionary

Exactly five rows, one per NOAA geomagnetic storm level. UTF-8, CSV header, JSON array. No nulls or missing-value sentinel.

| Field | Type | Meaning |
|---|---|---|
| level | string | G1 through G5, unique categorical severity |
| label | string | Minor, Moderate, Strong, Severe, Extreme |
| kp_display | string | Source display label; `8 or 9−` includes a minus variant, NOT a range or probability |
| sort_order | integer (CSV parsed) | 1–5 ordering only, no physical units |
| source_owner | string | NOAA / NWS Space Weather Prediction Center |
| source_url | URL | Official table |
| checked_date | ISO date | Human/source verification date, not observation time |

No timestamps of storms, sighting events, latitude probabilities, annual means or cycle maxima are included.
