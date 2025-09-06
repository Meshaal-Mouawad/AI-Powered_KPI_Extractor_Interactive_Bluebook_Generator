-- KPI: Energy Intensity Index (EII)
-- Example pattern: SELECT ... AS kpi_...
SELECT 
    total_energy_mmbtu / NULLIF(reference_energy_mmbtu, 0) AS kpi_eii
FROM unit_energy_summary;