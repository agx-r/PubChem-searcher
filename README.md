# PubChem-searcher

This Python module provides a convenient interface for retrieving compound connections and information from the PubChem site using the PubChem API. It allows users to search for compounds by name and retrieve detailed compound information in JSON format.

## Features

- Search for compounds by name: The module includes a function `search_compounds(query)` that takes a compound name as input and returns a list of compound IDs (CIDs) matching the search query.
- Get compound information: The module includes a function `get_compound_info(cid)` that takes a compound ID (CID) as input and retrieves detailed information about the compound, including its name, description, and other properties.
- JSON format: The module communicates with the PubChem API and retrieves data in JSON format, making it easy to parse and process the returned information.

## Usage

1. Import the `PubChemSearcher` module into your Python script or interactive session.
2. Use the `search_compounds(query)` function to search for compounds. Pass the compound name as the `query` parameter, and the function will return a list of compound IDs (CIDs) matching the search query.
3. Iterate over the CIDs returned from the search and use the `get_compound_info(cid)` function to retrieve detailed information about each compound. Pass the compound ID as the `cid` parameter, and the function will return a dictionary containing compound information in JSON format.
4. Process the compound information as needed for your application.

Example usage:

```python
import PubChemSearcher as pubchem_api

# Search for explosive compounds
query = input()
cids = pubchem_api.search_compounds(query)

# Retrieve detailed information for each compound
for cid in cids:
    compound_info = pubchem_api.get_compound_info(cid)
    print(f"Compound ID: {cid}")
    print(f"Name: {compound_info['id']['name']}")
    print(f"Description: {compound_info['props'][0]['urn']['label']}")
    print()
```

## Requirements

- Python 3.x
- `requests` library: Make sure to install the `requests` library using `pip install requests` before using this module.

## Contributions

Contributions to this module are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please open an issue or submit a pull request on the [GitHub repository](https://github.com/Aganow/PubChem-searcher).

We hope this module simplifies the process of retrieving compound connections and information from the PubChem API in your Python projects. Enjoy exploring the world of chemical compounds with ease!
