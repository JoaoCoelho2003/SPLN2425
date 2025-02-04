import sys

def remove_repetitive_lines_from_stream(input_stream, output_file):
    seen_lines = set()
    with open(output_file, 'w') as outfile:
        for line in input_stream:
            stripped_line = line.rstrip('\n')
            if stripped_line not in seen_lines:
                outfile.write(line)
                seen_lines.add(stripped_line)

def main():
    if len(sys.argv) > 2:
        print("Usage: python3 repetitiveLines.py [<input_file>]")
        sys.exit(1)
    
    output_file = 'output.txt'
    
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        with open(input_file, 'r') as infile:
            remove_repetitive_lines_from_stream(infile, output_file)
    else:
        print("Enter the text (Ctrl-D to end input):")
        remove_repetitive_lines_from_stream(sys.stdin, output_file)

if __name__ == "__main__":
    main()