import requests
import discord
from discord import Webhook

webhook = discord.SyncWebhook.partial(1339385478553800704, 'AgWcJ--FjDu48PZgF3wr40-Fr_yxXMgLWlg-da8lc5aYJ-Z6u1VXuHflVBIYDnsvt4Fl')
webhook.send('Hello World', username='CaptainHook')
