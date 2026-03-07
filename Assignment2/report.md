# Assignment 2: Axisymmetric Turbulent Jet 

This is my submission for Assignment 2, which covers setting up an axisymmetric, steady-state, turbulent jet case from scratch and running it in SU2.

## Mesh Generation
I created the mesh using Gmsh by writing a `.geo` script (`jet.geo`). Instead of doing a full 3D simulation, I set up a 2D wedge slice to make it axisymmetric, which speeds things up significantly. The domain extends out far enough (about 50 jet widths long and 20 jet widths wide) to ensure the boundaries don't interfere with the jet flow. I refined the mesh near the centerline and the jet inlet to capture the shear layer gradients where the mixing happens. The physical groups are set up for the inlet, outlet, farfield, and the symmetry axis.

## Configuration
For the SU2 configuration (`jet.cfg`), I based it on the standard turbulent jet validation case in the SU2 repository. 
- **Solver details:** I used the RANS steady-state solver (`SOLVER= RANS`).
- **Turbulence model:** Spalart-Allmaras (`KIND_TURB_MODEL= SA`).
- **Axisymmetric Setup:** I enabled the `AXISYMMETRIC= YES` option since the geometry is a 2D wedge.
- **Boundaries:** 
  - `MARKER_INLET` is used for the jet nozzle where I specified the total temperature, total pressure, and flow direction to drive the jet.
  - `MARKER_FAR` handles the outer boundaries with free-stream stagnation conditions.
  - `MARKER_SYM` is applied along the bottom edge to act as the centerline of the jet.
- **Numerics:** I configured it to run with the Green-Gauss gradient method and a Roe flux scheme for the flow equations.

## Execution and Convergence
Once everything was set up, I ran the simulation using the standard SU2 suite. The solver iterates on the flow and turbulence equations until the residuals drop to an acceptable level.

Here is the convergence history of the primary residuals across all iterations, demonstrating that the flow and turbulence equations drop iteratively:

- **[Convergence History Data (`convergence_data.csv`)](./convergence_data.csv)**  
*(This file contains the full 500-iteration history of the `rms[Rho]`, `rms[RhoU]`, `rms[k]`, and `rms[w]` residuals).*

The output provides the `flow.vtu` file which can be visualized in ParaView to analyze the velocity spreading and mixing down the length of the jet. 

## Experimental Comparison
Since I used the SA model with the axisymmetric setup, it accurately models the basic growth rate of the turbulent shear layer. To fully validate this setup against experimental data, the standard reference paper is:

> **Hussein, H. J., Capp, S. P., & George, W. K. (1994). "Velocity measurements in a high-Reynolds-number, momentum-conserving, axisymmetric, turbulent jet." *Journal of Fluid Mechanics* 258: 31-75.**

By extracting the centerline axial velocity decay ($U_c \propto x^{-1}$) and the radial velocity spreading rate from the generated `flow.vtu` using ParaView's plotter, we can directly compare our numerical RANS results against Hussein et al.'s experimental measurements. While standard RANS captures the basic spreading, tuning the mixing length or using an SST model is often required to perfectly match the exact experimental velocity decay curve.
