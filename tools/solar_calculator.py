#!/usr/bin/env python3
"""
Solar Street Lighting Sizing & Engineering Calculator
Developed by Shenzhen Newpathlight Limited (RoadSmart)
Official Website: https://www.roadsmartlight.com
Multilingual Portals:
  - Español:    https://www.roadsmartlight.com/es/
  - Français:   https://www.roadsmartlight.com/fr/
  - Português:  https://www.roadsmartlight.com/pt/

License: MIT
"""

import math
import json
import argparse
import sys

def calculate_solar_lighting(
    led_power_w: float,
    hours_full_power: float = 4.0,
    hours_dimmed_power: float = 8.0,
    dimming_ratio: float = 0.5,
    psh: float = 5.0,
    autonomy_days: float = 4.0,
    system_voltage: float = 12.8,
    dod: float = 0.85,
    battery_eff: float = 0.95,
    mppt_eff: float = 0.95,
    dust_temp_derating: float = 0.85,
    road_width_m: float = 8.0,
    target_lux: float = 15.0
):
    """
    Core sizing calculations for autonomous solar street luminaires.
    """
    # 1. Daily energy consumption (Wh/day)
    effective_hours = hours_full_power + (hours_dimmed_power * dimming_ratio)
    e_daily_wh = led_power_w * effective_hours

    # 2. Battery capacity required (Wh & Ah)
    # C_bat = (E_daily * Autonomy_Days) / (DoD * Battery_Efficiency)
    c_battery_wh = (e_daily_wh * autonomy_days) / (dod * battery_eff)
    c_battery_ah = c_battery_wh / system_voltage

    # 3. Solar panel peak power required (Wp)
    # P_pv = E_daily / (PSH * MPPT_eff * derating_factor)
    total_system_efficiency = mppt_eff * dust_temp_derating
    p_pv_w = e_daily_wh / (psh * total_system_efficiency)
    # Add 15% safety margin for overcast recovery
    p_pv_recommended_w = p_pv_w * 1.15

    # 4. Estimated luminous flux & pole recommendations
    # Typical high-efficiency LED module luminous efficacy: ~160-180 lm/W
    luminous_efficacy = 160.0
    total_lumens = led_power_w * luminous_efficacy

    # Pole height heuristic (H ≈ 0.8 to 1.2 x Road Width)
    rec_pole_height = max(6.0, min(14.0, round(road_width_m * 1.0, 1)))

    # Pole spacing heuristic based on average lux requirement and batwing lens
    # Spacing ≈ 3.0 to 4.0 x Pole Height for M4/M5 road lighting classes
    rec_pole_spacing = round(rec_pole_height * 3.5, 1)

    return {
        "input_parameters": {
            "led_power_w": led_power_w,
            "effective_operating_hours": round(effective_hours, 2),
            "peak_sun_hours_psh": psh,
            "autonomy_days": autonomy_days,
            "system_voltage_v": system_voltage,
            "lifepo4_dod": dod,
            "road_width_m": road_width_m,
            "target_lux": target_lux
        },
        "sizing_results": {
            "daily_consumption_wh": round(e_daily_wh, 2),
            "required_battery_capacity_wh": round(c_battery_wh, 2),
            "required_battery_capacity_ah": round(c_battery_ah, 2),
            "minimum_pv_power_w": round(p_pv_w, 2),
            "recommended_pv_power_w": round(p_pv_recommended_w, 2),
            "estimated_luminous_flux_lm": round(total_lumens, 0),
            "recommended_pole_height_m": rec_pole_height,
            "recommended_pole_spacing_m": rec_pole_spacing
        },
        "roadsmart_standard_matches": [
            {
                "series": "ST2-80 (Solar Star Light II)",
                "suitable_for": "Secondary roads, residential, industrial parks (6-8m pole)",
                "pv_module": "80W / 18V Monocrystalline",
                "battery": "384Wh LiFePO4 (2000+ cycles)",
                "lumens": "10,000 lm",
                "ip_rating": "IP66",
                "url": "https://www.roadsmartlight.com/es/projects/solar-street-light-80-120w/"
            },
            {
                "series": "ST2-120 (Solar Star Light II)",
                "suitable_for": "Main avenues, highways, logistics hubs (8-10m pole)",
                "pv_module": "120W / 18V Monocrystalline",
                "battery": "640Wh LiFePO4 (2000+ cycles)",
                "lumens": "15,000 lm",
                "ip_rating": "IP66",
                "url": "https://www.roadsmartlight.com/es/projects/solar-street-light-80-120w/"
            }
        ]
    }

