import aiohttp
from bs4 import BeautifulSoup
import zipfile
from typing import List, Tuple, Dict
import logging
import requests


r = requests.get('https://www.scrapethissite.com/pages/forms/')

def scrape_hockey_data() -> Tuple[List[str], List[Dict[str, str]]]:
    html_files = []
    hockey_stats = []

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    table_rows = soup.find_all("tr")

    for row in table_rows:
        cols = row.find_all("td")
        if len(cols) >= 4:  # Ensure enough columns exist
            hockey_stats.append({
                "year": cols[0].text.strip(),
                "team": cols[1].text.strip(),
                "wins": int(cols[2].text.strip() or 0),
                "losses": int(cols[3].text.strip() or 0),
            })

    print(f"Total records scraped: {len(hockey_stats)}")
    return html_files, hockey_stats

def save_html_files(html_files: List[str], output_path: str):
    with zipfile.ZipFile(output_path, "w") as zf:
        for idx, content in enumerate(html_files, 1):
            zf.writestr(f"{idx}.html", content)
