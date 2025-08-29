# petrochemical_plant_operations.py
# A simulation of various data processing and operational calculations for a petrochemical plant.

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# ==============================================================================
# NON-KPI UTILITY FUNCTIONS
# These functions represent typical data handling and logging tasks in a plant.
# ==============================================================================

def load_sensor_data(plant_area: str, hours: int = 24) -> pd.DataFrame:
    """
    Simulates loading time-series data from a plant's sensor database.
    This is a standard data ingestion task and does not calculate a KPI.
    """
    print(f"Loading sensor data for {plant_area} area...")
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=hours)
    timestamps = pd.to_datetime(np.linspace(start_time.timestamp(), end_time.timestamp(), hours * 60), unit='s')

    data = {
        'timestamp': timestamps,
        'temperature_c': np.random.normal(loc=150, scale=5, size=len(timestamps)),
        'pressure_bar': np.random.normal(loc=25, scale=1, size=len(timestamps)),
        'flow_rate_m3h': np.random.normal(loc=500, scale=25, size=len(timestamps)),
    }
    return pd.DataFrame(data)


def log_maintenance_event(equipment_id: str, description: str):
    """
    Simulates logging a maintenance event to a plant's maintenance system (CMMS).
    This is a critical operational task but not a KPI calculation.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"LOG [{timestamp}] | Maintenance on {equipment_id}: {description}")


# ==============================================================================
# KPI CALCULATION FUNCTIONS
# These functions calculate specific Key Performance Indicators for the plant.
# ==============================================================================

# --- Production and Yield KPIs ---

def calculate_ethylene_yield(feedstock_volume_tons: float, ethylene_produced_tons: float) -> float:
    """Calculates the percentage yield of ethylene from a given amount of feedstock."""
    if feedstock_volume_tons == 0:
        return 0.0
    # KPI: Ethylene Yield Percentage
    # Measures the efficiency of the steam cracker in converting feedstock to the primary product.
    yield_percentage = (ethylene_produced_tons / feedstock_volume_tons) * 100
    return yield_percentage


def calculate_propylene_to_ethylene_ratio(propylene_produced_tons: float, ethylene_produced_tons: float) -> float:
    """Calculates the P/E ratio, a key indicator of product mix."""
    if ethylene_produced_tons == 0:
        return 0.0
    # KPI: Propylene to Ethylene (P/E) Ratio
    # This ratio is critical for aligning production with market demand and maximizing profitability.
    pe_ratio = propylene_produced_tons / ethylene_produced_tons
    return pe_ratio


def calculate_daily_throughput(total_feedstock_processed_tons: float, hours_online: float) -> float:
    """Calculates the average daily processing rate of the plant."""
    if hours_online == 0:
        return 0.0
    # KPI: Daily Feedstock Throughput (tons/day)
    # Measures the total volume of raw material the plant is processing over a 24-hour period.
    throughput = (total_feedstock_processed_tons / hours_online) * 24
    return throughput


# --- Energy and Utilities KPIs ---

def calculate_specific_steam_consumption(steam_used_tons: float, product_produced_tons: float) -> float:
    """Calculates how much steam is used per ton of product."""
    if product_produced_tons == 0:
        return 0.0
    # KPI: Specific Steam Consumption (ton/ton)
    # A primary indicator of energy efficiency in the separation and reaction sections.
    ssc = steam_used_tons / product_produced_tons
    return ssc


def calculate_energy_intensity_index(actual_energy_consumed_gj: float, standard_energy_gj: float) -> float:
    """Compares actual energy consumption to a theoretical or historical standard."""
    if standard_energy_gj == 0:
        return 1.0
    # KPI: Energy Intensity Index (EII)
    # A value > 1.0 indicates higher-than-standard energy consumption, signaling inefficiency.
    eii = actual_energy_consumed_gj / standard_energy_gj
    return eii


def calculate_cooling_water_effectiveness(inlet_temp: float, outlet_temp: float) -> float:
    """Calculates the temperature difference, indicating heat exchanger performance."""
    # KPI: Cooling Water Delta-T (°C)
    # A lower-than-expected Delta-T can indicate fouling or scaling in heat exchangers.
    delta_t = outlet_temp - inlet_temp
    return delta_t


# --- Asset and Reliability KPIs ---

def calculate_mean_time_between_failures(operating_hours: int, number_of_failures: int) -> float:
    """Calculates the average time a piece of equipment operates before failing."""
    if number_of_failures == 0:
        return operating_hours
    # KPI: Mean Time Between Failures (MTBF)
    # A core metric for assessing the reliability and maintenance strategy of critical equipment.
    mtbf = operating_hours / number_of_failures
    return mtbf


def calculate_overall_equipment_effectiveness(availability: float, performance: float, quality: float) -> float:
    """Calculates the OEE, a composite metric for manufacturing productivity."""
    # KPI: Overall Equipment Effectiveness (OEE)
    # Combines availability, performance, and quality to give a single measure of asset productivity.
    oee = availability * performance * quality * 100
    return oee


def calculate_pump_vibration_anomaly_rate(vibration_readings: list) -> float:
    """Calculates the percentage of vibration readings that exceed a safe threshold."""
    if not vibration_readings:
        return 0.0
    vibration_threshold = 5.0  # mm/s
    anomalies = [r for r in vibration_readings if r > vibration_threshold]
    # KPI: Pump Vibration Anomaly Rate
    # A predictive maintenance KPI used to anticipate pump failures and plan proactive maintenance.
    anomaly_rate = (len(anomalies) / len(vibration_readings)) * 100
    return anomaly_rate


# --- Safety and Environmental KPIs ---

def calculate_ltifr(lost_time_injuries: int, total_hours_worked: int) -> float:
    """Calculates the Lost Time Injury Frequency Rate per million hours."""
    if total_hours_worked == 0:
        return 0.0
    # KPI: Lost Time Injury Frequency Rate (LTIFR)
    # A lagging indicator of safety performance, universally used in heavy industry.
    ltifr = (lost_time_injuries / total_hours_worked) * 1_000_000
    return ltifr


def calculate_sox_emissions_rate(sox_emitted_kg: float, flue_gas_volume_m3: float) -> float:
    """Calculates the concentration of SOx in emissions."""
    if flue_gas_volume_m3 == 0:
        return 0.0
    # KPI: SOx Emissions Concentration (kg/m³)
    # Monitors compliance with environmental regulations for sulfur oxide emissions.
    sox_rate = sox_emitted_kg / flue_gas_volume_m3
    return sox_rate


def calculate_flare_gas_recovery_percentage(gas_flared_m3: float, gas_recovered_m3: float) -> float:
    """Calculates the percentage of gas that is recovered instead of flared."""
    total_gas = gas_flared_m3 + gas_recovered_m3
    if total_gas == 0:
        return 100.0
    # KPI: Flare Gas Recovery Rate
    # Measures the effectiveness of systems designed to reduce waste and environmental impact.
    recovery_rate = (gas_recovered_m3 / total_gas) * 100
    return recovery_rate


# --- Product Quality KPIs ---

def calculate_polymer_mfi_variance(mfi_test_results: list) -> float:
    """Calculates the variance in Melt Flow Index, a key polymer quality metric."""
    if not mfi_test_results:
        return 0.0
    # KPI: Polymer Melt Flow Index (MFI) Variance
    # Low variance indicates consistent product quality and process stability.
    variance = np.var(mfi_test_results)
    return variance


def calculate_on_spec_production_rate(on_spec_batches: int, total_batches: int) -> float:
    """Calculates the percentage of production that meets all quality standards."""
    if total_batches == 0:
        return 100.0
    # KPI: On-Spec Production Percentage
    # A direct measure of the quality and reliability of the production process.
    on_spec_rate = (on_spec_batches / total_batches) * 100
    return on_spec_rate


# --- Financial and Cost KPIs ---

def calculate_specific_catalyst_cost(catalyst_cost_usd: float, product_tons: float) -> float:
    """Calculates the cost of catalyst per ton of product."""
    if product_tons == 0:
        return 0.0
    # KPI: Specific Catalyst Cost ($/ton)
    # A key cost control metric, used to optimize catalyst usage and reactor performance.
    scc = catalyst_cost_usd / product_tons
    return scc


def calculate_maintenance_to_operating_cost_ratio(maintenance_cost: float, total_operating_cost: float) -> float:
    """Calculates the ratio of maintenance costs to total operating costs."""
    if total_operating_cost == 0:
        return 0.0
    # KPI: Maintenance to Operating Cost Ratio
    # Used for budgeting and assessing the overall cost impact of the maintenance strategy.
    ratio = (maintenance_cost / total_operating_cost) * 100
    return ratio


# ==============================================================================
# MAIN EXECUTION BLOCK - SIMULATING A DAILY REPORT
# ==============================================================================

if __name__ == "__main__":
    print("--- Generating Daily Petrochemical Plant Operations Report ---")

    # --- Step 1: Load and Process Data (Non-KPI tasks) ---
    cracker_data = load_sensor_data("Cracker Unit")
    log_maintenance_event("P-101A", "Scheduled bearing replacement.")

    # --- Step 2: Calculate and Report KPIs ---
    print("\n--- Production KPIs ---")
    yield_val = calculate_ethylene_yield(feedstock_volume_tons=5000, ethylene_produced_tons=1600)
    print(f"Ethylene Yield: {yield_val:.2f}%")
    pe_ratio_val = calculate_propylene_to_ethylene_ratio(propylene_produced_tons=800, ethylene_produced_tons=1600)
    print(f"P/E Ratio: {pe_ratio_val:.2f}")

    print("\n--- Energy KPIs ---")
    ssc_val = calculate_specific_steam_consumption(steam_used_tons=8000, product_produced_tons=2400)
    print(f"Specific Steam Consumption: {ssc_val:.2f} ton/ton")
    eii_val = calculate_energy_intensity_index(actual_energy_consumed_gj=12000, standard_energy_gj=11500)
    print(f"Energy Intensity Index: {eii_val:.2f}")

    print("\n--- Reliability KPIs ---")
    mtbf_val = calculate_mean_time_between_failures(operating_hours=8760, number_of_failures=3)
    print(f"Compressor K-201 MTBF: {mtbf_val:.0f} hours")
    oee_val = calculate_overall_equipment_effectiveness(availability=0.95, performance=0.98, quality=0.99)
    print(f"Polymerization Reactor R-301 OEE: {oee_val:.1f}%")

    print("\n--- Safety & Environmental KPIs ---")
    ltifr_val = calculate_ltifr(lost_time_injuries=1, total_hours_worked=1_500_000)
    print(f"Plant-wide LTIFR: {ltifr_val:.2f}")
    flare_val = calculate_flare_gas_recovery_percentage(gas_flared_m3=500, gas_recovered_m3=9500)
    print(f"Flare Gas Recovery: {flare_val:.1f}%")

    print("\n--- Quality KPIs ---")
    mfi_tests = [2.1, 2.0, 2.2, 2.1, 1.9, 2.0, 2.1, 2.3]
    mfi_var = calculate_polymer_mfi_variance(mfi_tests)
    print(f"Polypropylene Grade P-500 MFI Variance: {mfi_var:.3f}")

    print("\n--- Financial KPIs ---")
    scc_cost = calculate_specific_catalyst_cost(catalyst_cost_usd=50000, product_tons=2400)
    print(f"Specific Catalyst Cost: ${scc_cost:.2f}/ton")

    print("\n--- Report Generation Complete ---")

