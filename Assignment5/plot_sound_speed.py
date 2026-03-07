import matplotlib
matplotlib.use('Agg') # Force non-GUI backend
import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET

def plot_vtu(vtu_file, output_img):
    print(f'Reading {vtu_file}...')
    with open(vtu_file, 'rb') as f:
        full_content = f.read()
    
    tag = b'<AppendedData encoding=\"raw\">'
    appended_start = full_content.find(tag)
    if appended_start == -1:
        print('Error: Could not find AppendedData tag')
        return

    xml_content = full_content[:appended_start].decode('utf-8', errors='ignore') + '</VTKFile>'
    root = ET.fromstring(xml_content)
    
    data_section_start = full_content.find(b'_', appended_start) + 1
    
    def get_data(name):
        for da in root.findall('.//DataArray'):
            if da.get('Name') == name:
                offset = int(da.get('offset'))
                d_start = data_section_start + offset
                length = np.frombuffer(full_content[d_start : d_start + 8], dtype=np.uint64)[0]
                data = np.frombuffer(full_content[d_start + 8 : d_start + 8 + int(length)], dtype=np.float32)
                return data
        return None

    coords = None
    for da in root.findall('.//Points/DataArray'):
        offset = int(da.get('offset'))
        d_start = data_section_start + offset
        length = np.frombuffer(full_content[d_start : d_start + 8], dtype=np.uint64)[0]
        coords = np.frombuffer(full_content[d_start + 8 : d_start + 8 + int(length)], dtype=np.float32)
        break
        
    sound_speed = get_data('Sound_Speed')
    
    if coords is not None and sound_speed is not None:
        n_points = len(sound_speed)
        x = coords[0:n_points*3:3]
        y = coords[1:n_points*3:3]
        
        plt.figure(figsize=(10, 5))
        try:
             plt.tricontourf(x, y, sound_speed, levels=100, cmap='inferno')
        except:
             plt.scatter(x, y, c=sound_speed, s=5, cmap='inferno')
             
        plt.colorbar(label='Speed of Sound (m/s)')
        plt.xlabel('X coordinate [m]')
        plt.ylabel('Y coordinate [m]')
        plt.title('Speed of Sound Field (SU2 Volume Output)')
        plt.axis('equal')
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.savefig(output_img, dpi=200, bbox_inches='tight')
        print(f'Successfully saved plot to {output_img}')
    else:
        print('Error: Could not find required data in VTU')

vtu_path = '/home/soumya/SU2-GSoC-Assignments/Assignment5/vol_solution.vtu'
img_path = '/home/soumya/SU2-GSoC-Assignments/Assignment5/sound_speed_visualization.png'
plot_vtu(vtu_path, img_path)
