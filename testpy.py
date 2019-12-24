print("abcdegs")


for i in range(10):
    print(i)
    try:
        if i > 5:
            print("here")
            if i == 7:
                print("hereio")
                continue
    except ValueError:
        pass
    print("er")