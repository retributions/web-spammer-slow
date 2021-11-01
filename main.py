from discord_webhook import DiscordWebhook

lol=["webhook link"]

webav = ("Image link")

webhook = DiscordWebhook(url=lol,content="Spammed", username="spammed", avatar_url=(webav))

while True:
 response = webhook.execute()
