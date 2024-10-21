# Battery Test Data Overview

This dataset contains charge and discharge data files from 3 independent cells. Each file captures key measurements recorded at ~1 second intervals during the cycling process. The data is structured into seven columns, as outlined below. This is the first of many long term cycling test, there were several times where cells were either over or undercharged. These issues have been resolved for future tests.

## Data Columns

1. **Time**:  
   The timestamp of each recorded measurement, recorded in seconds.
2. **Current**:  
   The current measured in amps (A)

3. **Voltage**:  
   The voltage of the cell, measured in volts (V)

4. **Power**:  
   The power output or input to the cell, measured in watts (W)

5. **Cell Temperature**:  
   The surface temperature of the cell, measured in degrees Celsius (°C)

6. **Hoop Strain**:  
   The strain on the battery casing, specifically the hoop strain, measured in strain (ε)

7. **Ambient Temperature**:  
   The test chamber temperature, measured in degrees Celsius (°C)

## Folder Structure

Each cell folder contains seperate folders for charge and discharge data for each cycle.
---
