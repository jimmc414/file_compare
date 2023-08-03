import sys

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        if lines1 == lines2:
            return "identical"

        differences = []
        for i, (line1, line2) in enumerate(zip(lines1, lines2)):
            if line1 != line2:
                differences.append((i, line1.strip(), line2.strip()))

        return differences

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    result = compare_files(file1, file2)

    if result == "identical":
        print("The files are identical.")
    else:
        print("The files are not identical. Differences:")
        for line_num, value1, value2 in result:
            # Print file1 value
            print(f"Line {line_num + 1}: File1: {value1}")
            # Add a few carriage returns to visually separate the values
            print("\n" * 2)
            # Print file2 value
            print(f"Line {line_num + 1}: File2: {value2}\n")

if __name__ == "__main__":
    main()
