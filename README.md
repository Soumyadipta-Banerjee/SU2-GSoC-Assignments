# SU2 GSoC Assignments

This repository contains my work for the SU2 Foundation's Google Summer of Code (GSoC) qualification assignments.

I've been working through the assignment list to get familiar with compiling SU2, setting up cases, using the Python wrapper, and eventually diving into the C++ source code to add new features.

## Assignment Progress

- **Assignment 1: Compilation**  
  Compiled the SU2 suite from source on my Linux machine using Meson and Ninja. (No files to submit for this one).

- **[Assignment 2: Test Case from Scratch](./Assignment2)**  
  Created a 2D axisymmetric mesh for a turbulent jet using Gmsh and set up the SU2 config to solve it using the RANS equations and the Spalart-Allmaras turbulence model.  
  *➡️ [Read the full Report](./Assignment2/report.md)*

- **[Assignment 3: Python Wrapper](./Assignment3)**  
  Recompiled SU2 to generate the Python wrapper (`pysu2`) and ran a standard flat plate case directly from a Python script instead of the command line.  
  *➡️ [Read the full Report](./Assignment3/report.md)*

- **[Assignment 4: Modifying python wrapper](./Assignment4)**  
  Wrote a custom Python script that interfaces with `pysu2` to dynamically apply a spatially varying temperature gradient to the wall boundary condition of the flat plate case.  
  *➡️ [Read the full Report](./Assignment4/report.md)*

- **[Assignment 5: C++ Code Modification](./Assignment5)**  
  Dug into `CFlowCompOutput.cpp` in the SU2 source code to expose the local speed of sound as a new output field. Modified the codebase so it can be written out to `.vtu` volume files and the `.csv` history logs.  
  *➡️ [Read the full Report](./Assignment5/report.md)*

Each assignment folder details the simulation setup and provides visualization of the results.
