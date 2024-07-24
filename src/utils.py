import pandas as pd
import re

# Function to convert the movies budgets to USD
def process_budget(budget):
    
    # Clean up budget data
    if pd.isna(budget):
        return 0, 0
    
    # Extract budget value and convert to integer
    budget_value = re.search(r'(\d+(?:\.\d+)?)', budget.replace(',', ''))
    if budget_value:
        budget_value = float(budget_value.group(0)) * (1e6 if 'million' in budget else 1)
        if 'US$' in budget or 'USD' in budget:
            return budget_value, budget_value
        else:
            # Convert to USD using an assumed conversion rate
            conversion_rate = 1.1  # Hypothetical conversion rate
            return budget_value, budget_value * conversion_rate
    return 0, 0

# Function to transform the tim
def parse_running_time(running_time):
    if not running_time:
        return None
    # Extract the running time in minutes
    match = re.search(r'(\d+) minutes', running_time)
    return int(match.group(1)) if match else None