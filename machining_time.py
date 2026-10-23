# Machining Time Calculator
# Manufacturing Engineering Project
# Estimates cutting time for a single-pass turning operation
# Assumes constant spindle speed and feed rate
import math
print("=== Turning Machining Time Calculator ===")

while True:
    try:
        # Step 1: Take inputs from the user
        length = float(input("Enter tool travel length (mm): "))
        feed = float(input("Enter feed rate (mm/rev): "))
        rpm = float(input("Enter spindle speed (rpm): "))
        initial_diameter = float(input("Enter initial diameter (mm): "))
        final_diameter = float(input("Enter final diameter (mm): "))
        depth_of_cut = float(input("Enter radial depth of cut (mm): "))
        machine_rate = float(input("Enter machine hourly rate (Rs/hour): "))
        setup_time = float(input("Enter setup time (minutes): "))

        # Step 2: Validate the inputs
        if (length <= 0 or feed <= 0 or rpm <= 0
            or initial_diameter <= 0 or final_diameter <= 0
            or depth_of_cut <= 0 or machine_rate <= 0
            or final_diameter >= initial_diameter) or setup_time < 0:

            print("Error: Enter valid positive machining parameters.")
            print("The final diameter must be smaller than the initial diameter.")

        else:
            # Step 3: Calculate machining time
            
            # Calculate number of passes
            passes = math.ceil((initial_diameter - final_diameter) / (2 * depth_of_cut))
            
            # Calculate time per pass
            time_per_pass = length / (feed * rpm)

            # Calculate total machining time
            machining_time = time_per_pass * passes

            # Calculate initial cutting speed
            cutting_speed = (math.pi * initial_diameter * rpm) / 1000

            # Calculate total cutting-time machine cost
            machining_cost = (machining_time / 60) * machine_rate
            
            # Calculate setup cost
            setup_cost = (setup_time / 60) * machine_rate

            # Calculate total estimated machine cost
            total_cost = machining_cost + setup_cost
            
            print("\n--- Machining Results ---")
            print(f"Number of Passes: {passes}")
            print(f"Time Per Pass: {time_per_pass:.2f} minutes")
            print(f"Total Machining Time: {machining_time:.2f} minutes")
            print(f"Total Machining Time: {machining_time * 60:.2f} seconds")
            print(f"Initial Cutting Speed: {cutting_speed:.2f} m/min")
            print(f"Estimated Machining Cost: Rs. {machining_cost:.2f}")
            print(f"Setup Cost: Rs. {setup_cost:.2f}")
            print(f"Total Estimated Machine Cost: Rs. {total_cost:.2f}")

    except ValueError:
        print("Error: Please enter valid numerical values.")

    # Step 5: Ask whether to calculate again
    again = input("\nCalculate again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you for using the calculator!")
        break