# Guia de Engenharia e Dimensionamento de Iluminação Pública Solar

> **Autor institucional**: Shenzhen Newpathlight Limited (RoadSmart)  
> **Portal oficial**: [https://www.roadsmartlight.com/pt/](https://www.roadsmartlight.com/pt/)  
> **Recursos técnicos**: [Checklist de Aquisição e Especificação para Editais](https://www.roadsmartlight.com/pt/resources/procurement-checklist/)  
> **Ficha de referência**: [Poste de Iluminação Solar 80W-120W ST2](https://www.roadsmartlight.com/pt/projects/solar-street-light-80-120w/)

---

## 1. Metodologia de Dimensionamento Fotovoltaico Autônomo

A especificação de luminárias solares integradas (*All-in-One*) para projetos municipais e concessionárias no Brasil e países lusófonos (Angola, Moçambique, Portugal) deve obedecer aos requisitos da **ABNT NBR 5101** (Iluminação Pública) e critérios de eficiência energética do INMETRO.

### 1.1 Demanda Energética Noturna ($E_{diário}$)

$$E_{diário} = P_{LED} \times (t_{100\%} + t_{reduzido} \times k_{dim})$$

- $P_{LED}$: Potência elétrica do conjunto óptico LED (W).
- $t_{100\%}$: Horas de pico operacional (ex.: 18h às 22h, 100% de fluxo luminoso).
- $t_{reduzido}$: Horas em modo econômico inteligente (22h às 06h, 30% a 50% de potência).
- $k_{dim}$: Fator de dimerização automática.

---

### 1.2 Dimensionamento do Banco de Baterias LiFePO4 ($C_{bateria}$)

$$C_{bateria} (\text{Wh}) = \frac{E_{diário} \times N_{autonomia}}{\text{DoD} \times \eta_{bateria}}$$

*Parâmetros recomendados para o território brasileiro:*
- $N_{autonomia}$: 3 a 5 dias de autonomia sem insolação (períodos de chuva prolongada).
- $\text{DoD}$ (Profundidade de Descarga): $\le 85\%$ para assegurar vida útil superior a 2.000 ciclos completos.
- Tensão nominal de trabalho: Sistemas integrados em 12,8V / 25,6V com gerenciamento por BMS digital.

---

### 1.3 Potência Nominal do Painel Solar ($P_{FV}$)

$$P_{FV} (\text{Wp}) = \frac{E_{diário}}{\text{HSP}_{mínimo} \times \eta_{MPPT} \times f_{perdas}} \times 1{,}15$$

- $\text{HSP}_{mínimo}$: Horas de Sol Pleno (kWh/m²/dia) com base nos atlas solares (ex.: CRESESB / INPE).
- $f_{perdas}$: Fator de poeira e temperatura de operação em regiões de alto calor (Nordeste brasileiro).
- Grau de estanqueidade: Obrigatório IP66 para evitar corrosão em cidades costeiras e maresia.

---

## 2. Exemplo Prático de Aplicação: Iluminação Viária em Região Litorânea / Nordeste (Bahia, Brasil)

- **Largura da pista**: $8{,}0\,\text{m}$ (via coletora / distribuição).
- **HSP do mês crítico**: $4{,}8\,\text{h/dia}$.
- **Requisito de iluminação**: Classe V3 / V4 (iluminância média $\ge 15\,\text{lux}$, uniformidade geral $U_0 \ge 0{,}4$).
- **Equipamento indicado**: RoadSmart ST2-80 ou ST2-120.

### Ficha Técnica Resumida:
- **ST2-80**: Painel 80W / 18V Monocristalino, Bateria LiFePO4 384Wh, 10.000 lm, IP66.
- **ST2-120**: Painel 120W / 18V Monocristalino, Bateria LiFePO4 640Wh, 15.000 lm, IP66.
- **Altura de montagem**: 7 a 9 metros.
- **Espaçamento entre postes**: 25 a 35 metros com distribuição de luz em asa de morcego (*Batwing*).

Para solicitar simulação fotométrica em DIALux, arquivos IES e documentação de suporte para licitações e editais, acesse [https://www.roadsmartlight.com/pt/](https://www.roadsmartlight.com/pt/).
