import pandas as pd
import os
import requests
import re
from urllib.parse import quote
from datetime import datetime

"""
Update README.md with the 20 most recent listings.

1. Format the listings by adjusting the 'Location' and encoding the URLs to handle special characters (see issue #1)
2. Update the README.md
"""

df = pd.read_csv('check_these.csv')
df['Published Date'] = pd.to_datetime(df['Published Date'])
df = df.sort_values(by='Published Date', ascending=False)

recent_listings = df.head(20)
recent_listings = recent_listings[['Rent (€)', 'Size (m²)', 'Rooms', 'Location', 'Link', 'Published Date']]

recent_listings['Location'] = recent_listings['Location'].apply(
    lambda x: f"{str(x).split(',')[1].split('.')[0]}. {str(x).split(',')[-1].strip()}" if isinstance(x, str) else "Unknown"
)

recent_listings['Link'] = recent_listings['Link'].apply(lambda x: quote(x, safe='/:?=&%'))

current_listings = recent_listings.rename(columns={
    'Rent (€)': '💰 Rent (€)',
    'Size (m²)': '📏 Size (m²)',
    'Rooms': '🛏️ Rooms',
    'Location': '🏙️ District',
    'Published Date': '📅 Published Date'  # Add the calendar emoji to the header
})

current_listings['Link'] = current_listings['Link'].apply(lambda x: f'[🔗]({x})')
current_listings['📅 Published Date'] = recent_listings['Published Date'].dt.strftime('%b %d, %H:%M')

try:
    with open('README.md', 'r') as readme_file:
        readme_contents = readme_file.read()
    old_links = re.findall(r'\[🔗\]\((.*?)\)', readme_contents)
except FileNotFoundError:
    old_links = []

markdown_table = current_listings[['💰 Rent (€)', '📏 Size (m²)', '🛏️ Rooms', '🏙️ District', 'Link', '📅 Published Date']].to_markdown(index=False)

with open('README.md', 'r') as readme_file:
    readme_contents = readme_file.read()

start_marker = "## Recent Active Listings\n"
if start_marker in readme_contents:
    before_table = readme_contents.split(start_marker)[0] + start_marker
else:
    before_table = readme_contents + "\n" + start_marker

with open('README.md', 'w') as readme_file:
    readme_file.write(before_table + "\n" + markdown_table + "\n")

"""
Send new listings to Telegram channel.

1. Identify 'new listings' by finding links that are in the new markdown but not in the old markdown.
2. Extract the 'old listings' from the previous markdown (those that are no longer in the top 20).
3. Find the most recent 'Published Date' from the 'old listings'.
4. Filter the 'new listings' to include only those more recent than the most recent 'old listing'. - because really nice deals have short lifespans
5. Sort the filtered listings by 'Published Date' in ascending order and send these to the Telegram channel.
"""

current_links = recent_listings['Link'].tolist()

new_links = [link for link in current_links if link not in old_links]

old_listings = recent_listings[recent_listings['Link'].isin(old_links)]

if not old_listings.empty:
    max_old_published_date = old_listings['Published Date'].max()
else:
    # Use a very old timestamp with the same timezone awareness
    max_old_published_date = pd.Timestamp('1900-01-01').tz_localize('UTC')

new_listings = recent_listings[
    (recent_listings['Link'].isin(new_links)) & 
    (recent_listings['Published Date'] > max_old_published_date)
]

new_listings = new_listings.sort_values(by='Published Date', ascending=True)

api_token = os.getenv('BOT_API_KEY')
channel_id = os.getenv('CHANNEL_ID')

if not api_token or not channel_id:
    print("ERROR: API token or channel ID not found!")
    exit()

telegram_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

for _, row in new_listings.iterrows():
    formatted_date = row['Published Date'].strftime('%b %d, %H:%M')
    message = (
        f"🗓 <b>Published</b>: {formatted_date}\n\n"
        f"🏙 <b>District</b>: {row['Location']}\n"
        f"💰 <b>Rent</b>: {row['Rent (€)']} €\n"
        f"📏 <b>Size</b>: {row['Size (m²)']} m²\n"
        f"🛏 <b>Rooms</b>: {row['Rooms']} rooms\n"
        f"<a href='{row['Link']}'>🔗 Link</a>"
    )
    message_data = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        response = requests.post(telegram_url, data=message_data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send message for listing: {row['Link']}. Error: {e}")