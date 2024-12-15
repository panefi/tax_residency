from datetime import datetime

def calculate_days_outside(departure_date, return_date):
    # Convert strings to datetime objects
    departure = datetime.strptime(departure_date, '%Y-%m-%d')
    return_ = datetime.strptime(return_date, '%Y-%m-%d')
    
    # Calculate the number of full days outside
    full_days_outside = (return_ - departure).days - 1
    return max(full_days_outside, 0) 