#!/bin/bash

# Ensure the script exits if any command fails
set -e

# Debug: print the current working directory
echo "Running script in $(pwd)"

# Check if the environment.yml file exists
if [[ ! -f "environment.yml" ]]; then
    echo "environment.yml not found! Please make sure you're in the correct directory."
    exit 1
fi

# Create the Conda environment
echo "Creating the Conda environment..."
conda env create -f environment.yml

# Activate the environment
echo "Activating the Conda environment..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate aiChess

# Check if the requirements.txt file exists and install additional dependencies
if [[ -f "requirements.txt" ]]; then
    echo "Installing additional dependencies from requirements.txt..."
    pip install -r $(pwd)/requirements.txt
else
    echo "requirements.txt not found, skipping pip install step."
fi

# Provide instructions to the user
echo "Setup complete!"
echo "To activate the environment, run: conda activate aiChess"
echo "You can now run your code using: python src/main.py"

# Optional: Print a success message and some additional information
echo "Environment setup was successful!"
echo "You are now ready to start developing with the following packages installed:"
conda list
