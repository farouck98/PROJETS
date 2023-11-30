
def get_from_list(l: list, index:int):
    try:
        value = l[index]
        return value
    except IndexError:
        return None

if __name__=="__main__":
    l = [1, 2, 3, 4]
print(get_from_list(l, 4))