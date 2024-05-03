import webbrowser
import random
from pytube import Search

def get_random_video():
    print("Playing music...")
    video_urls = Search('Most Popular Hindi Songs')
    video_urls = video_urls.results
    random_url = random.choice(video_urls)
    # print(random_url.video_id)
    return random_url.video_id

def play_random_music():
    random_video_url = get_random_video()
    
    webbrowser.open(f"https://www.youtube.com/watch?v={random_video_url}")

if __name__ == "__main__":
    play_random_music()
