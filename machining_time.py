import math
from plot_analysis import plot_feed_analysis


def calculate_machining_time(length, feed, rpm, passes):
    time_per_pass = length / (feed * rpm)
    total_time = time_per_pass * passes
    return time_per_pass, total_time


def calculate_cutting_speed(diameter, rpm):
    cutting_speed = (math.pi * diameter * rpm) / 1000
    return cutting_speed


def calculate_machine_cost(time_minutes, hourly_rate):
    cost = (time_minutes / 60) * hourly_rate
    return cost


print("=== Turning Machining Time and Cost Calculator ===")

while True:
    try:
        length = float(
            input("Enter tool travel length per pass (mm): ")
        )
        machined_length = float(
            input("Enter actual axial length machined (mm): ")
        )
        feed = float(
            input("Enter feed rate (mm/rev): ")
        )
        rpm = float(
            input("Enter spindle speed (rpm): ")
        )
        initial_diameter = float(
            input("Enter initial diameter (mm): ")
        )
        final_diameter = float(
            input("Enter final diameter (mm): ")
        )
        depth_of_cut = float(
            input("Enter radial depth of cut (mm): ")
        )
        machine_rate = float(
            input("Enter machine hourly rate (Rs/hour): ")
        )
        setup_time = float(
            input("Enter setup time per batch (minutes): ")
        )
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

        for value in decimal_inputs:
            if not math.isfinite(value):
                raise ValueError(
                    "Inputs must be finite numbers, not infinity or NaN."
                )

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

        if final_diameter >= initial_diameter:
            raise ValueError(
                "Final diameter must be smaller than initial diameter."
            )

        if machined_length > length:
            raise ValueError(
                "Actual machined length cannot exceed tool travel length."
            )

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

        passes = math.ceil(
            (initial_diameter - final_diameter)
            / (2 * depth_of_cut)
        )

        time_per_pass, machining_time = calculate_machining_time(
            length, feed, rpm, passes
        )

        removed_volume = (
            (math.pi / 4)
            * (initial_diameter**2 - final_diameter**2)
            * machined_length
        )

        mrr = removed_volume / machining_time
        mrr_cm3 = mrr / 1000

        cutting_speed = calculate_cutting_speed(
            initial_diameter, rpm
        )

        machining_cost = calculate_machine_cost(
            machining_time, machine_rate
        )

        setup_cost = calculate_machine_cost(
            setup_time, machine_rate
        )

        total_tool_change_time = (
            number_of_tool_changes * tool_change_time
        )

        tool_change_cost = calculate_machine_cost(
            total_tool_change_time, machine_rate
        )

        tool_cost = (
            machining_time / tool_life
        ) * tool_edge_cost

        variable_cost = (
            machining_cost
            + tool_change_cost
            + tool_cost
            + material_cost
        )

        batch_total_cost = (
            variable_cost * batch_size
        ) + setup_cost

        unit_cost = batch_total_cost / batch_size

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
        print(
            f"Machining Cost Per Component: "
            f"Rs. {machining_cost:.2f}"
        )
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

        print("\n--- Feed Comparison and Graphs ---")
        print("Enter at least two different positive feed values.")
        print("Example: 0.10,0.15,0.20,0.25,0.30")

        while True:
            try:
                feed_text = input(
                    "Enter comparison feeds separated by commas (mm/rev): "
                )

                comparison_feeds = []

                for value in feed_text.split(","):
                    comparison_feed = float(value.strip())
                    comparison_feeds.append(comparison_feed)

                plot_feed_analysis(
                    length,
                    rpm,
                    initial_diameter,
                    final_diameter,
                    depth_of_cut,
                    machine_rate,
                    comparison_feeds,
                )

                break

            except ValueError as error:
                print(f"Invalid comparison feeds: {error}")
                print("Please enter the comparison feeds again.")

    except ValueError as error:
        print(f"\nInput error: {error}")
        print("Please enter valid numbers without units or currency symbols.")

    again = input(
        "\nCalculate again? (yes/no): "
    ).strip().lower()

    if again != "yes":
        print("Thank you for using the calculator!")
        break