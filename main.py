
import time
import random
from youtube import YouTubeClient
from comment_generator import generate_comment
from dotenv import load_dotenv

load_dotenv()

def main():
    yt = YouTubeClient()
    print("Bot uruchomiony. Czekam na nowe filmy...")

    while True:
        latest_video_id = yt.get_latest_video_id()
        if not yt.has_already_commented(latest_video_id):
            comment = generate_comment(latest_video_id)
            yt.post_comment(latest_video_id, comment)
            print(f"Skomentowano film {latest_video_id}: {comment}")
        else:
            print("Brak nowych filmów.")

        wait_time = random.randint(1200, 5400)
        print(f"Czekam {wait_time} sekund...")
        time.sleep(wait_time)

if __name__ == "__main__":
    main()
