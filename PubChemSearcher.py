import requests

def search_compounds(query):
	base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
	url = f"{base_url}/compound/name/{query}/cids/JSON"

	response = requests.get(url)
	response.raise_for_status()

	data = response.json()
	cids = data["IdentifierList"]["CID"]

	return cids

def get_compound_info(cid):
	base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
	url = f"{base_url}/compound/cid/{cid}/JSON"

	response = requests.get(url)
	response.raise_for_status()

	data = response.json()
	compound_info = data["PC_Compounds"][0]

	return compound_info
