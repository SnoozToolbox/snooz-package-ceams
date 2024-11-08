#!/usr/bin/env python
import json
import os
from os.path import exists
import shutil

from jinja2 import Environment, FileSystemLoader

# Get user inputs
print("\n-- Package Name --")
print("IMPORTANT: always use the same package name for all your apps if you want to package them together.")

package_name = ""
package_exist = False
while not package_exist:
    package_name = input("Only letters, no space, camel case (ie: MyPackage): ")
    package_path = os.path.join(os.getcwd(), "apps", package_name)
    package_exist = exists(package_path)
    if not package_exist:
        print("This package doesn't exist, please enter a valid package name.")

package_description_path = os.path.join(package_path, f"{package_name}.json")

print("\n-- App class name --")
app_class = ""
while app_class == "":
    app_class = input("(only letters, no space, camel case (ex: EEGViewer): ")

# Validate output directory

app_path = os.path.join(package_path, app_class)
is_overwriting = False
if exists(app_path):
    overwrite = input("Warning the app already exist, would you like to overwrite it? (Y/n)")
    if overwrite == "" or overwrite.lower() == "y":
        is_overwriting = True
    else:
        quit()

print("\n-- App label --")
app_label = ""
while app_label == "":
    app_label = input("(ex: EEG Viewer): ")

print("\n-- App menu category --")
print("IMPORTANT: this is used to menu category the app will appear under.")
app_category = ""
while app_category == "":
    app_category = input("(ex: Viewers): ")


# Load template environment
templates_path = os.path.join(os.getcwd(), "utils","app_templates")
file_loader = FileSystemLoader(templates_path)
env = Environment(loader=file_loader)

# Create a file based on a template
def create_file(template_filename, output_filename):

    template = env.get_template(template_filename)
    output = template.render(
        package_name=package_name,
        app_class=app_class,
        app_label=app_label,
        app_category=app_category)

    filepath = os.path.join(app_path, output_filename)
    f = open(filepath, "w", encoding="utf_8")
    f.write(output)
    f.close()

if is_overwriting:
    shutil.rmtree(app_path)

os.mkdir(app_path)

# Create all files
create_file("app_description_template.txt", f"{app_class}.json")
create_file("app_init_template.txt","__init__.py")
create_file("app_view_template.txt", f"{app_class}View.py")
create_file("app_view_ui_template.txt",f"Ui_{app_class}View.ui")
create_file("app_view_ui_py_template.txt",f"Ui_{app_class}View.py")

# Add the app to the description.json file of the package.
if not is_overwriting:
    with open (package_description_path, "r") as f:
        description = json.loads(f.read())

        if "items" not in description:
            description["items"] = []
            
        description["items"].append(
            {
                "item_name":app_class,
                "item_type": "app",
                "item_version": "0.0.0",
                "item_hooks": [{
                    "endpoint_name": "menu_endpoint",
                    "parameters": {
                        "menu_category":app_category, 
                        "menu_label":app_label
                    }},
                    {
                        "endpoint_name": "file_menu_endpoint",
                        "parameters": {
                            "app_label":app_label
                        }
                }]
            }
        )

    # Save the description file
    with open(package_description_path, 'w', encoding="UTF-8") as outfile:
        json_string = json.dumps(description, indent=4)
        outfile.write(json_string)

print("Done!")