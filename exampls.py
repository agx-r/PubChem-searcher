import json
from pprint import pprint
import PubChemSearcher as pcs

def print_dict(dictionary):
	for key, value in dictionary.items():
		print(f"{key}: {value}".replace('_',' '))

def search_compounds(query):
	cids = pcs.search_compounds(query)
	for cid in cids:
		compound_info = pcs.get_compound_info(cid)
		print(f"Compound ID: {cid}")
		print(f"Description: {compound_info['props'][0]['urn']['label']}")
		print_dict(compound_info['count'])
		#pprint(compound_info)
		print()

if __name__ == "__main__":
	while True:
		search_compounds(input())