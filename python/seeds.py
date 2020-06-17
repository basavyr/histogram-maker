import randoms as rnd

data = [rnd.clhistogram(100, 0, 2)[3][0], rnd.clhistogram(100, 0, 2)[3][1]]
print(f'The seeds used for generating the random container are:')
print(f'rd: {data[0]}')
print(f'mt: {data[1]}')
