import json

from black import token

baseURI = 'https://ipfs.io/ipfs/QmSbPDkJsxjmLsf4Ec6YfsVeKjF1AC8W21c4MxQLV1XSWR/'

for i in range(2, 335):
    with open(f'./Metadata/{i}.json', 'r') as file:
        data = json.load(file)
        tokenURI = baseURI + f'{i}.png'        
        data["image"] = tokenURI

    with open(f'./Metadata/{i}.json', 'w') as newFile:
        json.dump(data, newFile)
    # print(f"{data}\n")