import sys
import argparse

def remove_repetitive_lines_from_stream(input_stream, output_file, keep_spaces, comment_empty):
    seen_lines = set()
    with open(output_file, 'w') as outfile:
        for line in input_stream:
            stripped_line = line.rstrip('\n')
            if not keep_spaces:
                stripped_line = stripped_line.strip()
            if stripped_line == '' and comment_empty:
                outfile.write('#\n')
            elif stripped_line not in seen_lines:
                outfile.write(line)
                seen_lines.add(stripped_line)

def main():
    parser = argparse.ArgumentParser(description="Remove repetitive lines from input.")
    parser.add_argument('input_file', nargs='?', help="Input file (default: stdin)")
    parser.add_argument('-s', '--spaces', action='store_true', help="Consider spaces in line comparison")
    parser.add_argument('-p', '--comment', action='store_true', help="Comment empty lines with #")
    args = parser.parse_args()

    output_file = 'output.txt'
    
    if args.input_file:
        with open(args.input_file, 'r') as infile:
            remove_repetitive_lines_from_stream(infile, output_file, args.spaces, args.comment)
    else:
        print("Enter the text (Ctrl-D to end input):")
        remove_repetitive_lines_from_stream(sys.stdin, output_file, args.spaces, args.comment)

if __name__ == "__main__":
    main()