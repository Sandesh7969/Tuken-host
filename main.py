import os
try:
    import discord
    import asyncio
    import json
    import random
    import time
    import colorama
    from colorama import Fore, Style

except ModuleNotFoundError:
    os.system('pip install discord==1.7.3')
    os.system('pip install discord.py==1.7.3')
    os.system('pip install asyncio')
    os.system('pip install colorama')
    os.system('pip install fore')

colorama.init()

with open('tokens.txt', 'r') as f:
    tokens = [line.strip() for line in f.readlines()]
print(Fore.WHITE + '[+] Loading...' + Style.RESET_ALL)
time.sleep(3)
print(Fore.YELLOW + f'[!] Loaded {len(tokens)} token(s)' + Style.RESET_ALL)

bots = []
for token in tokens:
    Activities = random.choice(['Minecraft', 'Grand Theft Auto V', 'Visual Studio Code', 'Code', 'Roblox', 'YouTube', 'Lunar Client', 'Github', 'Feather', 'League of Legends', 'Discord', 'Among Us', 'Valorant', 'Google Chrome', 'Rocket League', 'Netflix', 'Fortnite', 'Twitch', 'Apex Legends', 'Overwatch', 'Steam', 'Microsoft Word', 'Call of Duty: Warzone', 'Zoom', 'The Witcher 3: Wild Hunt'])
    Statuses = random.choice(['dnd', 'idle', 'online'])
    bot = discord.Client(intents=discord.Intents.default(), activity=discord.Game(name=Activities), status=Statuses)
    bots.append((bot, token))

async def start_bot(data):
    bot, token = data
    await bot.login(token, bot=False)
    await bot.connect()
    await bot.wait_until_ready()
print(Fore.GREEN + '[+] Hosted Successfully' + Style.RESET_ALL)
time.sleep(1)
print(Fore.RED + '[!] Note: You are not allowed to republish without permissions' + Style.RESET_ALL)

async def main():
    while True:
        tasks = [asyncio.create_task(start_bot(data)) for data in bots]
        await asyncio.gather(*tasks)
        await asyncio.sleep(60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Fore.RED + "[-] Exiting..." + Style.RESET_ALL)
