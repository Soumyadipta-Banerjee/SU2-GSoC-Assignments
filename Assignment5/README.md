# Assignment 5: Speed of Sound Output

## Overview
Adds the local speed of sound as a new volume and screen/history output field in SU2's compressible flow solver.

## Files
- `jet_sound.cfg` — Config file for the turbulent jet case with speed of sound output enabled
- `jet.su2` — Mesh file (reused from Assignment 2)
- `report.md` — Detailed report explaining the implementation and results
- `history.csv` — Simulation history with `SoundSpeed` column (column 24)
- `vol_solution.vtu` — Volume output with `Sound_Speed` field (viewable in ParaView)

## C++ Changes
Branch: `feature/add-sound-speed-output` in `~/SU2/`  
File: `SU2_CFD/src/output/CFlowCompOutput.cpp`  
- Registered `SOUND_SPEED` as volume output (`PRIMITIVE` group)
- Registered `SOUND_SPEED` as history/screen output (`FLOW_COEFF` group)
- Loads local value per grid point via `GetSoundSpeed(iPoint)`
- Computes domain-averaged value for history with MPI reduction

## Running
```bash
cd ~/SU2 && git checkout feature/add-sound-speed-output
ninja -C build install
cd ~/SU2-GSoC-Assignments/Assignment5
~/SU2/build/install/bin/SU2_CFD jet_sound.cfg
```
