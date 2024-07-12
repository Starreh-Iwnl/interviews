l = ["a", "b", ["c", "d", ["e", "f"]], "g", ["h"]]

d = {
    0: "a",
    1: "b",
    2: {
        0: "c",
        1: "d",
        2: {
            0: "e",
            1: "f"
        }
    },
    3: "g",
    4: {
        0: "h"
    }
}

def list_to_dict(l1):

    d1 = {}

    for idx, ele in enumerate(l1):
        
        if type(ele) == list:
            d1[idx] = list_to_dict(ele)
        else:
            d1[idx] = ele
    
    return d1

l1 = ["a", "b", ["c", "d", ["e", "f"]], "g", ["h"]]
d1 = list_to_dict(l1)

print(d1)
