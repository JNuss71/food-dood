from nutritionix import Nutritionix
from logos import getlogo
# Application ID:
appid = 'ffb27ccd'
# API Key:
apikey = '516561556bb62da642a4824b86084d02'


nix = Nutritionix(app_id=appid, api_key=apikey)


def search_calls(searchTerm):
    itemID=None
    pizza2 = nix.search(searchTerm)  # , results="0:1")
    json = pizza2.json()

    for dics in json['hits']:
        if searchTerm in dics['fields']['item_name']:
            itemID = dics['fields']['item_id']
            break
    if not bool(itemID):
        itemID = str(json['hits'][0]['fields']['item_id'])

    itemJSON = nix.item(id=itemID).json()
    calories = itemJSON['nf_calories']
    grams = itemJSON['nf_serving_weight_grams']
    serving_quant = itemJSON['nf_serving_size_qty']
    serving_units = itemJSON['nf_serving_size_unit']
    serving = str(serving_quant) + " " + serving_units
    calories_per_serving = str(calories) + " calories per " + serving
    return searchTerm, calories_per_serving, calories, serving_units

if __name__ == '__main__':
    file_name = "cheetos.png"
    output=str(getlogo(file_name))