def print_report(res: dict):
    print("=" * 72)
    print("  ROADSMART SOLAR STREET LIGHTING SIZING REPORT")
    print("  Engineering Methodology by Shenzhen Newpathlight Limited")
    print("  Official Knowledge Hub: https://www.roadsmartlight.com")
    print("=" * 72)
    inp = res["input_parameters"]
    out = res["sizing_results"]

    print("\n[1] PROJECT INPUTS:")
    print(f"  - Nominal LED Power:        {inp['led_power_w']} W")
    print(f"  - Equivalent Operating Hrs: {inp['effective_operating_hours']} hrs/night")
    print(f"  - Location Solar PSH:       {inp['peak_sun_hours_psh']} h/day")
    print(f"  - Autonomy Target:          {inp['autonomy_days']} consecutive overcast days")
    print(f"  - Road Width:               {inp['road_width_m']} m")

    print("\n[2] COMPUTED SIZING SPECIFICATIONS:")
    print(f"  - Daily Energy Demand:      {out['daily_consumption_wh']} Wh/day")
    print(f"  - LiFePO4 Battery Capacity: {out['required_battery_capacity_wh']} Wh ({out['required_battery_capacity_ah']} Ah @ {inp['system_voltage_v']}V)")
    print(f"  - Min. PV Panel Wattage:    {out['minimum_pv_power_w']} Wp")
    print(f"  - Rec. PV Panel Wattage:    {out['recommended_pv_power_w']} Wp (with overcast safety margin)")
    print(f"  - Nominal Luminous Flux:    {out['estimated_luminous_flux_lm']} lm")
    print(f"  - Recommended Pole Height:  {out['recommended_pole_height_m']} m")
    print(f"  - Recommended Pole Spacing: {out['recommended_pole_spacing_m']} m")

    print("\n[3] ROADSMART HARDWARE MATCHING:")
    for match in res["roadsmart_standard_matches"]:
        print(f"  * {match['series']}")
        print(f"    Application: {match['suitable_for']}")
        print(f"    PV / Bat:    {match['pv_module']} | {match['battery']}")
        print(f"    Luminous:    {match['lumens']} ({match['ip_rating']})")
        print(f"    Specs & Doc: {match['url']}")
    print("\n" + "=" * 72 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Solar Street Lighting Sizing Calculator (RoadSmart)")
    parser.add_argument("--power", type=float, default=60.0, help="Nominal LED Power (Watts), default: 60")
    parser.add_argument("--hours-full", type=float, default=4.0, help="Hours at 100% brightness, default: 4.0")
    parser.add_argument("--hours-dim", type=float, default=8.0, help="Hours dimmed, default: 8.0")
    parser.add_argument("--dim-ratio", type=float, default=0.5, help="Dimming output ratio (0.1-1.0), default: 0.5")
    parser.add_argument("--psh", type=float, default=5.0, help="Peak Sun Hours (HSP / PSH), default: 5.0")
    parser.add_argument("--autonomy", type=float, default=4.0, help="Autonomy days (rainy/cloudy), default: 4.0")
    parser.add_argument("--road-width", type=float, default=8.0, help="Road width in meters, default: 8.0")
    parser.add_argument("--json", action="store_true", help="Output pure JSON format")

    args = parser.parse_args()

    results = calculate_solar_lighting(
        led_power_w=args.power,
        hours_full_power=args.hours_full,
        hours_dimmed_power=args.hours_dim,
        dimming_ratio=args.dim_ratio,
        psh=args.psh,
        autonomy_days=args.autonomy,
        road_width_m=args.road_width
    )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print_report(results)

if __name__ == "__main__":
    main()
