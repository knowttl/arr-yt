import json
import config
from googleapiclient.discovery import build


def search_youtube_videos(query):
    youtube = build('youtube', 'v3', developerKey=config.YOUTUBE_API_KEY)
    request = youtube.search().list(part="snippet",q=query,type="video",maxResults=5,videoDefinition="high",regionCode="US")
    response = request.execute()
    return response

def get_youtube_video_localizations(search_results):
    results = []
    youtube = build('youtube', 'v3', developerKey=config.YOUTUBE_API_KEY)
    for item in search_results["items"]:
        video_details = {}
        videoId = item["id"]["videoId"]

        video_details["id"] = videoId
        video_details["title"] = item["snippet"]["title"]
        video_details["localization"] = "default"

        video_request = youtube.videos().list(part="localizations",id=videoId)
        video_response = video_request.execute()["items"][0]
        try:
            if "id" in video_response["localizations"]:
                video_details["title"] = video_response["localizations"]["id"]["title"]
                video_details["localization"] = "id"
            elif "en" in video_response["localizations"]:
                video_details["title"] = video_response["localizations"]["en"]["title"]
                video_details["localization"] = "en"
        except KeyError:
            # Failed to find specific title localization for this video search
            pass
        results.append(video_details)
    return results

def parse_youtube_videos(results):
    for item in results:
        print(item["title"])

def main():
    search_results = search_youtube_videos("legend of xianwu ep51")
    # search_results = search_youtube_videos("immortality s3 ep4")
    # search_results = search_youtube_videos("world of immortals ep4")
    results = get_youtube_video_localizations(search_results)
    # results = search_youtube_videos("immortality s3 ep4")
    parse_youtube_videos(results)

if __name__ == "__main__":
    main()
