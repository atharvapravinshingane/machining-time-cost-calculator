# ============================================================
# MACHINING TIME AND COST CALCULATOR
# Manufacturing Engineering Project
#
# This program:
# 1. Asks for turning-operation inputs.
# 2. Checks whether the inputs are valid.
# 3. Calculates machining time, cutting speed, and MRR.
# 4. Calculates component and batch costs.
# 5. Generates graphs for different feed values.
#
# Main assumptions:
# - Spindle speed and feed remain constant during each calculation.
# - Every pass uses the same tool travel length.
# - Setup occurs once per batch.
# - Tool-change count is entered PER COMPONENT.
# - Tool consumption is charged in proportion to cutting time.
# ============================================================


# ------------------------------------------------------------
# IMPORTS: bring useful tools into this program.
# ------------------------------------------------------------

# "math" provides mathematical tools:
# math.pi = the value of pi
# math.ceil() = round upward to a whole number
# math.isfinite() = check that a number is not infinity or NaN
import math

# Import our graphing function from plot_analysis.py.
# Both Python files must be in the same folder.
from plot_analysis import plot_feed_analysis


# ------------------------------------------------------------
# FUNCTION: calculate time for one pass and for all passes.
#
# "def" defines a function.
# The names inside parentheses are the inputs it receives.
# The indented lines are the instructions inside the function.
#
# Defining this function does not run its calculations.
# They run later when we call calculate_machining_time(...).
# ------------------------------------------------------------

def calculate_machining_time(length, feed, rpm, passes):
    # feed (mm/rev) × rpm (rev/min) = tool speed (mm/min).
    # Distance divided by speed gives time in minutes.
    time_per_pass = length / (feed * rpm)

    # Multiply the time for one pass by the number of passes.
    total_time = time_per_pass * passes

    # Send both answers back, in this order:
    # first time_per_pass, then total_time.
    return time_per_pass, total_time

# Calculate cutting speed at the initial workpiece diameter.
def calculate_cutting_speed(diameter, rpm):
    cutting_speed = (math.pi * diameter * rpm) / 1000
    return cutting_speed

# ------------------------------------------------------------
# START THE CALCULATOR
# ------------------------------------------------------------

print("=== Turning Machining Time and Cost Calculator ===")


