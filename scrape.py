import requests
import json

domain = 'https://ideal-sport.ro'
c = 1
for page in range(1, 999):
    r = requests.get(f'{domain}/collections.json?limit=250&page={page}', headers={})

    if r.status_code == 200:
        j = json.loads(r.text)
        if len(j['collections']) > 0:
            for collection in j['collections']:
                print(f'{str(c).ljust(4)} - {str(collection["products_count"]).ljust(4)} - {collection["title"].ljust(50)} - {domain}/collections/{collection["handle"]}')
                c += 1
        else:
            exit()
    else:
        print(f'Status code {r.status_code}, exiting...')
        exit()