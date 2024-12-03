from bs4 import BeautifulSoup
import requests
import csv

# Fetch the webpage content
url = "" #for the equipment auction site
response = requests.get(url)
html_content = response.content

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find all equipment listings using the identified selector
equipment_listings = soup.find_all("div", class_="cat-list-card")

# Prepare the data for writing to CSV
equipment_list = []
for listing in equipment_listings:
    title_element = listing.find("h2", class_="mb-3")
    price_element = listing.find("span", class_="price")  

    equipment_data = {
        "title": title_element.text.strip() if title_element else None,
        "price": price_element.text.strip() if price_element else None,
    }
    equipment_list.append(equipment_data)

# Write the extracted equipment list to a CSV file
csv_file = "excavator_equipment_data.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price"])
    writer.writeheader()  # Write the header row
    writer.writerows(equipment_list)  # Write all equipment data


print(f"Data successfully written to {csv_file}")
