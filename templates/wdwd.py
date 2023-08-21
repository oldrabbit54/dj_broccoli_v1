d = {'one': 1, 'two': 2, 'natural': 1, 'True': 1, 'even': 2, 'three': 3, 'False': 0}  # этот словарь не менять
d_unique = {{j:i for i, j in d.items()}[i] : i for i in set({j:i for i, j in d.items()})}


# здесь продолжайте программу




