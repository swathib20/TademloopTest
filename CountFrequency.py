def CountFrequency(my_list):

    f = {}
    for item in my_list:
        if (item in f):
            f[item] += 1
        else:
            f[item] = 1

    print(f)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    CountFrequency(my_list)
