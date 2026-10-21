
# Machining Time Calculator
# Manufacturing Engineering Project

print("=== Turning Machining Time Calculator ===")

while True:

    try:
        # Step 1: Take inputs from the user
        length = float(input("Enter tool travel length (mm): "))
        feed = float(input("Enter feed rate (mm/rev): "))
        rpm = float(input("Enter spindle speed (rpm): "))

        # Step 2: Validate the inputs
        if length <= 0 or feed <= 0 or rpm <= 0:
            print("Error: All values must be greater than zero.")

        else:
            # Step 3: Calculate machining time
            machining_time = length / (feed * rpm)

            # Step 4: Display the result
            print("\n--- Machining Results ---")
            print(f"Machining Time: {machining_time:.2f} minutes")
            print(f"Machining Time: {machining_time * 60:.2f} seconds")

    except ValueError:
        print("Error: Please enter valid numerical values.")

    # Step 5: Ask whether to calculate again
    again = input("\nCalculate again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you for using the calculator!")
        break
