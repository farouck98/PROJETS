def main():
    source_file = "example.txt"
    with open(source_file, "r") as f:
        for i, line in enumerate(f, start=1):
            print(f"line {i} has {len(line.split(' '))} words.")

if __name__ == "__main__":
    main()