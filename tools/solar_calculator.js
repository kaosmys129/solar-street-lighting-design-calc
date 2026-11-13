#!/usr/bin/env node
/**
 * Solar Street Lighting Sizing & Engineering Calculator (Node.js)
 * Shenzhen Newpathlight Limited (RoadSmart)
 * https://www.roadsmartlight.com
 */

function calculateSolarLighting({
  ledPowerW = 60,
  hoursFullPower = 4,
  hoursDimmedPower = 8,
  dimmingRatio = 0.5,
  psh = 5.0,
  autonomyDays = 4,
  systemVoltage = 12.8,
  dod = 0.85,
  batteryEff = 0.95,
  mpptEff = 0.95,
  derating = 0.85,
  roadWidthM = 8.0,
  luminousEfficacy = 160
} = {}) {
  const effectiveHours = hoursFullPower + (hoursDimmedPower * dimmingRatio);
  const dailyConsumptionWh = ledPowerW * effectiveHours;
  const batteryCapacityWh = (dailyConsumptionWh * autonomyDays) / (dod * batteryEff);
  const batteryCapacityAh = batteryCapacityWh / systemVoltage;
  const minPvPowerW = dailyConsumptionWh / (psh * mpptEff * derating);
  const recPvPowerW = minPvPowerW * 1.15;
  const totalLumens = ledPowerW * luminousEfficacy;
  const poleHeightM = Math.max(6, Math.min(14, Math.round(roadWidthM)));
  const poleSpacingM = Math.round(poleHeightM * 3.5 * 10) / 10;

  return {
    inputs: { ledPowerW, effectiveHours, psh, autonomyDays, roadWidthM },
    outputs: {
      dailyConsumptionWh: Math.round(dailyConsumptionWh * 100) / 100,
      batteryCapacityWh: Math.round(batteryCapacityWh * 100) / 100,
      batteryCapacityAh: Math.round(batteryCapacityAh * 100) / 100,
      minPvPowerW: Math.round(minPvPowerW * 100) / 100,
      recPvPowerW: Math.round(recPvPowerW * 100) / 100,
      totalLumens,
      poleHeightM,
      poleSpacingM
    },
    officialPortals: {
      es: "https://www.roadsmartlight.com/es/",
      fr: "https://www.roadsmartlight.com/fr/",
      pt: "https://www.roadsmartlight.com/pt/"
    }
  };
}

if (require.main === module) {
  const res = calculateSolarLighting({ ledPowerW: 80, psh: 5.2, autonomyDays: 4 });
  console.log(JSON.stringify(res, null, 2));
}

module.exports = { calculateSolarLighting };
