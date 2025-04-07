import os
import requests
import shelve
from bs4 import BeautifulSoup as bs

cache = shelve.open("page_cache.db")


def fetch_page(url):
    if url not in cache:
        print(f"Fetching {url}...")
        response_text = requests.get(url).text
        cache[url] = response_text
    return cache[url]


def extract_file_urls(base_url):
    response = requests.get(base_url)
    response.raise_for_status()

    soup = bs(response.text, "html.parser")
    links = soup.find_all("a")

    file_urls = [
        base_url + link.get("href")
        for link in links
        if link.get("href")
        and not link.get("href").startswith("?")
        and not link.get("href").startswith("/")
    ]

    return file_urls


base_url = "https://natura.di.uminho.pt/~jj/bs4/folha8-2023/"
file_urls = extract_file_urls(base_url)

output_folder = "output_files"
os.makedirs(output_folder, exist_ok=True)

for file_url in file_urls:
    page_content = fetch_page(file_url)
    soup = bs(page_content, "html.parser")

    title_meta = soup.find("meta", property="og:title")
    title = (
        title_meta["content"].strip()
        if title_meta and "content" in title_meta.attrs
        else "No Title"
    )

    description_meta = soup.find("meta", property="og:description")
    description = (
        description_meta["content"].strip()
        if description_meta and "content" in description_meta.attrs
        else "No Description"
    )

    article = soup.find("article")
    article_content = article.get_text("\n").strip() if article else "No Article Found"

    filename = os.path.join(
        output_folder,
        file_url.replace("http://", "").replace("https://", "").replace("/", "_")
        + ".txt",
    )
    print(title)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Description: {description}\n\n")
        file.write("Article Content:\n")
        file.write(article_content)

cache.close()
