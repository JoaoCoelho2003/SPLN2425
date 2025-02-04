# TPC1

## Thought Process

The goal of this script is to remove repetitive lines from an input stream and write the unique lines to an output file. The script can handle two cases:
1. When an input file is provided as a command-line argument.
2. When no input file is provided, and the user inputs text directly.

## How It Works

### Function: `remove_repetitive_lines_from_stream`

This function takes two arguments:
- `input_stream`: The stream of input lines (either from a file or standard input).
- `output_file`: The name of the file where unique lines will be written.

The function uses a set `seen_lines` to keep track of lines that have already been encountered. For each line in the input stream:
1. The line is stripped of its trailing newline character.
2. If the stripped line is not in `seen_lines`, it is written to the output file, and the line is added to `seen_lines`.

### Function: `main`

This function handles the command-line arguments and determines the input source:
- If more than one argument is provided, it prints a usage message and exits.
- If one argument (the input file) is provided, it opens the file and calls `remove_repetitive_lines_from_stream` with the file stream.
- If no arguments are provided, it prompts the user to enter text directly and calls `remove_repetitive_lines_from_stream` with the standard input stream.

## Usage

### Case 1: Providing an Input File

To run the script with an input file, use the following command:
```sh
python3 repetitiveLines.py input.txt
```

**Example:**
Suppose `input.txt` contains:
```
Hello
World
Hello
Python
```

The script will create `output.txt` with the following content:
```
Hello
World
Python
```

### Case 2: No Input File Provided

To run the script without an input file, use the following command:
```sh
python3 repetitiveLines.py
```

The script will prompt you to enter text. After entering the text, press `Ctrl-D` (or `Ctrl-Z` on Windows) to end the input.

**Example:**
```
Enter the text (Ctrl-D to end input):
Hello
World
Hello
Python
```

The script will create `output.txt` with the following content:
```
Hello
World
Python
```

## Conclusion

This script efficiently removes repetitive lines from an input stream and writes the unique lines to an output file. It can handle both file input and direct user input, making it versatile for different use cases.