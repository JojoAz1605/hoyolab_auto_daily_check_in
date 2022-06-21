import asyncio
import os

import genshin
import time

from dotenv import load_dotenv

load_dotenv()
MAIL = os.getenv("MAIL")
PASS = os.getenv("PASS")


async def main():
    print("Création du client genshin...")
    client = genshin.Client(lang="fr-fr", game=genshin.Game.HONKAI)

    print("Client créé!\nRécupération des cookies(Il est possible qu'un captcha vous soit soumis)...")
    cookies = await client.login_with_password(MAIL, PASS)
    print(f"Cookies récupérés!\n{cookies}\nTentative de récupération des récompenses...")

    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        print("\nVous avez déjà récupérées les récompenses aujourd'hui\n")
    else:
        print(f"Récompenses récupérées {reward.amount}x {reward.name}!")

    print("Le programme va se fermer dans 3 secondes, il est possible qu'une erreur s'affiche, désolé, je sais pas ce qu'elle veut dire xD")
    for i in range(3):
        time.sleep(1)


asyncio.run(main())
