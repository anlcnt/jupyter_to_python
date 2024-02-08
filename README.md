# Jupyter Notebook to Python Converter
This Python code is designed to convert .ipynb files to Python code and run that code.

The ```convert_ipynb``` function takes the path to the .ipynb file and the output format (defaults to "python"). It checks that the file has the correct extension, and then uses the jupyter nbconvert command to convert the file to code.

The ```run_ipynb``` function runs the .ipynb file, calling the convert_ipynb function and then executing the resulting code.

At the end of the code, there is an if ```__name__ == "__main__":``` block that runs the run_ipynb function with the file specified on the command line.

To use this code, make sure you have Jupyter and Python installed. You can then run the code by specifying the path to the .ipynb file on the command line.

## How to use

To use this code, follow these steps:

1. Make sure you have Jupyter and Python installed.
2. Open a terminal or command prompt.
3. Navigate to the directory where the .ipynb file you want to convert is located.
4. Run the code by typing the following command:

```
python main.py path/to/your.ipynb
```

where ```path/to/your.ipynb``` is the path to your .ipynb file.

Once this command is executed, the code in the .ipynb file will be converted to Python code and executed.
