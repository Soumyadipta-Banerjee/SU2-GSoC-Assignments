# Assignment 2: Axisymmetric Turbulent Jet

This folder contains the setup for an axisymmetric, steady-state, turbulent jet case in SU2.

## Folder Contents
- `jet.geo`: Geometry script for Gmsh.
- `jet.su2`: Mesh file generated from the `.geo` script.
- `jet.cfg`: SU2 configuration file for the simulation.
- `report.md`: Detailed report on the setup and results.
- `history.csv`: Solver convergence history.
- `surface.vtu`: Visualization of the boundary results.

## Running the Simulation
1. (Optional) Re-generate the mesh with Gmsh:
   ```bash
   gmsh jet.geo -2 -format su2 -o jet.su2
   ```
2. Run the CFD solver:
   ```bash
   SU2_CFD jet.cfg
   ```
   Alternatively, run in parallel:
   ```bash
   mpirun -n 4 SU2_CFD jet.cfg
   ```
