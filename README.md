# Machining Time and Cost Calculator

### Python-Based Manufacturing Engineering Analysis

A Python-based engineering calculator developed to estimate machining time, cutting speed, the number of turning passes, and machine operating cost for conventional turning operations.

This project applies fundamental concepts of **Manufacturing Engineering, Machining Science, and Industrial Engineering** through computational methods.

## 1. Project Objectives

- Develop an interactive machining calculation tool using Python.
- Estimate cutting time for single-pass and multiple-pass turning operations.
- Calculate cutting speed based on workpiece diameter and spindle speed.
- Determine the number of passes required for a specified diameter reduction.
- Estimate machine operating costs based on machining time.
- Explore the influence of machining parameters on manufacturing efficiency.

## 2. Current Features

- Interactive user input for machining parameters.
- Automatic calculation of the number of turning passes.
- Machining time estimation per pass and for the complete operation.
- Initial cutting speed calculation.
- Cutting-time-based machine cost estimation.
- Input validation for invalid or non-positive parameters.
- Option to perform repeated calculations without restarting the program.

## 3. Engineering Methodology

The calculator uses fundamental turning-operation equations.

### 3.1 Number of Machining Passes

For a specified maximum radial depth of cut:

\[
n = \left\lceil \frac{D_i-D_f}{2a_p} \right\rceil
\]

Where:

- **n** = Number of machining passes
- **Dᵢ** = Initial workpiece diameter (mm)
- **Dբ** = Final workpiece diameter (mm)
- **aₚ** = Maximum radial depth of cut (mm)

The calculated number of passes is rounded upward to the nearest integer.

### 3.2 Machining Time

Time required for one turning pass:

\[
T_p = \frac{L}{fN}
\]

Total machining time:

\[
T_m = n \times T_p
\]

Where:

- **Tₚ** = Machining time per pass (min)
- **Tₘ** = Total cutting time (min)
- **L** = Tool travel length (mm)
- **f** = Feed per revolution (mm/rev)
- **N** = Spindle speed (rpm)

### 3.3 Cutting Speed

Initial cutting speed is estimated using:

\[
V_c = \frac{\pi D_i N}{1000}
\]

Where:

- **V꜀** = Initial cutting speed (m/min)
- **Dᵢ** = Initial workpiece diameter (mm)
- **N** = Spindle speed (rpm)

### 3.4 Machining Cost Estimation

The cutting-time-based machine operating cost is calculated as:

\[
C_m = \frac{T_m}{60}\times R
\]

Where:

- **Cₘ** = Estimated machine operating cost (₹)
- **Tₘ** = Total cutting time (min)
- **R** = Machine operating rate (₹/hour)

This estimate excludes setup costs, tooling costs, material costs, and other non-cutting expenses.

## 4. Sample Calculation

The following example demonstrates the calculator's functionality.

### Input Parameters

| Parameter | Value |
|---|---:|
| Tool travel length | 100 mm |
| Feed rate | 0.2 mm/rev |
| Spindle speed | 500 rpm |
| Initial diameter | 60 mm |
| Final diameter | 50 mm |
| Radial depth of cut | 1 mm |
| Machine hourly rate | ₹600/hour |

### Calculated Results

| Output | Result |
|---|---:|
| Number of passes | 5 |
| Machining time per pass | 1.00 min |
| Total machining time | 5.00 min |
| Total machining time | 300.00 sec |
| Initial cutting speed | 94.25 m/min |
| Estimated machine operating cost | ₹50.00 |

These results illustrate the relationship between machining parameters, cutting time, and operating cost.

## 5. Tools and Technologies

- **Programming Language:** Python 3
- **Development Environment:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub
- **Python Libraries:** `math` (Python standard library)

No additional third-party Python packages are required for the current version.

## 6. How to Run the Project

1. Install Python 3 on your computer.
2. Clone or download this GitHub repository.
3. Open the project folder in Visual Studio Code.
4. Open a terminal in the project folder.
5. Execute the following command:

   `python3 machining_time.py`

6. Enter the requested machining parameters.
7. Review the calculated results.
8. Choose whether to perform another calculation.

## 7. Project Structure

**machining-time-cost-calculator/**

- `machining_time.py` — Python source code for machining calculations.
- `README.md` — Project documentation, engineering equations, and usage instructions.

## 8. Assumptions and Limitations

The current model is intended for preliminary engineering calculations and educational purposes.

- The turning operation is modeled using constant spindle speed and feed.
- Axial tool travel is assumed identical for every pass.
- The number of passes is estimated using the maximum specified radial depth of cut.
- The final pass may use a smaller depth of cut.
- Cutting speed is calculated at the initial workpiece diameter; it changes as the workpiece diameter decreases under constant RPM.
- Setup time, tool changes, tool return time, and other non-cutting operations are excluded.
- The cost model considers machine operating time during cutting only.
- Cutting-tool constraints, material-specific machining parameters, and machine capacity are not independently verified.

The results should therefore be interpreted as simplified estimates rather than complete industrial process plans.

## 9. Future Development

Planned improvements include:

- Setup-time and tool-change-time estimation.
- More detailed manufacturing cost analysis.
- Material Removal Rate (MRR) calculations.
- Tooling and material cost estimation.
- Cutting parameter analysis for different materials.
- Graphical visualization of machining parameters.
- Improved input validation and modular Python code.
- Comparison of alternative machining strategies.

## 10. Project Status

**Status: Functional prototype — Under active development**

The current version implements interactive multiple-pass turning calculations, machining time estimation, initial cutting speed, and basic operating cost estimation.

Further development will focus on engineering accuracy, cost modeling, visualization, and code improvements.

## 11. Author

**Atharva Shingane**

Incoming Master's Student in Mechanical Engineering

B.Tech in Manufacturing Science and Industrial Management

**GitHub:** [atharvapravinshingane](https://github.com/atharvapravinshingane)

---

*This project is part of an ongoing effort to develop computational engineering skills and apply manufacturing science principles to practical engineering problems.*