# "while True" repeats the calculator until we use "break".
while True:

    # "try" lets us handle invalid numerical input without
    # immediately stopping the entire program.
    try:

        # ----------------------------------------------------
        # STEP 1: GET INPUTS
        #
        # input() displays a question and reads typed text.
        # float() converts that text into a decimal number.
        # int() converts it into a whole number.
        #
        # Enter numbers only; do not type units or currency.
        # ----------------------------------------------------

        # Total distance travelled by the tool during one pass.
        # This can include approach and overtravel.
        length = float(
            input("Enter tool travel length per pass (mm): ")
        )

        # Actual axial length from which material is removed.
        # Used to calculate removed volume.
        machined_length = float(
            input("Enter actual axial length machined (mm): ")
        )

        # Distance the tool advances per workpiece revolution.
        feed = float(
            input("Enter feed rate (mm/rev): ")
        )

        # Number of workpiece revolutions per minute.
        rpm = float(
            input("Enter spindle speed (rpm): ")
        )

        initial_diameter = float(
            input("Enter initial diameter (mm): ")
        )

        final_diameter = float(
            input("Enter final diameter (mm): ")
        )

        # Radial depth is half the diameter reduction per pass.
        depth_of_cut = float(
            input("Enter radial depth of cut (mm): ")
        )

        machine_rate = float(
            input("Enter machine hourly rate (Rs/hour): ")
        )

        # Setup time is charged once for the entire batch.
        setup_time = float(
            input("Enter setup time per batch (minutes): ")
        )

        # This simplified model uses a manually entered
        # tool-change count for EACH component.
        number_of_tool_changes = int(
            input("Enter number of tool changes per component: ")
        )

        tool_change_time = float(
            input("Enter time per tool change (minutes): ")
        )

        tool_life = float(
            input("Enter tool life per cutting edge (minutes): ")
        )

        tool_edge_cost = float(
            input("Enter cost per cutting edge (Rs): ")
        )

        batch_size = int(
            input("Enter number of components: ")
        )

        material_cost = float(
            input("Enter material cost per component (Rs): ")
        )

        # ----------------------------------------------------
        # STEP 2: VALIDATE INPUTS
        #
        # "if" checks a condition.
        # "or" means any one of the conditions can trigger it.
        # "raise ValueError" sends an error message to the
        # "except ValueError" section near the bottom.
        # ----------------------------------------------------

        # A list groups several values together.
        decimal_inputs = [
            length,
            machined_length,
            feed,
            rpm,
            initial_diameter,
            final_diameter,
            depth_of_cut,
            machine_rate,
            setup_time,
            tool_change_time,
            tool_life,
            tool_edge_cost,
            material_cost,
        ]

        # Check each decimal input individually.
        for value in decimal_inputs:
            if not math.isfinite(value):
                raise ValueError(
                    "Inputs must be finite numbers, not infinity or NaN."
                )

        # These quantities must be greater than zero.
        if (
            length <= 0
            or machined_length <= 0
            or feed <= 0
            or rpm <= 0
            or initial_diameter <= 0
            or final_diameter <= 0
            or depth_of_cut <= 0
            or tool_life <= 0
        ):
            raise ValueError(
                "Lengths, diameters, feed, rpm, depth of cut, "
                "and tool life must be greater than zero."
            )

        # External turning must reduce the diameter.
        if final_diameter >= initial_diameter:
            raise ValueError(
                "Final diameter must be smaller than initial diameter."
            )

        # For this model, tool travel must cover the machined length.
        if machined_length > length:
            raise ValueError(
                "Actual machined length cannot exceed tool travel length."
            )

        # These quantities can be zero, but cannot be negative.
        if (
            machine_rate < 0
            or setup_time < 0
            or number_of_tool_changes < 0
            or tool_change_time < 0
            or tool_edge_cost < 0
            or material_cost < 0
        ):
            raise ValueError(
                "Costs, setup time, tool-change time, and "
                "tool-change count cannot be negative."
            )

        if batch_size <= 0:
            raise ValueError(
                "The number of components must be greater than zero."
            )

        # ----------------------------------------------------
        # STEP 3: CALCULATE MACHINING RESULTS
        # ----------------------------------------------------

        # Each pass reduces the DIAMETER by twice the radial
        # depth of cut.
        #
        # math.ceil() rounds upward because a partial final
        # depth still requires another machining pass.
        passes = math.ceil(
            (initial_diameter - final_diameter)
            / (2 * depth_of_cut)
        )

        # CALL the function defined at the top.
        #
        # Give it the four values it needs.
        # Store its two returned answers in the same order.
        #
        # This replaces the original time formulas here;
        # the formulas now live inside the function.
        time_per_pass, machining_time = calculate_machining_time(
            length, feed, rpm, passes
        )

        # Removed volume = initial cylinder volume minus
        # final cylinder volume over the actual machined length.
        #
        # **2 means "squared".
        removed_volume = (
            (math.pi / 4)
            * (initial_diameter**2 - final_diameter**2)
            * machined_length
        )

        # Average material removal rate:
        # volume removed divided by total cutting time.
        mrr = removed_volume / machining_time

        # 1 cm³ = 1000 mm³.
        mrr_cm3 = mrr / 1000

        # Cutting speed at the INITIAL diameter.
        # Divide by 1000 to convert mm/min to m/min.
        cutting_speed = calculate_cutting_speed(
            initial_diameter, rpm )
            
        # ----------------------------------------------------
        # STEP 4: CALCULATE COSTS
        # ----------------------------------------------------

        # Convert cutting time from minutes to hours,
        # then multiply by the hourly machine rate.
        machining_cost = (
            machining_time / 60
        ) * machine_rate

        # Setup cost is charged once per batch.
        setup_cost = (
            setup_time / 60
        ) * machine_rate

        # Tool-change time and cost PER COMPONENT.
        total_tool_change_time = (
            number_of_tool_changes * tool_change_time
        )

        tool_change_cost = (
            total_tool_change_time / 60
        ) * machine_rate

        # Fraction of one cutting edge's life used × edge cost.
        # This estimates consumption cost; it does not predict
        # the actual number of tool changes.
        tool_cost = (
            machining_time / tool_life
        ) * tool_edge_cost

        # Costs charged for each component.
        variable_cost = (
            machining_cost
            + tool_change_cost
            + tool_cost
            + material_cost
        )

        # Multiply per-component costs by batch quantity,
        # then add the one-time batch setup cost.
        batch_total_cost = (
            variable_cost * batch_size
        ) + setup_cost

        # Spread the total batch cost across all components.
        unit_cost = batch_total_cost / batch_size

        # ----------------------------------------------------
        # STEP 5: DISPLAY RESULTS
        #
        # print() displays text in the terminal.
        # \n starts a new line.
        # f before the quotation mark lets us insert values
        # inside {braces}.
        # :.2f displays a number with two decimal places.
        # ----------------------------------------------------

        print("\n--- Machining Results Per Component ---")
        print(f"Number of Passes: {passes}")
        print(f"Time Per Pass: {time_per_pass:.2f} minutes")
        print(f"Total Machining Time: {machining_time:.2f} minutes")
        print(
            f"Total Machining Time: "
            f"{machining_time * 60:.2f} seconds"
        )
        print(f"Initial Cutting Speed: {cutting_speed:.2f} m/min")
        print(f"Removed Material Volume: {removed_volume:.2f} mm^3")
        print(f"Average MRR: {mrr:.2f} mm^3/min")
        print(f"Average MRR: {mrr_cm3:.2f} cm^3/min")

        print("\n--- Cost Breakdown ---")
        print(f"Machining Cost Per Component: Rs. {machining_cost:.2f}")
        print(f"Setup Cost Per Batch: Rs. {setup_cost:.2f}")
        print(
            f"Tool Change Time Per Component: "
            f"{total_tool_change_time:.2f} minutes"
        )
        print(
            f"Tool Change Cost Per Component: "
            f"Rs. {tool_change_cost:.2f}"
        )
        print(
            f"Tool Consumption Cost Per Component: "
            f"Rs. {tool_cost:.2f}"
        )

        print("\n--- Production Cost Analysis ---")
        print(f"Batch Quantity: {batch_size}")
        print(f"Material Cost Per Component: Rs. {material_cost:.2f}")
        print(f"Variable Cost Per Component: Rs. {variable_cost:.2f}")
        print(f"Total Batch Cost: Rs. {batch_total_cost:.2f}")
        print(f"Estimated Cost Per Component: Rs. {unit_cost:.2f}")

        # ----------------------------------------------------
        # STEP 6: COMPARE FEEDS AND GENERATE GRAPHS
        #
        # Reuse the machining inputs already entered.
        # Only ask for the different feeds to compare.
        #
        # These graphs show cutting time and cutting-time
        # machine cost, NOT the full component cost.
        # ----------------------------------------------------

        print("\n--- Feed Comparison and Graphs ---")
        print("Enter at least two different positive feed values.")
        print("Example: 0.10,0.15,0.20,0.25,0.30")

        # This inner loop repeats only the feed-entry step
        # if the comparison feeds are invalid.
        while True:
            try:
                feed_text = input(
                    "Enter comparison feeds separated by commas (mm/rev): "
                )

                # Start with an empty list.
                comparison_feeds = []

                # split(",") separates the text at each comma.
                # strip() removes spaces around each value.
                # float() converts the text into a decimal.
                # append() adds that decimal to the list.
                for value in feed_text.split(","):
                    comparison_feed = float(value.strip())
                    comparison_feeds.append(comparison_feed)

                # Call the graphing function from plot_analysis.py.
                # It validates the feeds, prints comparisons,
                # saves both graphs, and displays graph windows.
                plot_feed_analysis(
                    length,
                    rpm,
                    initial_diameter,
                    final_diameter,
                    depth_of_cut,
                    machine_rate,
                    comparison_feeds,
                )

                # Leave this inner loop after graphing finishes.
                break

            except ValueError as error:
                print(f"Invalid comparison feeds: {error}")
                print("Please enter the comparison feeds again.")

    # Handle invalid main inputs or failed numerical validation.
    except ValueError as error:
        print(f"\nInput error: {error}")
        print("Please enter valid numbers without units or currency symbols.")

    # --------------------------------------------------------
    # STEP 7: REPEAT OR FINISH
    #
    # strip() removes surrounding spaces.
    # lower() changes text to lowercase.
    # Therefore "YES", "Yes", and "yes" are treated alike.
    # --------------------------------------------------------

    again = input(
        "\nCalculate again? (yes/no): "
    ).strip().lower()

    # != means "is not equal to".
    # Anything other than "yes" ends the calculator.
    if again != "yes":
        print("Thank you for using the calculator!")
        break