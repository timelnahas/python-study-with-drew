import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Declare variables
# Constants
PercentageOfPopulationUsingElectricity = .48
PowerConsumptionPerCapita = 350
EndYear = 2050

# Mutable
# Step 1a: In Kilowats/Hr
CurrentPowerAvailability = 15128000000
CurrentYear = 2027
CurrentPopulation = 120000000 * (PercentageOfPopulationUsingElectricity)
CurrentPowerConsumption = CurrentPopulation * PowerConsumptionPerCapita

PopulationDelta = 1.025
PowerDelta = (1 - .01)

def CalculatePowerConsumption(population, consumptionRate):
    return population * consumptionRate

def CalculateNewPopulation(population, populationDelta):
    return population * populationDelta

def CalculateNewPowerAvailability(availability, powerDelta):
    return availability * powerDelta


# Step 2: Create an empty DataFrame with columns
df = pd.DataFrame(columns=['Year', 'Population', 'Power Availability', 'Power Consumption'])
df = df.append({
    'Year': CurrentYear, 
    'Population': CurrentPopulation, 
    'Power Availability': CurrentPowerAvailability, 
    'Power Consumption': CurrentPowerConsumption
}, ignore_index=True)

CurrentYear += 1

while CurrentPowerConsumption <= CurrentPowerAvailability:

    CurrentPopulation = CalculateNewPopulation(CurrentPopulation, PopulationDelta)
    CurrentPowerConsumption = CalculatePowerConsumption(CurrentPopulation, PowerConsumptionPerCapita)
    CurrentPowerAvailability = CalculateNewPowerAvailability(CurrentPowerAvailability, PowerDelta)

    df = df.append({
        'Year': CurrentYear, 
        'Population': CurrentPopulation, 
        'Power Availability': CurrentPowerAvailability, 
        'Power Consumption': CurrentPowerConsumption
    }, ignore_index=True)
    CurrentYear += 1

# # Save the filled DataFrame
# file_path = './output.csv'
# df.to_csv(file_path, index=False, float_format='%.2f')

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Power Availability'], marker='o', label='Power Availability', linestyle='-', color='b')
plt.plot(df['Year'], df['Power Consumption'], marker='o', label='Power Consumption', linestyle='-', color='r')

# Add labels and a legend
plt.xlabel('Year')
plt.ylabel('Power (in units)')
plt.title('Power Consumption vs. Power Availability Over the Years')
plt.legend()

# Display the chart
plt.grid(True)
plt.show()