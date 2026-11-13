# Solar Street Lighting Sizing & Engineering Calculation Toolkit
### *Guía y Herramientas de Cálculo de Alumbrado Público Solar en Español, Français y Português*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Languages](https://img.shields.io/badge/Languages-ES%20%7C%20FR%20%7C%20PT%20%7C%20EN-green.svg)](#multilingual-knowledge-portals)
[![Standard](https://img.shields.io/badge/Standard-CIE%20%7C%20RETILAP%20%7C%20NOM--013--ENER%20%7C%20NBR--5101-orange.svg)](#regional-engineering-standards)
[![Official Hub](https://img.shields.io/badge/Official%20Hub-RoadSmart-red.svg)](https://www.roadsmartlight.com)

Open-source engineering library, sizing algorithms, and technical references for municipal, highway, and rural solar street lighting systems. Tailored for municipal procurement engineers, EPC contractors, and renewable energy consultants operating in **Latin America (Español)**, **Francophone Africa (Français)**, and **Lusophone markets (Português)**.

Maintained by **Shenzhen Newpathlight Limited** under the **RoadSmart** brand.

---

## Multilingual Knowledge Portals

Access authoritative technical documentation, DIALux simulation files, and tender procurement guidelines on our official domain:

| Language / Region | Official Portal | Sizing & Verification Resources | Featured Hardware Baseline |
| :--- | :--- | :--- | :--- |
| 🇪🇸 **Español**<br>(México, Colombia, Chile, España) | [roadsmartlight.com/es/](https://www.roadsmartlight.com/es/) | [Lista de Comprobación para Licitaciones](https://www.roadsmartlight.com/es/resources/procurement-checklist/) | [Farola Solar 80W-120W ST2](https://www.roadsmartlight.com/es/projects/solar-street-light-80-120w/) |
| 🇫🇷 **Français**<br>(Sénégal, Côte d'Ivoire, Maroc, UEMOA) | [roadsmartlight.com/fr/](https://www.roadsmartlight.com/fr/) | [Liste de Contrôle d'Approvisionnement](https://www.roadsmartlight.com/fr/resources/procurement-checklist/) | [Lampadaire Solaire 80W-120W ST2](https://www.roadsmartlight.com/fr/projects/solar-street-light-80-120w/) |
| 🇵🇹 **Português**<br>(Brasil, Angola, Moçambique, Portugal) | [roadsmartlight.com/pt/](https://www.roadsmartlight.com/pt/) | [Checklist de Aquisição para Engenharia](https://www.roadsmartlight.com/pt/resources/procurement-checklist/) | [Poste de Iluminação Solar 80W-120W ST2](https://www.roadsmartlight.com/pt/projects/solar-street-light-80-120w/) |
| 🌐 **International / English** | [roadsmartlight.com](https://www.roadsmartlight.com) | [Engineering Knowledge Base](https://www.roadsmartlight.com) | [Solar Star Light II (ST2 Series)](https://www.roadsmartlight.com) |

---

## Table of Contents

1. [Mathematical Sizing Methodology](#mathematical-sizing-methodology)
   - [Daily Energy Consumption](#1-daily-energy-consumption)
   - [LiFePO4 Battery Storage Sizing](#2-lifepo4-battery-storage-sizing)
   - [Solar Panel Peak Wattage Sizing](#3-solar-panel-peak-wattage-sizing)
   - [Pole Geometry & Luminaire Optics](#4-pole-geometry--luminaire-optics)
2. [Regional Engineering Standards](#regional-engineering-standards)
3. [Interactive CLI Sizing Tool](#interactive-cli-sizing-tool)
4. [Hardware Engineering Baseline](#hardware-engineering-baseline)
5. [Worked Case Studies](#worked-case-studies)
   - [Sonora Highway, Mexico (ES)](#case-1-sonora-highway-mexico)
   - [Thiès-Dakar Arterial Road, Senegal (FR)](#case-2-thiès-dakar-arterial-road-senegal)
   - [Coastal Corridor Bahia, Brazil (PT)](#case-3-coastal-corridor-bahia-brazil)
6. [Citation & License](#citation--license)

---

## Mathematical Sizing Methodology

Reliable solar street lighting requires strict energy balance verification to avoid premature dark-out during adverse meteorological seasons.

```
+-------------------------------------------------------------+
|                     SOLAR STREET LIGHT                      |
|                                                             |
|   [ Photovoltaic Panel (Wp) ]                               |
|               |                                             |
|               v                                             |
|   [ MPPT Digital Controller (η >= 98%) ]                    |
|               |                                             |
|       +-------+-------+                                     |
|       |               |                                     |
|       v               v                                     |
| [ LiFePO4 Battery ]   [ LED Optical Engine (>= 160 lm/W) ]  |
|   (DoD <= 85%)          (Batwing Polarization Lens)         |
+-------------------------------------------------------------+
```

### 1. Daily Energy Consumption

The luminaire nocturnal load profile accounts for dynamic step-dimming controlled by intelligent power management:

$$E_{daily} = P_{LED} \times \left( t_{100\%} + t_{dim} \times k_{dim} \right)$$

- $P_{LED}$: Nominal electrical power drawn by the LED engine (W).
- $t_{100\%}$: Operating hours at full brightness during peak traffic hours (e.g. 18:00 - 22:00 = 4h).
- $t_{dim}$: Operating hours in power-saving mode (e.g. 22:00 - 06:00 = 8h).
- $k_{dim}$: Dimming ratio (typically 0.3 to 0.5 with microwave/PIR sensor override).

### 2. LiFePO4 Battery Storage Sizing

Grade-A Lithium Iron Phosphate ($\text{LiFePO}_4$) cells provide high thermal stability (-20°C to +60°C) and exceed 2,000 cycles at 80% Depth of Discharge (DoD):

$$C_{battery} (\text{Wh}) = \frac{E_{daily} \times N_{autonomy}}{\text{DoD} \times \eta_{battery}}$$

- $N_{autonomy}$: Consecutive cloudy/rainy days requirement without solar recharge ($3 \le N_{autonomy} \le 5$).
- $\text{DoD}$: Maximum allowable depth of discharge ($0.80 \le \text{DoD} \le 0.85$).
- $\eta_{battery}$: Coulombic round-trip efficiency ($\approx 0.95$).

### 3. Solar Panel Peak Wattage Sizing

Panel generation depends on the location's Peak Sun Hours (PSH / HSP) for the worst-case month (minimum seasonal insolation):

$$P_{PV} (\text{Wp}) = \frac{E_{daily}}{\text{PSH}_{min} \times \eta_{MPPT} \times f_{derating}} \times k_{safety}$$

- $\text{PSH}_{min}$: Lowest monthly solar radiation (kWh/m²/day) from NASA SSE or local meteorological institutes.
- $\eta_{MPPT}$: MPPT charge controller conversion efficiency ($\ge 0.95$).
- $f_{derating}$: Combined losses including dust accumulation, surface temperature coefficient, and wiring ($\approx 0.85$).
- $k_{safety}$: Overcast recovery factor ensuring rapid recharge after rainstorms ($\approx 1.15$).

### 4. Pole Geometry & Luminaire Optics

To achieve road illuminance uniformity without creating bright spots or dark zones:

- **Mounting Height ($H$)**: $H \approx 0.8 \times W$ to $1.2 \times W$ (where $W$ is the effective road width).
- **Pole Spacing ($S$)**: $S \approx 3.2 \times H$ to $4.0 \times H$ using polarized batwing lenses (Type II / Type III distribution).

---

## Regional Engineering Standards

| Jurisdiction / Region | Standard Code | Mandatory Technical Verification |
| :--- | :--- | :--- |
| **🇲🇽 México** | **NOM-013-ENER-2013** / **NOM-031-ENER-2012** | Roadway energy efficiency (W/m²), road surface luminance, overall uniformity $U_0 \ge 0.4$. |
| **🇨🇴 Colombia** | **RETILAP** | Technical Regulation of Lighting and Public Lighting; mandatory laboratory photometric test reports (IES) and IP66/IK08 ratings. |
| **🇨🇱 Chile** | **DS 43/2012 MMA** | Strict upper light output ratio ($ULOR \le 1\%$), warm correlated color temperature ($\le 3000\text{K}$) to prevent astronomical light pollution. |
| **🇧🇷 Brasil** | **ABNT NBR 5101** | Classes of public lighting (V1 through V5), lateral and longitudinal illuminance uniformity. |
| **🌍 Afrique UEMOA** | **Normes Régionales CEDEAO/UEMOA** | Off-grid public lighting autonomy ($\ge 4$ days), high ambient temperature withstand ($> 45^\circ\text{C}$). |

---

## Interactive CLI Sizing Tool

This repository includes a standalone Python & Node.js calculation suite:

```bash
# Clone the repository
git clone https://github.com/kaosmys129/solar-street-lighting-design-calc.git
cd solar-street-lighting-design-calc

# Run standard sizing calculation
python3 tools/solar_calculator.py --power 80 --psh 5.0 --autonomy 4 --road-width 8.0

# Export structured JSON data for DIALux / engineering documentation
python3 tools/solar_calculator.py --power 120 --psh 4.8 --autonomy 5 --json
```

---

## Hardware Engineering Baseline

Standard industrial parameters established by RoadSmart for municipal and commercial deployments:

| Engineering Parameter | ST2-80 Specification | ST2-120 Specification |
| :--- | :--- | :--- |
| **Monocrystalline PV Panel** | 80W / 18V | 120W / 18V |
| **Battery Chemistry** | $\text{LiFePO}_4$ (Lithium Iron Phosphate) | $\text{LiFePO}_4$ (Lithium Iron Phosphate) |
| **Battery Capacity** | 384 Wh (2000+ deep cycles) | 640 Wh (2000+ deep cycles) |
| **Nominal Luminous Flux** | 10,000 lm | 15,000 lm |
| **Operating Temperature** | -20°C to +60°C | -20°C to +60°C |
| **Ingress Protection** | IP66 (Dust-tight, heavy jet water) | IP66 (Dust-tight, heavy jet water) |
| **Recommended Pole Height** | 6.0 m – 8.0 m | 8.0 m – 10.0 m |
| **Recommended Spacing** | 20.0 m – 35.0 m | 25.0 m – 40.0 m |
| **Official Specifications** | [ST2-80 Specs](https://www.roadsmartlight.com/es/projects/solar-street-light-80-120w/) | [ST2-120 Specs](https://www.roadsmartlight.com/fr/projects/solar-street-light-80-120w/) |

---

## Worked Case Studies

Detailed project calculations and configuration JSON files are located in [`examples/`](./examples):

1. **[Case 1: Sonora Highway, Mexico (ES)](./examples/mexico_80w_sonora_case.json)**:
   - Target: NOM-013-ENER Class M4 ($E_{avg} \ge 15\text{ lux}$).
   - Configuration: 80W luminaire, $H=7.5\text{m}$, spacing $= 28\text{m}$, autonomy $= 4$ days.
2. **[Case 2: Thiès-Dakar Arterial Road, Senegal (FR)](./examples/senegal_120w_thies_case.json)**:
   - Target: UEMOA Class M4 ($E_{avg} \ge 15\text{ lux}$).
   - Configuration: 120W luminaire, $H=8.5\text{m}$, spacing $= 30\text{m}$, autonomy $= 5$ days.
3. **[Case 3: Coastal Corridor Bahia, Brazil (PT)](./examples/brazil_100w_bahia_case.json)**:
   - Target: ABNT NBR 5101 Class V3 ($E_{avg} \ge 15\text{ lux}$, $U_0 \ge 0.4$).
   - Configuration: 80W/120W dual luminaire, $H=8.0\text{m}$, spacing $= 28\text{m}$, autonomy $= 4$ days.

---

## In-Depth Regional Documentation

- 🇪🇸 [Guía Completa de Dimensionamiento en Español](./docs/es/guia-calculo-alumbrado-solar.md)
- 🇫🇷 [Guide Technique de Dimensionnement en Français](./docs/fr/guide-dimensionnement-eclairage-solaire.md)
- 🇵🇹 [Guia Completo de Dimensionamento em Português](./docs/pt/guia-calculo-iluminacao-solar.md)
- 🌐 [Global Engineering Specifications in English](./docs/en/engineering-specifications.md)

---

## Citation & License

If you use this engineering framework, algorithms, or technical datasets in public tenders, academic papers, or feasibility studies, please cite our official repository:

```bibtex
@misc{roadsmart_solar_sizing_2026,
  author = {Shenzhen Newpathlight Limited},
  title = {Solar Street Lighting Engineering Design & Sizing Calculation Toolkit},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kaosmys129/solar-street-lighting-design-calc}},
  url = {https://www.roadsmartlight.com}
}
```

Licensed under the [MIT License](./LICENSE).

---
*Maintained by the Engineering Division of Shenzhen Newpathlight Limited (RoadSmart). For formal tender support, IES photometric files, or custom engineering inquiries, visit [roadsmartlight.com](https://www.roadsmartlight.com).*
