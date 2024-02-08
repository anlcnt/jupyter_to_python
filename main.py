import os
import sys
import subprocess


# Convert .ipynb to code
def convert_ipynb(fullpath: str, format: str = "python") -> bytes:
    fullpath = os.path.basename(os.path.normpath(fullpath))
    filename, file_extension = os.path.splitext(fullpath)

    # Checking the received file for validity
    if file_extension != ".ipynb":
        raise ValueError(f"File \"{fullpath}\" have not *.ipynb extension")

    # Output the result to stdout
    cmd = ["jupyter", "nbconvert", fullpath, "--to", format, "--stdout"]
    return subprocess.check_output(cmd)


# Run .ipynb
def run_ipynb(filepath: str):
    code = convert_ipynb(filepath)
    return exec(code)


if __name__ == "__main__":
    file = sys.argv[-1]  # Here we specify the path to the file
    run_ipynb(file)
