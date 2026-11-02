# Lesson 12: reusable graphing function
import math
from pathlib import Path
import matplotlib.pyplot as plt


def plot_feed_analysis(length, rpm, initial_diameter, final_diameter,
                       depth_of_cut, machine_rate, feed_rates):
    """Compare feeds using the main calculator's machining inputs."""
    feed_rates = sorted(set(feed_rates))
    if len(feed_rates) < 2 or any(not math.isfinite(f) or f <= 0 for f in feed_rates):
        raise ValueError("Enter at least two different positive, finite feed values.")
    # Step 4: Calculate number of machining passes
    passes = math.ceil(
        (initial_diameter - final_diameter) / (2 * depth_of_cut)
    )

    machining_times = []
    machining_costs = []

    # Step 5: Calculate machining time and cost
    for feed in feed_rates:

        time_per_pass = length / (feed * rpm)

        total_time = time_per_pass * passes

        cutting_cost = (total_time / 60) * machine_rate

        machining_times.append(total_time)
        machining_costs.append(cutting_cost)

    # Step 6: Display calculated results
    print("\n--- Engineering Results ---")
    print(f"Number of Passes: {passes}")

    for feed, time, cost in zip(
        feed_rates, machining_times, machining_costs
    ):
        print(
            f"Feed: {feed:.3f} mm/rev | "
            f"Time: {time:.2f} min | "
            f"Cutting Cost: Rs. {cost:.2f}"
        )

    # Step 7: Create figures folder
    figures_folder = Path(__file__).resolve().parent / "figures"
    figures_folder.mkdir(exist_ok=True)

    # Step 8: Graph 1 - Feed Rate vs Machining Time
    plt.figure(figsize=(8, 5))

    plt.plot(feed_rates, machining_times, marker="o")

    plt.xlabel("Feed Rate (mm/rev)")
    plt.ylabel("Total Machining Time (minutes)")
    plt.title("Effect of Feed Rate on Machining Time")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(figures_folder / "feed_vs_time.png", dpi=200)
    # Keep the figure open until both graphs are ready.

    # Step 9: Graph 2 - Feed Rate vs Machining Cost
    plt.figure(figsize=(8, 5))

    plt.plot(feed_rates, machining_costs, marker="o")

    plt.xlabel("Feed Rate (mm/rev)")
    plt.ylabel("Cutting-Time Machine Cost (Rs)")
    plt.title("Effect of Feed Rate on Machining Cost")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(figures_folder / "feed_vs_cost.png", dpi=200)
    # Keep the figure open until both graphs are ready.

    print("\nGraphs generated successfully!")
    print("Both graphs saved in the figures folder.")

    print("Close the graph windows to continue.")
    plt.show()
    plt.close("all")


if __name__ == "__main__":
    print("Run machining_time.py to calculate results and generate graphs together.")
