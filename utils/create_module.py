#!/usr/bin/env python
import json
import os
from os.path import exists
import shutil

from jinja2 import Environment, FileSystemLoader

# Get user inputs
print("\n-- Package Name --")
print("IMPORTANT: always use the same package name for all your modules if you want to package them together.")

package_name = ""
package_exist = False
while not package_exist:
    package_name = input("Only letters, no space, camel case (ie: MyPackage): ")
    package_path = os.path.join(os.getcwd(), "modules", package_name)
    package_exist = exists(package_path)
    if not package_exist:
        print("This package doesn't exist, please enter a valid package name.")

package_description_path = os.path.join(package_path, f"{package_name}.json")

print("\n-- Module class name --")
module_class = ""
while module_class == "":
    module_class = input("(only letters, no space, camel case (ex: JsonReader): ")

# Validate output directory

module_path = os.path.join(package_path, module_class)
is_overwriting = False
if exists(module_path):
    overwrite = input("Warning the module already exist, would you like to overwrite it? (Y/n)")
    if overwrite == "" or overwrite.lower() == "y":
        is_overwriting = True
    else:
        quit()

print("\n-- Module label --")
module_label = ""
while module_label == "":
    module_label = input("(ex: JSON Reader): ")

print("\n-- Module category --")
print("IMPORTANT: this is used to organized the modules within the app, the synthax is crucial if you want your modules to appear in the correct category.")
module_category = ""
while module_category == "":
    module_category = input("(ex: Hypnogram Analysis): ")

print("\n-- Inputs --")
print("(starts with a letter, alphanumerical, no space, snake case) (ex: new_filename): ")
print("Leave empty and press enter when done.")
inputs = []
while True:
    value = input(f"Input {len(inputs)+1}: ")
    if value == '':
        break

    inp = {}
    inp['name'] = value
    inputs.append(inp)

print("\n-- Outputs --")
print("(starts with a letter, alphanumerical, no space, snake case) (ex: my_results): ")
print("Leave empty and press enter when done.")
outputs = []
while True:
    value = input(f"Output {len(outputs)+1}: ")
    if value == '':
        break

    out = {}
    out['name'] = value
    outputs.append(out)

# Load template environment
templates_path = os.path.join(os.getcwd(), "utils","module_templates")
file_loader = FileSystemLoader(templates_path)
env = Environment(loader=file_loader)

# Create a file based on a template
def create_file(template_filename, output_filename):

    template = env.get_template(template_filename)
    output = template.render(
        package_name=package_name,
        module_class=module_class,
        module_label=module_label,
        module_category=module_category,
        inputs=inputs,
        outputs=outputs)

    filepath = os.path.join(module_path, output_filename)
    f = open(filepath, "w", encoding="utf_8")
    f.write(output)
    f.close()

if is_overwriting:
    shutil.rmtree(module_path)

os.mkdir(module_path)

# Create all files
create_file("module_init_template.txt","__init__.py")
create_file("module_description_template.txt", f"{module_class}.json")
create_file("module_template.txt", f"{module_class}.py")
create_file("module_settings_view_template.txt",f"{module_class}SettingsView.py")
create_file("module_results_view_template.txt",f"{module_class}ResultsView.py")
create_file("module_ui_settings_view_template.txt",f"Ui_{module_class}SettingsView.ui")
create_file("module_ui_results_view_template.txt",f"Ui_{module_class}ResultsView.ui")

# Add the modules to the description.json file of the package.
if not is_overwriting:
    with open (package_description_path, "r") as f:
        description = json.loads(f.read())

        if "items" not in description:
            description["items"] = []
            
        description["items"].append(
            {
                "item_name":module_class,
                "item_type": "module",
                "item_version": "0.0.0",
                "item_hooks": [{
                        "endpoint_name": "module_endpoint", 
                        "parameters": {
                            "module_category":module_category, 
                            "module_label":module_label
                        }
                    }]
            }
        )

    # Save the description file
    with open(package_description_path, 'w', encoding="UTF-8") as outfile:
        json_string = json.dumps(description, indent=4)
        outfile.write(json_string)


print("What to do next?")
print("Generate the .py files from all .ui files in the module")
print("- Select the file in Visual Studio Code.")
print("- Right-click")
print("- Select 'Compile Qt UI File'")

print("Done!")