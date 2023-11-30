from random import choices

chars = "0123456789ABCDEF"

def color_code():
    l_color = choices(chars, k=6)
    str_color = "".join(l_color)

    return str_color
def main():
    print(color_code())

if __name__ == "__main__":
        main()