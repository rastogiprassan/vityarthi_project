PROJECT TITLE : Develop a Cab Fare estiator bases on distance.

OVERVIEW OF THE PROJECT : This Python taxi fare estimator project is designed to compute the total taxi fare for a trip by incorporating key variables such as trip distance, passenger count, vehicle type, round trip indicator, and waiting time. It uses predefined base fares and per kilometer rates for multiple vehicle categories (HATCHBACK, SEDAN, SUV, PREMIUM SEDAN), allowing the fare calculation to reflect different pricing tiers.

THE PROJECT FEATURES :

1. Input handlng for journey distance, number of passengers, round trip option, vehicle type selection, waiting time in minutes, and waiting charge per minute.
2. Round trip logic that doubles the distance for fare calculation.
3.  Dynamic rate look-up for different vehicle types using a dictionary.
4. Calculation of waiting charges by multiplying waiting minutes with a per-minute waiting rate.
5. A final computed fare that sums base fare, distance-based fare, and waiting fees.

This approach provides a customizable, extendable, and user-friendly fare estimation tool that can simulate realistic taxi fare computations based on common billing practices. It supports varying fare structures by vehicle and includes additional charges like waiting time, making it applicable for practical taxi service scenarios. The codebase is modular and easy to maintain or enhance with further features like surge pricing or fare caps.

THE  KEY TOOLS USED IN THIS TAXI FARE CALCULATOR PROJECT :

Python: The primary programming language used to implement the fare calculation logic and user interaction.
Python standard libraries: For input/output, string manipulation, and basic math operations.
Console interface: The project leverages a simple command-line interface for user interaction without GUI dependencies.

STEPS TO  INSTALL AND  RUN THE PROJECT ARE :

To install and run the Python taxi fare calculator project, follow these steps:

STEP 1:
Install Python
Ensure Python 3.x is installed on your system.
Verify installation by running python --version or python3 --version in your command prompt or terminal.

STEP 2: 
Prepare the Project Script
Create a new Python file, e.g., taxi_fare_calculator.py.

Copy the taxi fare calculator code into this file.

STEP 3: 
Run the Program
Open a terminal or comand prompt.
Navigate to the directory containing taxi_fare_calculator.py.
Run the script with python taxi_fare_calculator.py or python3 taxi_fare_calculator.py.

STEP 4:
Interact with the Program
Input the requested values such as distance, passengers, trip type, vehicle type, waiting time, and waiting charge per minute as prompted.
The program will calculate and display the total fare.
No additional libraries or dependencies are required for this basic console application. This makes setup straightforward and quick.
For advanced use (GUI, web integration), additional tools like Tkinter or Flask would need installation via pip.
This simple process lets you test and use the taxi fare estimator locally on your machine.

INSTRUCTIONS FOR TESTING :

1. Run the Python script in your console.
2. Input valid numeric values when prompted for distance, number of passengers, waiting time, and waiting charge per minute.
3. Choose a valid vehicle type from the provided list.
4. Check the output fare displayed matches expected calculations:
   Total fare = base fare + (per km rate × distance) + (waiting time × waiting charge per minute)
   Distance doubles if round trip is selected.
5. Test boundary cases: zero waiting time, one passenger, round trip yes/no, invalid vehicle input (should default).
6. Repeat with multiple data sets to verify consistnt behavior.
7. Optionally, add assertions or unit tests on the calculation function for automated testing.
