import subprocess
import sys

def run_script(script_name):
    print(f"\nRunning {script_name}...\n")
    result = subprocess.run([sys.executable, script_name])
    
    if result.returncode != 0:
        print(f"\nError running {script_name}")
        sys.exit(1)

# -----------------------------
# PIPELINE ORDER
# -----------------------------
scripts = [
    "analysis_pipeline.py",
    "figure1.py",
    "figure2.py",
    "figureS1.py"
]

for script in scripts:
    run_script(script)

print("\nAll analyses completed successfully.")
