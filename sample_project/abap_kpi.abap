* KPI: Polymer Melt Flow Index (MFI) Variance
* Math Formula: MFI Variance is not directly calculated in this snippet. See code for context.
DATA: lv_var   TYPE f,
      gas_recovered_m3 TYPE f VALUE 120.0,
      total_gas_m3     TYPE f VALUE 450.0,
      lv_rate          TYPE f.

lv_var = 0.0. " placeholder for variance example

* KPI: Flare Gas Recovery Rate (%)
* Math Formula: (Gas Recovered / Total Gas) * 100
" Example KPI expression so the formula renders:
lv_rate = ( gas_recovered_m3 / total_gas_m3 ) * 100.

WRITE: / 'MFI Variance (example):', lv_var.
WRITE: / 'Flare Gas Recovery Rate (%):', lv_rate.