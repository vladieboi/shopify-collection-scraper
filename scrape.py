import requests
import argparse
import json
import csv
import re

# Argument parsing
def parseArguments():
	parser = argparse.ArgumentParser(description='Scrape a Shopify website and save the output to a file')
	parser.add_argument('--domain', help='specify domain to be scraped')
	parser.add_argument('--output', help='specify output file format', choices=['csv'], default='csv')
	arguments = parser.parse_args()
	return arguments
args = parseArguments()

# Check if domain is set
if args.domain == False:
	# Show error message and exit if domain is not set
	print('You must specify a domain to be scraped using "--domain" argument!')
	exit()
else:
	if args.output == 'csv':
		# Write header to "output.csv" if "--output" argument is set to "csv"
		header = ['ID', 'Title', 'Handle', 'Published At', 'Updated At', 'Image', 'Products Count', 'URL']
		with open('output.csv', 'w') as file:
			writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)
			writer.writerow(header)

	# Strip text for "https://" & "http://" & "www." if domain is set
	strippedDomain = re.sub(r'https://|http://|www.', '', args.domain)
	url = f'https://{strippedDomain}/collections.json?limit=250&page='
	
	collectionCount = 1
	# For each page, scrape response
	for pageNumber in range(1, 9999):
		r = requests.get(f'{url}{pageNumber}', headers={})

		# If request successful
		if r.status_code == 200:
			j = json.loads(r.text)
			collectionsOnPage = j['collections']
			# Continue if more than 0 collections on page
			if len(collectionsOnPage) > 0:
				print(f'Page {pageNumber} request status code {r.status_code}, scraping {str(len(collectionsOnPage)).ljust(3)} collections...')
				for collection in j['collections']:
					# Set collection variables
					collectionId = collection['id']
					collectionTitle = collection['title']
					collectionHandle = collection['handle']
					collectionDescription = collection['description'] # This does not get written to output file as it often contains line breaks
					collectionPublishedAt = collection['published_at']
					collectionUpdatedAt = collection['updated_at']
					collectionImage = collection['image']
					collectionProductsCount = collection['products_count']
					collectionUrl = f'https://{strippedDomain}/collections/{collectionHandle}'
					collectionCount += 1

					# Write collection data to output file
					if args.output == 'csv':
						csvData = [collectionId, collectionTitle, collectionHandle, collectionPublishedAt, collectionUpdatedAt, collectionImage, collectionProductsCount, collectionUrl]
						with open('output.csv', 'a') as file:
							writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)
							writer.writerow(csvData)

			# Show error message and exit if 0 collections on page
			else:
				print('Ran out of collections to scrape - saving output to file...')
				exit()

		# If request not successful
		else:
			print(f'Page {pageNumber} request status code {r.status_code}, skipping...')