import json

tokens = []

for i in range(1,51):
    file = open(f'./Metadata/planet{i}.json')
    data = json.load(file)
    # print(f"({i}): {data['attributes'][1]['value']}\n")

    color = data['attributes'][1]['value']
    surface = data['attributes'][2]['value']

    token = [color, surface]

    for j, item in enumerate(tokens):
        if token == item:
            print(f"Token already exists: ({i}) {token} == ({j + 1}) {item}")
            break

    # if token in tokens:
    #     print(f'Token already exists: ({i}) {token}')
    #     break

    tokens.append(token)

    file.close()