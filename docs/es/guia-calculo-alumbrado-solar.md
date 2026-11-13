# Guía de Dimensionamiento y Cálculo de Alumbrado Público Solar

> **Autor institucional**: Shenzhen Newpathlight Limited (RoadSmart)  
> **Sitio oficial**: [https://www.roadsmartlight.com/es/](https://www.roadsmartlight.com/es/)  
> **Recursos de ingeniería**: [Checklist de Licitación y Verificación Técnica](https://www.roadsmartlight.com/es/resources/procurement-checklist/)  
> **Referencia de proyectos**: [Farola Solar 80W-120W ST2](https://www.roadsmartlight.com/es/projects/solar-street-light-80-120w/)

---

## 1. Fundamentos Matemáticos del Dimensionamiento Fotovoltaico

El cálculo de una luminaria solar autónoma (All-in-One o Split) se rige por la física del balance energético diario. Para garantizar operatividad ininterrumpida sin recurrir a la red eléctrica, el sistema debe captar y almacenar más energía de la consumida durante el ciclo nocturno más exigente.

### 1.1 Consumo Energético Diario ($E_{diario}$)

El consumo nocturno real depende del perfil de atenuación (*dimming profile*) controlado por el microcontrolador MPPT:

$$E_{diario} = P_{LED} \times (t_{100\%} + t_{atenuado} \times k_{dim})$$

*Donde:*
- $P_{LED}$: Potencia eléctrica consumida por el módulo LED (W).
- $t_{100\%}$: Horas de funcionamiento a máxima potencia (usualmente 3 a 4 horas en horas pico de tráfico).
- $t_{atenuado}$: Horas en modo ahorro de energía (4 a 8 horas con sensor de movimiento PIR/microondas o reducción programada).
- $k_{dim}$: Coeficiente de atenuación lumínica (típicamente 0.3 a 0.5).

---

### 1.2 Capacidad de la Batería LiFePO4 ($C_{batería}$)

Las baterías de Litio Ferro-Fosfato ($\text{LiFePO}_4$) son el estándar de la industria por su estabilidad térmica (-20°C a +60°C) y vida útil superior a 2.000 ciclos al 80% de profundidad de descarga (DoD).

$$C_{batería} (\text{Wh}) = \frac{E_{diario} \times N_{autonomía}}{\text{DoD} \times \eta_{batería}}$$

*Parámetros de diseño recomendados para México y LATAM:*
- $N_{autonomía}$: Días de autonomía sin radiación solar (3 a 5 días para cumplir normativas viales).
- $\text{DoD}$: Profundidad de descarga segura ($\le 85\%$).
- $\eta_{batería}$: Eficiencia culómbica ($\approx 95\%$).

---

### 1.3 Potencia Pico del Panel Solar ($P_{FV}$)

La potencia pico requerida del módulo monocristalino se calcula a partir de las Horas de Sol Pico (HSP / PSH) del mes con menor radiación histórica en la ubicación del proyecto (datos NASA SSE o SMN):

$$P_{FV} (\text{Wp}) = \frac{E_{diario}}{\text{HSP}_{mín} \times \eta_{MPPT} \times f_{derating}} \times k_{seguridad}$$

*Factores de pérdida:*
- $\eta_{MPPT}$: Rendimiento del regulador MPPT ($\ge 95\%$).
- $f_{derating}$: Pérdidas combinadas por suciedad, temperatura superficial del panel y desajuste angular ($\approx 0.85$).
- $k_{seguridad}$: Margen para recarga acelerada tras días lluviosos ($\approx 1.15$).

---

## 2. Marco Normativo en Países de Habla Hispana

| País | Norma / Estándar | Requisitos Clave para Proyectos Públicos |
| :--- | :--- | :--- |
| **México** | **NOM-013-ENER-2013** / **NOM-031-ENER-2012** | Eficiencia energética en vialidades, luminancia mínima (cd/m²), uniformidad general ($U_0 \ge 0.4$). |
| **Colombia** | **RETILAP** | Reglamento Técnico de Iluminación y Alumbrado Público, certificación obligatoria de fotometría IES y grado IP/IK. |
| **Chile** | **DS 43/2012 MMA** (Contaminación Lumínica) | Control estricto de emisión hemisférica superior ($FHS \le 1\%$), temperatura de color cálida ($\le 3000\text{K}$) en zonas astronómicas. |
| **España** | **RD 1890/2008** | Eficiencia energética en instalaciones de alumbrado exterior. |

---

## 3. Ejemplo Práctico de Cálculo: Proyecto Carretero en Sonora, México

- **Ubicación**: Carretera interurbana secundaria (ancho de calzada $W = 8\,\text{m}$, 2 carriles).
- **HSP mes crítico (Diciembre)**: $4.8\,\text{h/día}$.
- **Requisito lumínico**: Clase M4 ($E_{media} \ge 15\,\text{lux}$, uniformidad $U_0 \ge 0.4$).
- **Selección de luminaria**: RoadSmart ST2-80 (Panel 80W / Batería LiFePO4 384Wh / 10.000 lm).

### Resultados del dimensionamiento:
1. **Consumo por noche**: Con perfil 4h al 100% (40W nominal LED) + 8h al 40% (16W) $\rightarrow E_{diario} = (40 \times 4) + (16 \times 8) = 288\,\text{Wh/día}$.
2. **Autonomía**: $\frac{384\,\text{Wh} \times 0.85 \times 0.95}{288\,\text{Wh}} \approx 1.07$ noches a ciclo completo; en modo sensor inteligente garantiza hasta **5 a 7 días** en condiciones de lluvia continua.
3. **Altura de poste recomendada**: $7.0\,\text{m}$ a $8.0\,\text{m}$.
4. **Interdistancia entre postes**: $28\,\text{m}$ con óptica tipo Batwing polarizada.

Para consultar especificaciones completas y validar compatibilidad de proyectos de licitación, visite el portal oficial [https://www.roadsmartlight.com/es/](https://www.roadsmartlight.com/es/).
