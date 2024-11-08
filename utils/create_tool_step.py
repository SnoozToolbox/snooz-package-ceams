#!/usr/bin/env python
import json
import os
from os.path import exists
from jinja2 import Environment, FileSystemLoader

# Get user inputs
print("\n-- Package Name --")
print("IMPORTANT: always use the same package name for all your tools if you want to package them together.")

package_name = ""
package_exist = False
while not package_exist:
    package_name = input("Only letters, no space, camel case (ie: MyPackage): ")
    package_path = os.path.join(os.getcwd(), "tools", package_name)
    package_exist = exists(package_path)
    if not package_exist:
        print("This package doesn't exist, please enter a valid package name.")

tool_exist = False
while not tool_exist:
    tool_name = input("Tool name (ex:SleepReport): ")
    tool_path = os.path.join(package_path, tool_name)
    tool_exist = exists(tool_path)
    if not tool_exist:
        print("This tool doesn't exist, please enter a valid tool name.")

done = False
while not done:
    # Is it a custom step or not
    is_custom_decision = input("Is this a custom step? (Y/n)")
    if is_custom_decision.lower() == "y" or is_custom_decision == "":
        step_exist = True
        while step_exist:
            step_class = input("Step class (ex:IntroStep): ")
            step_path = os.path.join(tool_path, step_class)
            step_exist = exists(step_path)
            if step_exist:
                print("This step already exist, please enter a valid step name.")

        step_label = input("Step label: ")
        step_description = input("Step description: ")

        # Create module output folder
        root_path = f"{step_path}"
        os.mkdir(step_path)

        # Load template environment
        templates_path = os.path.join(os.getcwd(), "utils","tool_templates")
        file_loader = FileSystemLoader(templates_path)
        env = Environment(loader=file_loader)

        # Create a file based on a template
        def create_file(template_filename, output_filename):

            template = env.get_template(template_filename)
            output = template.render(step_class=step_class, tool_name=tool_name, package_name=package_name)

            filepath = os.path.join(root_path, output_filename)
            f = open(filepath, "w", encoding="UTF-8")
            f.write(output)
            f.close()

        # Create all files
        create_file("step_template.txt", f"{step_class}.py")
        create_file("step_ui_template.txt",f"Ui_{step_class}.ui")

        # Add the step to the description.json file of the parent tool
        tool_description_path = os.path.join(tool_path, f"{tool_name}.json")
        with open (tool_description_path, "r") as f:
            tool_description = json.loads(f.read())
            tool_description["tool_params"]["steps"].append(
                {
                    "name": step_label,
                    "description": step_description,
                    "custom_step_name":step_class,
                    "show_index": True if len(tool_description["tool_params"]["steps"]) > 0 else False
                }
            )

        with open(tool_description_path, 'w', encoding="UTF-8") as outfile:
            json_string = json.dumps(tool_description, indent=4)
            outfile.write(json_string)
    else:
        step_label = input("Step label: ")
        step_description = input("Step description: ")
        module_id = input("Module ID: ")

        # Add the step to the description.json file of the parent tool
        tool_description_path = os.path.join(tool_path, f"{tool_name}.json")
        with open (tool_description_path, "r") as f:
            tool_description = json.loads(f.read())
            tool_description["tool_params"]["steps"].append(
                {
                    "name": step_label,
                    "description": step_description,
                    "module_id":module_id
                }
            )

        with open(tool_description_path, 'w', encoding="UTF-8") as outfile:
            json_string = json.dumps(tool_description, indent=4)
            outfile.write(json_string)
    

    continue_decision = input("Would you like to create another step? (Y/n): ")
    if continue_decision.lower() != "y" and continue_decision.lower() != "":
        done = True


print(f"\nWhat to do next?")
#print(f"- Move the subfolder '{step_class}' into {import_path}")
#print(f"- Add these lines to {init_path}")
#print(f"from presets.{tool_name}.{step_class} import Ui_{step_class}")
#print(f"from presets.{tool_name}.{step_class} import {step_class}")
print(f"- Generate the .py files from the .ui files using pyuic")
