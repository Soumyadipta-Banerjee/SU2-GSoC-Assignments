# Assignment 4: Modification of the Python Wrapper Setup

## Overview
This folder contains the setup and results for Assignment 4, which involves implementing a spatially varying wall temperature for a turbulent flat plate case using the SU2 Python wrapper.

## Contents
- `turb_SA_flatplate.cfg`: SU2 configuration file modified for Python-driven boundary conditions.
- `run_flatplate_temp.py`: Python script that applies the temperature gradient and drives the simulation.
- `report.md`: A summary report describing the implementation and results.

## Prerequisites
- SU2 compiled with Python wrapper support.
- `pysu2`, `mpi4py`, and `numpy` installed in your Python environment.
- `SU2_RUN` and `PYTHONPATH` environment variables set correctly.

## How to Run
To run the simulation with the custom temperature gradient:

```bash
python3 run_flatplate_temp.py
```

Or in parallel with MPI:

```bash
mpirun -n 4 python3 run_flatplate_temp.py
```

## Results
The simulation generates `flow.vtu` and `surface_flow.vtu` files, which can be visualized in ParaView to verify the spatial variation of the temperature field on the wall.
