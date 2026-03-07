# Assignment 3: Python Wrapper Test Case

This folder contains the setup and results for Assignment 3, which involves running the `flatplate` test case using the SU2 Python wrapper.

## Setup and Execution
To run the python wrapper, I first had to build SU2 with the wrapper enabled. I configured the build using meson (`-Denable-pywrapper=true`) and installed the necessary python dependencies: `swig`, `mpi4py`, `scipy` and `numpy`. After compiling, I set my `SU2_RUN` and `PYTHONPATH` environment variables so the script could find the `pysu2` module.

For the testcase itself, I grabbed the `turb_SA_flatplate.cfg` configuration from the `TestCases/rans/flatplate` directory in the SU2 repository. To avoid waiting too long for the solver, I dropped the `ITER` count from 99999 down to 250 in the config file.

I launched the simulation using MPI to speed it up across 4 cores:
```bash
mpiexec -n 4 python3 $SU2_RUN/SU2_CFD.py -f turb_SA_flatplate.cfg --parallel
```

## Results
The simulation ran without any issues using the Spalart-Allmaras (SA) turbulence model. After 250 iterations, it hit the maximum limit and exited normally.

Here are the final residuals at iteration 250:
- `rms[Rho]`: -5.51145
- `rms[nu]`: -7.11571
- `CL`: -0.187520
- `CD`: 0.004696

The solver successfully generated the output files, including `restart_flow.dat`, `flow.vtu` and `surface_flow.vtu`.
