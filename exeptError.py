result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ValueError:
        print("ValueError: a < b")
    except IndexError:
        print("IndexError: b > 100")
    except Exception as e:
        print("Exception:", type(e).__name__)
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)
