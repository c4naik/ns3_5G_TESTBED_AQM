#!/bin/bash

# Define the source directories
src_dirs=(
"./Output/ns3::CoDelQueueDisc/Images/"
"./Output/ns3::CobaltQueueDisc/Images/"
"./Output/ns3::PieQueueDisc/Images/"
"./Output/ns3::FqPieQueueDisc/Images/"
"./Output/ns3::FqCoDelQueueDisc/Images/"
)

# Define the destination directory
dest_dir="./Output/graphs/"

# Loop over the source directories
for src_dir in "${src_dirs[@]}"; do
  # Extract the directory name, replace "::" with "_" and append "_Images"
  dir_name=$(basename $(dirname "$src_dir"))
  new_dir_name="${dir_name//::/_}_Images"

  # Construct the destination directory path
  dest_path="${dest_dir}${new_dir_name}"

  # Create the destination directory if it doesn't exist
  mkdir -p "$dest_path"

  # Copy the files
  cp -r "${src_dir}." "$dest_path"
done

echo "Directories copied successfully."

