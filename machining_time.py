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
        machined_length = float(input("Enter actual axial length machined (mm): "))
        feed = float(input("Enter feed rate (mm/rev): "))
        rpm = float(input("Enter spindle speed (rpm): "))
        initial_diameter = float(input("Enter initial diameter (mm): "))
        final_diameter = float(input("Enter final diameter (mm): "))
        depth_of_cut = float(input("Enter radial depth of cut (mm): "))
        machine_rate = float(input("Enter machine hourly rate (Rs/hour): "))
        setup_time = float(input("Enter setup time (minutes): "))
        number_of_tool_changes = int(input("Enter number of tool changes: "))
        tool_change_time = float(input("Enter time per tool change (minutes): "))
        tool_life = float(input("Enter tool life per cutting edge (minutes): "))
        tool_edge_cost = float(input("Enter cost per cutting edge (Rs): "))
        batch_size = int(input("Enter number of components: "))
        material_cost = float(input("Enter material cost per component (Rs): "))

        # Step 2: Validate the inputs
        if (length <= 0 or feed <= 0 or rpm <= 0
            or initial_diameter <= 0 or final_diameter <= 0
            or depth_of_cut <= 0 or machine_rate <= 0
            or final_diameter >= initial_diameter or setup_time < 0 or number_of_tool_changes < 0 
            or tool_change_time < 0 or tool_life <= 0 or tool_edge_cost < 0 or machined_length <= 0 or batch_size <= 0 or material_cost < 0):

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
            
            # Calculate removed material volume
            removed_volume = (math.pi / 4) * (initial_diameter**2 - final_diameter**2) * machined_length

            # Calculate average Material Removal Rate
            mrr = removed_volume / machining_time

            # Convert mm^3/min into cm^3/min
            mrr_cm3 = mrr / 1000
            
            # Calculate initial cutting speed
            cutting_speed = (math.pi * initial_diameter * rpm) / 1000

            # Calculate total cutting-time machine cost
            machining_cost = (machining_time / 60) * machine_rate
            
            # Calculate setup cost
            setup_cost = (setup_time / 60) * machine_rate

            # Calculate total tool-change time
            total_tool_change_time = number_of_tool_changes * tool_change_time

            # Calculate tool-change cost
            tool_change_cost = (total_tool_change_time / 60) * machine_rate
            
            # Calculate cutting tool consumption cost 
            tool_cost = (machining_time / tool_life) * tool_edge_cost

            # Variable cost per component
            variable_cost = (machining_cost + tool_change_cost + tool_cost + material_cost)
            
            # Batch setup cost is charged only once
            batch_total_cost = variable_cost * batch_size + setup_cost

            # Calculate cost per component
            unit_cost = batch_total_cost / batch_size

            # Display machining results
            print("\n--- Machining Results ---")
            print(f"Number of Passes: {passes}")
            print(f"Time Per Pass: {time_per_pass:.2f} minutes")
            print(f"Total Machining Time: {machining_time:.2f} minutes")
            print(f"Total Machining Time: {machining_time * 60:.2f} seconds")
            print(f"Initial Cutting Speed: {cutting_speed:.2f} m/min")
            print(f"Removed Material Volume: {removed_volume:.2f} mm^3")
            print(f"Average MRR: {mrr:.2f} mm^3/min")
            print(f"Average MRR: {mrr_cm3:.2f} cm^3/min")

            # Display cost breakdown
            print(f"Machining Cost: Rs. {machining_cost:.2f}")
            print(f"Setup Cost: Rs. {setup_cost:.2f}")
            print(f"Total Tool Change Time: {total_tool_change_time:.2f} minutes")
            print(f"Tool Change Cost: Rs. {tool_change_cost:.2f}")
            print(f"Cutting Tool Consumption Cost: Rs. {tool_cost:.2f}")
            
            print("\n--- Production Cost Analysis ---")
            print(f"Batch Quantity: {batch_size}")
            print(f"Material Cost Per Component: Rs. {material_cost:.2f}")
            print(f"Variable Cost Per Component: Rs. {variable_cost:.2f}")
            print(f"Total Batch Cost: Rs. {batch_total_cost:.2f}")
            print(f"Estimated Cost Per Component: Rs. {unit_cost:.2f}")

    except ValueError:
        print("Error: Please enter valid numerical values.")

    # Step 5: Ask whether to calculate again
    again = input("\nCalculate again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you for using the calculator!")
        break