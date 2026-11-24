import base64
import os

# List of artifact example images to convert
image_files = ['cohort_psa_mean_std_Total_CZ-A1_3x2.png', 'cohort_psa_mean_std_Total_O1-A2_3x2.png']

# Variable names for each image
variable_names = ['IMAGE_BASE64_CZ', 'IMAGE_BASE64_O1']

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the data file
output_file = os.path.join(script_dir, 'image_data_base64.py')

with open(output_file, 'w') as f:
    f.write('"""\n')
    f.write('Base64 encoded images\n')
    f.write('"""\n\n')
    
    for image_file, var_name in zip(image_files, variable_names):
        try:
            with open(os.path.join(script_dir, image_file), 'rb') as img_f:
                image_data = base64.b64encode(img_f.read()).decode()
                f.write(f'{var_name} = """\n')
                f.write(image_data)
                f.write('\n""".strip()\n\n')
        except FileNotFoundError:
            print(f"Warning: {image_file} not found in {script_dir}")
            f.write(f'{var_name} = ""\n\n')

print(f"Created {output_file}")
