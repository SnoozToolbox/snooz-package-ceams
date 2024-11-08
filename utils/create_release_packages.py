import json
import os
import shutil

export_destination = "release"

def create_release_package(package_name, src_folder):
    print(f"Creating release package {package_name}...")
    # Read tools description file
    src_package_folder = os.path.join(src_folder, package_name)
    tools_description_filepath = os.path.join(src_package_folder, f"{package_name}.json")
    f = open (tools_description_filepath, "r")
    tools_description = json.loads(f.read())

    versioned_package_name = f"{package_name}_{tools_description['package_version'].replace('.', '_')}"

    release_folder = os.path.join(export_destination, versioned_package_name, package_name)
    #os.mkdir(release_folder)
    shutil.copytree(os.path.join(src_folder,package_name), release_folder)

if os.path.isdir(export_destination):
    shutil.rmtree(export_destination)
os.mkdir(export_destination)

modules_packages = os.listdir( "modules" )
for folder in modules_packages:
    package_name = os.path.basename(os.path.normpath(folder))
    create_release_package(package_name, "modules")

tools_packages = os.listdir( "tools" )
for folder in tools_packages:
    package_name = os.path.basename(os.path.normpath(folder))
    create_release_package(package_name, "tools")

# Verify if the folder apps exists
if os.path.isdir( "apps" ):
    apps_packages = os.listdir( "apps" )
    for folder in apps_packages:
        package_name = os.path.basename(os.path.normpath(folder))
        create_release_package(package_name, "apps")

print("Done!")

    

