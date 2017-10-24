import json
import os
import shutil


def clean_json(stringname):
    """

    :rtype: file_name
    """
    with open(stringname) as data_file:
        data = json.load(data_file)
    for element in data:
        if 'categories' in element:
            for x in (range(len(element['categories']))):
                if 'href' in element['categories'][x]:
                    del element['categories'][x]['href']
        if 'href' in element['faction']:
            del element['faction']['href']
        if 'href' in element['group']:
            del element['group']['href']
        if 'href' in element:
            del element['href']
        for x in (range(len(data[0]['variations']))):
            if 'href' in element['variations'][x]:
                del element['variations'][x]['href']
        for x in range(len(element['variations'])):
            if 'href' in element['variations'][x]['rarity']:
                del element['variations'][x]['rarity']['href']
    with open(stringname, 'w') as file:
        file.write(json.dumps(data))


def delete(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    elif os.path.isdir(filename):
        shutil.rmtree(filename)
    else:
        raise ValueError('File or Directory %s Does Not Exist', (str(filename)))
