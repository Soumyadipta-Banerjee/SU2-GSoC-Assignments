# Assignment 4: Spatially Varying Wall Temperature via Python Wrapper

## Overview
This assignment demonstrates the ability to programmatically control boundary conditions in SU2 using the Python wrapper (`pysu2`). The goal was to apply a spatially varying temperature gradient along the wall of a steady-state, compressible, turbulent flat plate.

## Implementation Details

### Configuration
A baseline RANS simulation of a flat plate using the Spalart-Allmaras (SA) turbulence model was used. The following modifications were made to the SU2 configuration file (`turb_SA_flatplate.cfg`):
- `MARKER_PYTHON_CUSTOM= ( wall )`: Enabled custom Python-driven boundary conditions on the 'wall' marker.
- `MARKER_ISOTHERMAL= ( wall, 300.0 )`: Provided a baseline isothermal boundary condition, which is overridden by the Python script.

### Python Steering Script
A Python script (`run_flatplate_temp.py`) was developed to drive the simulation:
1. **Initialization:** The SU2 driver was initialized using `pysu2.CSinglezoneDriver`.
2. **Coordinates Extraction:** Node coordinates on the 'wall' marker were extracted using `driver.MarkerCoordinates(wall_id)`.
3. **Temperature Mapping:** A linear temperature gradient was calculated as a function of the x-coordinate: $T(x) = T_{ref} + 100.0 \cdot x$, where $T_{ref} = 300 K$.
4. **Boundary Update:** The custom temperatures were applied to each vertex using `driver.SetMarkerCustomTemperature(...)`.
5. **Execution:** The solver was run for 100 iterations using the `driver.StartSolver()` method.

## Results and Verification
The simulation successfully completed the specified 100 iterations. Verification was performed by checking the generated `surface_flow.vtu` file, which confirms that the `Temperature` field was successfully applied to the wall boundary nodes.

### Convergence
The RANS solver exhibited typical convergence behavior for a turbulent flat plate case, despite the added temperature gradient.

## Conclusion
The SU2 Python wrapper effectively enables complex boundary condition steering without requiring modifications to the underlying C++ solver code. This functionality is essential for coupled simulations, optimization loops, and non-trivial physical setups.
