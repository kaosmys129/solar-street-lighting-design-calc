# Solar Street Lighting Engineering Specifications & Design Standards

> **Author / Maintainer**: Shenzhen Newpathlight Limited (RoadSmart)  
> **Official Knowledge Base**: [https://www.roadsmartlight.com](https://www.roadsmartlight.com)  
> **Global Portals**:
> - 🇪🇸 [Español (América Latina y España)](https://www.roadsmartlight.com/es/)
> - 🇫🇷 [Français (Afrique Francophone & Europe)](https://www.roadsmartlight.com/fr/)
> - 🇵🇹 [Português (Brasil e Países Lusófonos)](https://www.roadsmartlight.com/pt/)

---

## 1. Key Component Technical Benchmarks

| Component | Engineering Standard / Specification | Key Verification Metrics |
| :--- | :--- | :--- |
| **PV Module** | High-efficiency monocrystalline silicon ($\eta \ge 21.5\%$) | IEC 61215, IEC 61730, positive tolerance (0/+5W) |
| **Battery Storage** | Grade-A $\text{LiFePO}_4$ (Lithium Iron Phosphate) cells | UN38.3, MSDS, $\ge 2000$ cycles at 80% DoD, active BMS |
| **Luminaire Optics** | High-transmittance optical PC Batwing lens (Type II / Type III) | LM-79, LM-80, Color Rendering Index $CRI \ge 70$, 3000K-6000K |
| **Charge Controller** | Digital MPPT tracking ($\ge 98\%$ tracking efficiency) | Multi-peak tracking, multi-stage charging, temperature compensation |
| **Enclosure** | Die-cast ADC12 aluminum alloy with anti-corrosion coating | IP66 water/dust ingress, IK08/IK10 mechanical impact protection |

---

## 2. DIALux Photometric Simulation Guidelines

For highway and municipal engineering tenders, luminaires must provide accredited `.IES` / `.LDT` photometric files to verify road class compliance:

1. **Road Class M3 / M4 (Expressways and Primary Arterials)**:
   - Average Luminance ($L_{avg}$): $\ge 1.0\,\text{cd/m}^2$
   - Overall Uniformity ($U_0$): $\ge 0.40$
   - Longitudinal Uniformity ($U_l$): $\ge 0.60$
   - Threshold Increment ($TI$): $\le 15\%$

2. **Road Class M5 / P1 (Secondary Roads & Industrial Zones)**:
   - Average Illuminance ($E_{avg}$): $\ge 15.0\,\text{lux}$
   - Overall Uniformity ($U_0$): $\ge 0.35$

For project-specific DIALux files and custom project simulations, refer to the technical engineering portal at [https://www.roadsmartlight.com](https://www.roadsmartlight.com).
