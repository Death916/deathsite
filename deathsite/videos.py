# get the newest video from the youtube channel
import os
import json
from googleapiclient.discovery import build

class Youtube:

    def __init__(self):
        # get the api key from the config file
        keys = ""


    def get_api_key(self):
        keys_path = os.path.join(os.path.dirname(__file__), "keys.json")
        with open(keys_path) as k:
            keys = json.load(k)
            return keys


    def get_newest_video(self):
            # get the newest video from the youtube channel
            keys = self.get_api_key()

#use basic auth to get newest video
            youtube = build("youtube", "v3", developerKey=keys["youtube_api_key"])
            # get the channel id
            id = keys["channel_id"]
            request = youtube.search().list(
                part="snippet",
                channelId=id,
                order="date",
                maxResults=1,
                type="video"
            )
            response = request.execute()
            items = response.get("items", [])
            if items:
                video_id = items[0]["id"]["videoId"]
                self.current_yt_video = f"https://www.youtube.com/watch?v={video_id}"
            else:
                self.current_yt_video = ""

    def get_current_yt_video(self):
        # get the current youtube video
        self.get_newest_video()
        return self.current_yt_video

    def get_last_5_yt_videos(self):
        # get the last 5 videos from the youtube channel
        keys = self.get_api_key()
        youtube = build("youtube", "v3", developerKey=keys["youtube_api_key"])
        id = keys["channel_id"]
        request = youtube.search().list(
            part="snippet",
            channelId=id,
            order="date",
            maxResults=5,
            type="video"
        )
        response = request.execute()
        items = response.get("items", [])
        videos = []
        for item in items:
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append(video_url)
        return videos

if __name__ == "__main__":
    yt = Youtube()
    yt.get_current_yt_video()
    print(yt.current_yt_video)
