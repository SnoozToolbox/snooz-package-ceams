## 
# Convert process description file (description.json) into the new simplified versioning version
# This will remove all versions for all modules and add a dependency attribute to the base of the 
# description file.
#
## How to use:
# 
# Use either the path to a description file, ex:
# python convert_process_description_to_simplified_version.py the/path/to/my/file/desciption.json
# 
# Or the path to the tools folder to convert all tools from a package, ex:
# python convert_process_description_to_simplified_version.py the/path/to/my/package_tools/

import json
import os
from struct import pack
import sys

def update_process_description(process_description_filepath):
    f = open (process_description_filepath, "r")
    description = json.loads(f.read())

    dependencies = []

    for node in description["nodes"]:
        print("  " + node["module_name"])
        package_version = node["package"]["package_version"]
        package_name = node["package"]["package_name"]
        del node["package"]["package_version"]
        del node["package"]["package_author"]
        del node["package"]["package_url"]
        del node["module_version"]
        pack = find_dependency(dependencies, package_name)
        if pack is None:
            dependencies.append({
                "package_name": package_name,
                "package_version": package_version
            })

    if "tool_description" in description:
        if "tool_version" in description["tool_description"]:
            del description["tool_description"]["tool_version"]
        if "package_version" in description["tool_description"]:
            del description["tool_description"]["package_version"]
    
    description["dependencies"] = dependencies

    with open(process_description_filepath, 'w', encoding="UTF-8") as outfile:
        json_string = json.dumps(description, indent=4)
        outfile.write(json_string)

def find_dependency(dependencies, package_name):
    for dep in dependencies:
        if dep["package_name"] == package_name:
            return dep
    return None

def main():
    if len(sys.argv) != 2:
        print("Missing parameter.")
        print("")
        print("Use either the path to a description file, ex:")
        print("python convert_process_description_to_simplified_version.py the/path/to/my/file/desciption.json")
        print("")
        print("Or the path to the tools folder to convert all tools from a package, ex:")
        print("python convert_process_description_to_simplified_version.py the/path/to/my/package_tools/")

    if ".json" in sys.argv[1]:
        update_process_description(sys.argv[1])
    else:
        root_folder = sys.argv[1]

        process_folders = os.listdir( root_folder )
        for folder in process_folders:
            process_name = os.path.basename(os.path.normpath(folder))
            process_path = os.path.join(root_folder, process_name)
            if os.path.isdir(process_path):

                print(f"Updating {process_name}")
                process_description_filepath = os.path.join(process_path, "description.json")
                update_process_description(process_description_filepath)
    
main()