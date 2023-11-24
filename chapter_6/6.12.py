
def read_from_index(l: dict, k, default_value=None):
    if k in l:
      return l[k]
    else:
        return default_value
print(read_from_index({"sith":"Dark Vendor", "farouck": 25},
                      "c"))
