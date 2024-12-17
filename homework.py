import requests
from bs4 import BeautifulSoup
import discord

# Replace with your Discord bot token and webhook URLs
bot_token = 'MTMxODM3MDk1MDE3MzAzMjUwMQ.Gt7L69.sKdNdn6oqYVm_K-KdQ7l_mrxONixoPTqF1gjPsn'
homework_webhook_url = 'https://discord.com/api/webhooks/1318358536261992530/XlT3IzvrVthRB5jqYsZxSVQfPBzEV9M93LWp3D_kQqe7CzNgM-Yj8uGwLUOTue7x7sGQ'
notices_webhook_url = 'https://discord.com/api/webhooks/1318367896618930177/FBZmNwGj6caC8IQIP0phuANHU_Zc0duFZKltrCOucIU09-uvJds3PQNJIfMz29ivHS2g'

def fetch_homework(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP statuses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Adjust the selector to match the specific HTML element containing homework
        homework_text = soup.select_one('.homework-text').text

        return homework_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching homework: {e}")
        return None

def send_to_discord(webhook_url, homework_text):
    try:
        webhook = discord.Webhook.from_url(webhook_url)
        webhook.send(homework_text)
        print("Homework posted to Discord!")
    except discord.errors.HTTPException as e:
        print(f"Error posting to Discord: {e}")

if __name__ == '__main__':
    homework_url = 'https://beaconlightacademy.edu.pk/app/diary?tab=classwork'
    notices_url = 'https://beaconlightacademy.edu.pk/app/diary?tab=notices'

    homework_text = fetch_homework(homework_url)
    notices_text = fetch_homework(notices_url)

    if homework_text:
        send_to_discord(homework_webhook_url, homework_text)

    if notices_text:
        send_to_discord(notices_webhook_url, notices_text)
