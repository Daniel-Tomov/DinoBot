import feedparser
from datetime import datetime, timedelta
from discord.ext import tasks
import asyncio

URL = "https://feeds.feedburner.com/TheHackersNews"

class RSSParser:
    # Constructor
    def __init__(self, client):
        self.client = client
        self.url = URL
        self.rssSendMessage.start()

    # send RSS updates
    @tasks.loop(hours = 1)
    async def rssSendMessage(self):
        feed = feedparser.parse(self.url)
        now = datetime.now().astimezone()
        time_range = timedelta(hours = 1)

        for entry in feed.entries:
            entry_time = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z").astimezone()

            if now - entry_time <= time_range:
                discMessageString = f'Title: {entry.title}\nPublication Date: {entry.published}\nSummary: {entry.summary}'
                channel = self.client.get_channel(1208824287457321080)
                await channel.send(discMessageString)