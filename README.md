# ZCode Compiler

ZCode is a general-purpose block-structured procedural programming language designed for students practicing the implementation of a basic compiler.

## Instructions

### Setting up Environment Variables

Set the environment variable `ANTLR_JAR` to the file `antlr-4.9.2-complete.jar` on your computer.

### Changing Directory

Navigate to the `initial/src` directory where the `run.py` file is located.

### Generating Code

Run the command:
```bash
python run.py gen
```
### Running Tests
To test the generated code, run the command:
```bash
python run.py test ASTGenSuite
```
Replace ASTGenSuite with the name of the test you want to run.

### Viewing Results
Check the `testcases` and `solutions` folders for the results

Make sure to follow these instructions in sequence for setting up, generating, and testing your code. If you encounter any issues, ensure that you've correctly set up the environment variable and are running the commands from the correct directory.
