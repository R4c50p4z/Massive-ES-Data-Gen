"""
    This script first of all generates the 3 files with the data, and after of this it generates the final
    CSV file with the random combinations of data
"""

import subprocess
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# List of scripts to execute in order
scripts = [
    "DNI_Random_Generator.py",
    "IBAN_Generator.py",
    "Name_Generator.py",
    "Anonamizer.py"
]

# Execute each script
for script in scripts:
    script_path = os.path.join(script_dir, script)
    print(f"Executing {script}...")
    subprocess.run(["python", script_path])
    print(f"{script} completed.\n")

print("All scripts executed successfully!")