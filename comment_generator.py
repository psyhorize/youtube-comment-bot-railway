
import random

templates = [
    "Ale to dobrze brzmi",
    "Świetna energia",
    "Klimat nie do podrobienia",
    "Mega vibe",
    "Zostaje w głowie",
    "Czuć emocje w tym kawałku",
    "Naprawdę piękne",
    "Super brzmienie",
    "Uwielbiam takie klimaty",
    "Znakomita robota"
]

emojis = ["🎧", "🔥", "🌌", "❤️", "🙌", "🎶", "💫", "✨", "🖤", "🎵"]

def generate_comment(video_title):
    comment = random.choice(templates)
    emoji = random.choice(emojis)
    return f"{comment} {emoji}"
