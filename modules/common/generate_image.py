import requests
from modules.common.word_dictionary import word_dictionary

def fetch_image_from_wikipedia(word: str):
    base_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={word}&prop=pageimages&format=json&pithumbsize=500"
    response = requests.get(base_url)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        page_id = next(iter(data['query']['pages']))
        page_data = data['query']['pages'][page_id]
        if 'thumbnail' in page_data:
            # Get the image URL
            image_url = page_data['thumbnail']['source']
            return image_url
        else:
            return "No image found"
    else:
        return "Error fetching data from Wikipedia"


# word = "x-ray"  # This can be replaced with any word dynamically
# image_url = fetch_image_from_wikipedia(word)
# print(image_url)


for i in word_dictionary:
    for j in word_dictionary[i]:
        print(j['english_word'])
        image_url = fetch_image_from_wikipedia(j['english_word'])
        print(image_url)
        print("\n")
