'''Module that allows JSON imports for the dataframe'''

import json

'''Module that allows calculation of distance for similarity of words (also known as Levenshtein distance) '''

import editdistance

'''Module that allows exports in a csv file format'''

import csv

'''Module that allows parsing of ISO8601 into an hour format'''

import isodate

'''Calculates the edit distance (in our case, used to find misspellings, singulars or proper forms of 'Chilies')
Threshold has been empirically chosen to fit the needs'''

def is_similar(string1, string2, threshold=2):
    current_distance = editdistance.eval(string1, string2)
    if (current_distance <= threshold):
        return True

'''Adds the 'difficulty' field for a recipe ensuring proper data format handling for times (minutes, hours)'''

def difficulty(recipe):

    '''If a time is expressed in hours and studying the dataset tells us we can make this optimization to automatically classify as Hard'''

    if("H" in recipe['cookTime'] or "H" in recipe['prepTime']):
        recipe['difficulty'] = "Hard"
        return
    
    try:

        '''Parsing the ISO8601 format of time into H:M:S and then into minutes'''

        array_cookMinutes = str(isodate.parse_duration(recipe['cookTime'])).split(":")
        array_prepMinutes = str(isodate.parse_duration(recipe['prepTime'])).split(":")
        cookMinutes = float(array_cookMinutes[0]) * 60 + float(array_cookMinutes[1]) + float(array_cookMinutes[2]) / 60
        prepMinutes = float(array_prepMinutes[0]) * 60 + float(array_prepMinutes[1]) + float(array_prepMinutes[2]) / 60
        totalMinutes = cookMinutes + prepMinutes
        if(totalMinutes > 60.0):
            recipe['difficulty'] = "Hard"
        elif(totalMinutes >= 30.0 and totalMinutes <= 60.0):
            recipe['difficulty'] = "Medium"
        elif(totalMinutes < 30.0):
            recipe['difficulty'] = "Easy"
    except ValueError:

        '''Will be classified as unknown if the format is not proper (e.g. cookTime: ""), therefore parsing is impossible'''

        recipe['difficulty'] = "Unknown"

data = []

with open('recipes.json', 'r') as file1:
    json_data = file1.readlines()

'''We correct the file we were given because the format was not proper JSON, we need an array of objects'''

with open('data_with_commas.json', 'w') as file2:
    file2.write('[')
    for i, line in enumerate(json_data):
        line = line.rstrip().rstrip(',')
        if i < len(json_data) - 1:
            file2.write(line + ',\n')
        else:
            file2.write(line + '\n')
    file2.write(']')

with open('data_with_commas.json', 'r') as file:
    data = json.load(file)

'''We filter the data finding "Chilies" or derivatives of this in the ingredients list, then we create the difficulty levels'''

filtered_data = [recipe for recipe in data if any(is_similar("Chilies", ingredient) for ingredient in recipe['ingredients'].split(" "))]
for recipe in filtered_data:
    difficulty(recipe)

with open('result-recipes.csv', "w", newline="", encoding="utf-8") as file3:
    fieldnames = ["name", "ingredients", "url", "image", "cookTime", "recipeYield", "datePublished", "prepTime", "description", "difficulty"]
    writer = csv.DictWriter(file3, fieldnames=fieldnames)
    writer.writeheader()
    for recipe in filtered_data:
        writer.writerow(recipe)