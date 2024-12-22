import json
import config
import openai_config
from googleapiclient.discovery import build
from openai import OpenAI

def get_openai_response(user_input):
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    new_user_input = {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_input
                    }
                ]
            }
    openai_config.options["messages"].append(new_user_input)
    response = client.chat.completions.create(**openai_config.options)
    return response

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

def format_youtube_videos_json(search_query, videos):
    result = {}
    result["search_query"] = search_query
    video_titles = []
    for item in videos:
        video_titles.append(item["title"])
    result["video_titles"] = video_titles
    return result

def main():
    # search_string = "Legend of Xianwu EP89"
    # search_string = "Immortality S3 EP4"
    # search_string = "World of Immortals EP7"
    # search_string = "Legend of Xianwu EP52"
    search_string = "Stellar Transformation EP 18"
    search_results = search_youtube_videos(search_string)
    # search_results = search_youtube_videos("immortality s3 ep4")
    # search_results = search_youtube_videos("world of immortals ep4")
    video_results = get_youtube_video_localizations(search_results)
    # results = search_youtube_videos("immortality s3 ep4")
    result = format_youtube_videos_json(search_string, video_results)
    print(json.dumps(result, indent=4, ensure_ascii=False))
    print(get_openai_response(json.dumps(result, indent=4, ensure_ascii=False)))

if __name__ == "__main__":
    main()
