import requests
from bs4 import BeautifulSoup

def read_urls(file_path):
    """Read URLs from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file]
    return urls

def fetch_and_write_content(urls, output_file_path):
    """Fetch content from each URL and write to a file."""
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Select elements with the class "entry"
                entries = soup.select(".entry-permalink")
                for entry in entries:
                    
                    
                    # Extract and write all hyperlinks within the entry
                    links = entry.find_all('a', href=True)
                    if links:
                        for link in links:
                            file.write(f"{link['href']}\n")
            else:
                print(f"Failed to retrieve the page at {url}. Status code: {response.status_code}")

# Define the input and output file paths
urls_file_path = 'siderealinksall.txt'
output_file_path = 'sidereapermalinksall.txt'

# Read URLs from the file
urls = read_urls(urls_file_path)

# Fetch content from each URL and write to a new file
fetch_and_write_content(urls, output_file_path)
