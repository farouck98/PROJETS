def main():
    filename = "9.2.i_can_write.txt"
    with open(filename, "w") as f:
        f.write("I can write!")

if __name__ == "__main__":
    main()