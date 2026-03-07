import pysu2
import mpi4py.MPI as MPI
import sys

def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Load the configuration file
    config_file = "turb_SA_flatplate.cfg"
    
    # Initialize the SU2 driver
    try:
        # The constructor will perform initial preprocessing including PreprocessPythonInterface
        driver = pysu2.CSinglezoneDriver(config_file, 1, comm)
    except Exception as e:
        if rank == 0:
            print(f"Error initializing SU2 driver: {e}")
        return
    
    # Get marker information
    marker_indices = driver.GetMarkerIndices()
    if 'wall' not in marker_indices:
        if rank == 0:
            print("Error: 'wall' marker not found in configuration.")
        driver.Finalize()
        return

    wall_marker_id = marker_indices['wall']
    num_marker_nodes = driver.GetNumberMarkerNodes(wall_marker_id)
    
    # Get coordinates of the wall nodes
    coords = driver.MarkerCoordinates(wall_marker_id)
    
    # Apply a spatially varying temperature
    # T(x) = T_ref + 100 * x
    T_ref = 300.0
    
    if rank == 0:
        print(f"Rank {rank}: Applying temperature gradient $T(x) = 300 + 100x$ on 'wall' marker ({num_marker_nodes} nodes)...")

    # Set temperature for each node on the wall
    for i in range(num_marker_nodes):
        # Use .Get(i, j) for CPyWrapperMarkerMatrixView
        x = coords.Get(i, 0)
        target_temp = T_ref + 100.0 * x
        driver.SetMarkerCustomTemperature(wall_marker_id, i, target_temp)

    # Launch the solver for the entire computation (100 iterations as per config)
    if rank == 0:
        print("Starting SU2 solver loop...")
    
    # We can also use driver.BoundaryConditionsUpdate() to ensure the values are picked up
    # but StartSolver() should handle it.
    driver.StartSolver()

    # Finalize and save results
    driver.Finalize()

    if rank == 0:
        print("Simulation finished successfully. Output files generated.")

if __name__ == "__main__":
    main()
