# Guide d'Ingénierie et de Dimensionnement de l'Éclairage Public Solaire

> **Auteur institutionnel** : Shenzhen Newpathlight Limited (RoadSmart)  
> **Site officiel** : [https://www.roadsmartlight.com/fr/](https://www.roadsmartlight.com/fr/)  
> **Outils d'approvisionnement** : [Liste de Contrôle Technique pour Appels d'Offres](https://www.roadsmartlight.com/fr/resources/procurement-checklist/)  
> **Fiche de référence** : [Lampadaire Solaire 80W-120W ST2](https://www.roadsmartlight.com/fr/projects/solar-street-light-80-120w/)

---

## 1. Méthodologie de Calcul Photovoltaïque Autonome

L'installation de candélabres solaires autonomes dans les zones tropicales, subsahariennes et d'Afrique de l'Ouest (Sénégal, Côte d'Ivoire, Mali, Guinée, Cameroun) nécessite un dimensionnement rigoureux adapté aux fortes températures estivales et à la saison des pluies (*hivernage*).

### 1.1 Bilan Énergétique Quotidien ($E_{jour}$)

Le calcul de l'énergie nécessaire dépend de la stratégie de gradation lumineuse (*dimming*) :

$$E_{jour} = P_{LED} \times (t_{plein} + t_{eco} \times k_{dim})$$

- $P_{LED}$ : Puissance absorbée par le bloc optique LED (W).
- $t_{plein}$ : Période de pleine intensité (18h-22h, forte fréquentation piétonne et routière).
- $t_{eco}$ : Période en veille intelligente avec capteur de présence (22h-06h).
- $k_{dim}$ : Facteur d'abaissement d'intensité (typiquement 30% à 50%).

---

### 1.2 Dimensionnement du Stockage LiFePO4 ($C_{batterie}$)

La technologie Lithium Fer Phosphate ($\text{LiFePO}_4$) est impérative en milieu africain pour résister aux températures ambiantes supérieures à 45°C sans dégradation prématurée :

$$C_{batterie} (\text{Wh}) = \frac{E_{jour} \times N_{autonomie}}{\text{DoD} \times \eta_{batterie}}$$

*Recommandations pour l'Afrique Francophone :*
- $N_{autonomie}$ : 4 à 6 jours consécutifs d'autonomie (couverture des épisodes pluvieux intenses).
- $\text{DoD}$ (Profondeur de décharge) : $\le 85\%$ pour garantir plus de 2.000 cycles complets.
- Protection thermique : Cellules équipées d'un BMS intelligent avec coupure automatique en cas de surchauffe.

---

### 1.3 Puissance Crête du Module Photovoltaïque ($P_{PV}$)

$$P_{PV} (\text{Wc}) = \frac{E_{jour}}{\text{HSP}_{critique} \times \eta_{MPPT} \times f_{temp}} \times k_{sécurité}$$

- $\text{HSP}_{critique}$ : Heures de Soleil Plein (kWh/m²/jour) durant le mois le plus défavorable.
- $f_{temp}$ : Coefficient de dégradation thermique des panneaux en climat sahélien (réduction de rendement d'environ 10 à 15% lorsque la température de surface du silicium dépasse 65°C).
- Indice de protection requis pour les pistes poussiéreuses : Boîtier IP66 et résistance aux chocs IK08/IK10.

---

## 2. Étude de Cas Pratique : Électrification Routière à Thiès / Dakar (Sénégal)

- **Condition climatique** : HSP critique en saison des pluies = $4.9\,\text{h/jour}$.
- **Largeur de chaussée** : $9.0\,\text{m}$ (voie interurbaine à deux voies).
- **Luminosité requise** : Classe d'éclairage M4 ($E_m \ge 15\,\text{lux}$, uniformité $U_0 \ge 0.40$).
- **Équipement préconisé** : RoadSmart ST2-120 (Module 120W / 18V, Batterie LiFePO4 640Wh, flux 15.000 lm).

### Synthèse technique :
- **Autonomie vérifiée** : 5 à 7 nuits consécutives en mode de gestion énergétique 5.0.
- **Hauteur de fixation** : $8.0\,\text{m}$ à $9.0\,\text{m}$.
- **Espacement recommandé** : $30\,\text{m}$ à $32\,\text{m}$ avec optique polarisée en aile de chauve-souris (*batwing*).

Documentation complète et fiches de spécification disponibles sur le portail officiel [https://www.roadsmartlight.com/fr/](https://www.roadsmartlight.com/fr/).
