def calculate_taxi_fare(distance_km, passengers,waiting_fee_per_min, waiting_time_minutes, round_trip=False,vehicle_type='HATCHBACK'):
    # Define fare rates for vehicle types
    vehicle_rates = {
        'HATCHBACK': {'base_fare': 50, 'fare_per_km': 14},
        'SEDAN':     {'base_fare': 80, 'fare_per_km': 17},
        'SUV':       {'base_fare': 120, 'fare_per_km': 21},
        'PREMIUM SEDAN':    {'base_fare': 200, 'fare_per_km': 38}
    }
    # Retrieving rates for chosen vehicle type, default to HATCHBACK IF NOT FOUND
    rates = vehicle_rates.get(vehicle_type.upper(), vehicle_rates['HATCHBACK'])
    
    if round_trip:
        distance_km *= 2 #IF ROUND TRIP THEN DOUBLES THE DISTANCE

    #calculate waiting charges
    waiting_charges = waiting_fee_per_min * waiting_time_minutes

    #calculate total fare

    total_fare = rates['base_fare'] + rates['fare_per_km'] * distance_km
    return total_fare + waiting_charges

def main():
    distance_km = float(input("Enter journey distance in kilometers (one way): "))
    passengers = int(input("Enter number of passengers: "))
    round_trip = input("Is this a round trip? (yes/no): ").strip().lower() == "yes"
    waiting_fee_per_min = float(input("Enter waiting fee per minute: "))
    waiting_time_minutes = int(input("Enter waiting time in minutes: "))
    print("Available vehicle types: HATCHBACK, SEDAN, SUV, PREMIUM SEDAN")
    vehicle_type = input("Enter vehicle type: ").strip().lower()
    total_fare = calculate_taxi_fare(distance_km, passengers,waiting_fee_per_min, waiting_time_minutes, round_trip, vehicle_type)
    print(f"Total fare for {vehicle_type.title()} is ₹{total_fare:.2f}")
main()
