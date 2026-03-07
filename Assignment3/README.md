# Assignment 3: Python Wrapper Test Case

This folder demonstrates how to run a steady-state flat plate RANS case using the SU2 Python wrapper.

## Folder Contents
- `turb_SA_flatplate.cfg`: SU2 configuration file modified for the Python wrapper test.
- `mesh_flatplate_turb_137x97.su2`: Mesh file for the flat plate.
- `report.md`: Small report on building the wrapper and the testcase.
- `history.csv`: Solver convergence history.
- `flow.vtu`, `surface_flow.vtu`: Visualization files.

## Running the Simulation
1. Make sure the SU2 Python wrapper is built and installed.
2. Set your environment variables:
   ```bash
   export SU2_RUN=/path/to/SU2/install/bin
   export PYTHONPATH=$SU2_RUN:$PYTHONPATH
   ```
3. Run the CFD solver via the Python script:
   ```bash
   python3 $SU2_RUN/SU2_CFD.py -f turb_SA_flatplate.cfg
   ```
   Or in parallel:
   ```bash
   mpirun -n 4 python3 $SU2_RUN/SU2_CFD.py -f turb_SA_flatplate.cfg --parallel
   ```
