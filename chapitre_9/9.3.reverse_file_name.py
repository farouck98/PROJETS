def main():
    filename = "example.txt"
    reversed_filename = "reversed_example.txt"
    with open(filename, "r") as source_file, open(reversed_filename, "w") as target_file:
        for line in source_file:
            reversed_line = line.strip("\n")
            reversed_line = reversed_line[::-1]
            reversed_line = reversed_line + "\n"
            target_file.write(reversed_line)

if __name__ == "__main__":
    main()