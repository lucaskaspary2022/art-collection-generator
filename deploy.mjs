import create from 'ipfs-http-client'

const image = './ImprovedPlanets/6.png'
const ipfsClient = create("http://ipfs.infura.io:5001/api/v0")
const addedImage = ipfsClient.add(image)
const metadata = {
    "name": "Planet #6", 
    "image": "https://ipfs.io/ipfs/QmW4qFjMzhvC6FRkFJ95wnpQHc1T6qQoTZLmQJVVV5gBB1/6.png", 
    "description": "Not even just 0.0000000000000001 percent of our universe", 
    "attributes": [
        {"trait_type": "Galaxy", "value": "Galaxy 1000"}, 
        {"trait_type": "Color", "value": "Turquoise Color"}, 
        {"trait_type": "Size (Radius)", "value": "6,799,379 km"}, 
        {"trait_type": "Surface", "value": "Stripes"}
    ]
}
const addedMetadata = ipfsClient.add(metadata)