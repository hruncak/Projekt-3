"""
projekt_3.py: třetí projekt

author: Filip Hruncak
email: fhruncak@gmail.com
discord: Nemam
"""

import sys
import requests 
from bs4 import BeautifulSoup
import pandas as pd

def scrape_election_results(url, output_file):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Unable to access {url}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = []
    
    df = pd.DataFrame(data, columns=[
        'kód obce', 'název obce', 'voliči v seznamu', 
        'vydané obálky', 'platné hlasy', 'strany...'
    ])

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python projekt_4.py <url> <output_file>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]
    scrape_election_results(url, output_file)
