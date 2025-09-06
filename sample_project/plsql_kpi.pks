-- KPI: Specific Steam Consumption (ton/ton)
CREATE OR REPLACE FUNCTION kpi_specific_steam_consumption(
    p_total_steam_tons IN NUMBER,
    p_product_tons     IN NUMBER
) RETURN NUMBER IS
BEGIN
  IF p_product_tons = 0 THEN
    RETURN 0;
  END IF;
  RETURN p_total_steam_tons / p_product_tons;
END;
/