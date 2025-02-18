# TPC2: Added Flags to document empty lines and consider spaces

This script is designed to remove repetitive lines from an input stream, such as a file or standard input, and write the unique lines to an output file. Additionally, it provides options to handle spaces in line comparisons and to comment empty lines.

## Features

- **Consider Spaces**: An optional flag to consider spaces in line comparisons.
- **Comment Empty Lines**: An optional flag to comment empty lines with the `#` character.

## Thought Process

The main goal of this script is to filter out repetitive lines from the input and write only unique lines to the output file. To enhance its functionality, two additional features were added:

1. **Consider Spaces**: By default, the script ignores leading and trailing spaces when comparing lines. However, with the `-s` flag, spaces are considered, making lines with different spacing unique.
2. **Comment Empty Lines**: By default, empty lines are ignored. With the `-p` flag, empty lines are commented out with the `#` character instead of being ignored.

## Usage

The script can be run from the command line with the following options:

```sh
python script.py input_file -s -p
```

### Examples

#### Example 1: Default Behavior

**Input File:**
```
hello
world
hello
```

**Output File:**
```
hello
world
```

#### Example 2: Considering Spaces (`-s` flag)

**Input File:**
```
hello
 world
hello
```

**Command:**
```sh
python script.py input_file -s
```

**Output File:**
```
hello
 world
```

#### Example 3: Commenting Empty Lines (`-p` flag)

**Input File:**
```
hello

world
```

**Command:**
```sh
python script.py input_file -p
```

**Output File:**
```
hello
#
world
```

#### Example 4: Combining Both Flags (`-s` and `-p`)

**Input File:**
```
hello

 world
hello
```

**Command:**
```sh
python script.py input_file -s -p
```

**Output File:**
```
hello
#
 world
```

For more details on the repetitive line removal, refer to TPC1 documentation.
