def convert():
    value = "This is a text"
    try:
        return(float(value))
    except ValueError:
        print("An error occured")

if __name__ == "__main__":
    convert()