
import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class YouTubeClient:
    def __init__(self):
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        self.api_service_name = "youtube"
        self.api_version = "v3"

        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                self.credentials = pickle.load(token)
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_config({
                "installed": {
                    "client_id": os.getenv("CLIENT_ID"),
                    "client_secret": os.getenv("CLIENT_SECRET"),
                    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token"
                }
            }, scopes)
            self.credentials = flow.run_local_server(port=8080)
            with open("token.pickle", "wb") as token:
                pickle.dump(self.credentials, token)

        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, credentials=self.credentials)

        self.commented_videos = set()

    def get_latest_video_id(self):
        request = self.youtube.search().list(
            part="snippet",
            channelId=os.getenv("CHANNEL_ID"),
            order="date",
            maxResults=1
        )
        response = request.execute()
        return response["items"][0]["id"]["videoId"]

    def has_already_commented(self, video_id):
        return video_id in self.commented_videos

    def post_comment(self, video_id, comment_text):
        request = self.youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                    "videoId": video_id,
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": comment_text
                        }
                    }
                }
            }
        )
        request.execute()
        self.commented_videos.add(video_id)
