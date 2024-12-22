options = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Adapt the task to extract and format video titles from YouTube video titles based on a search query. Ensure to never select titles containing the word \"trailer\" and present the selected title in a new format.\n\nAnalyze the list of video title data provided in json format to identify the best title match with the search query. Have a preference for videos that are listed higher in the list.\n\nIf no good match is found return the index -1 with in the result.\n\n# Steps \n\n1. **Identify the closest match**: Compare each video title against the search query, ensuring titles with the word \"trailer\" are excluded.\n2. **Extract and format the title**: Extract the relevant details in the specified format, focusing on English.\n3. **Format the Result**: Ensure the resulting title is formatted as `[YouTube] Title - S01E05 [1080p]`, using only available information.\n4. **Return Results**: Output the index of the selected title and the new formatted title.\n\n# Output Format\n\nReturn results in a JSON object containing:  \n- `index`: The zero-based index of the video title that matches the query.\n- `formatted_title`: The selected and formatted title string.\n\n```json\n{\n  \"index\": [index_of_title],\n  \"formatted_title\": \"[formatted_title]\"\n}\n```\n\n# Examples\n\n### Example 1\n\n**Input:**\n```json\n{\n    \"search_query\": \"Legend of Xianwu EP89\",\n    \"video_titles\": [\n        \"【Legend of Xianwu】EP89 | Chinese Fantasy Anime | YOUKU ANIMATION\",\n        \"【Legend of Xianwu】EP89 Trailer | Chinese Fantasy Anime | YOUKU ANIMATION\",\n        \"✨Legend of Xianwu EP 89 Preview\",\n        \"ENGSUB【仙武传 Legend of Xianwu】EP89 预告Trailer  | 超燃玄幻国漫 | 优酷动漫 YOUKU ANIMATION\",\n        \"Legend Of Xianwu Episode 89 🥰 #shorts #viralshorts #trending #donghua #anime\"\n    ]\n}\n```\n\n**Output:**\n```json\n{\n  \"index\": 0,\n  \"formatted_title\": \"[YOUKU] Legend of Xianwu - E89\"\n}\n```\n\n### Example 2\n\n**Input:**\n```json\n{\n    \"search_query\": \"Immortality S3 EP4\",\n    \"video_titles\": [\n        \"Immortality S3 EP4【Fantasy | Fighting | Fantasy | Made By Bilibili】\",\n        \"【ENGSUB】Immortality S3  EP01-16 collection【Join to watch latest】\",\n        \"Immortality S4 EP4【Fantasy | Fighting | Fantasy | Made By Bilibili】\",\n        \"Immortality Season 4 Episode 04 Preview (Eng Sub)\",\n        \"MENYERAP PIL RAKSASA STAR DOU #immortality  SEASON 3 EPISODE 4 -5\"\n    ]\n}\n```\n**Output:**\n```json\n{\n  \"index\": 0,\n  \"formatted_title\": \"[Bilibili] Immortality - S3E4\"\n}\n```\n\n### Example 3\n\n**Input:**\n```json\n{\n    \"search_query\": \"World of Immortals EP7\",\n    \"video_titles\": [\n        \"✨World of Immortals EP 07 [MULTI SUB]\",\n        \"ENG SUB | \\\"World of Immortals\\\" EP07 | Ancestral Dragon | Tencent Video-ANIMATION\",\n        \"ENG SUB | World of Immortals  [EP7 Part1] english sub\",\n        \"✨World of Immortals EP 07 CLIP 8minutes [MULTI SUB]\",\n        \"ENG SUB | World of Immortals  [EP7 Part2] english sub\"\n    ]\n}\n```\n\n**Output:**\n```json\n{\n  \"index\": 1,\n  \"formatted_title\": \"[Tencent] World of Immortals - E7\"\n}\n```\n\n### Example 4\n\n**Input:**\n```json\n{\n    \"search_query\": \"Legend of Xianwu EP52\",\n    \"video_titles\": [\n        \"【Legend of Xianwu】EP52 | Chinese Fantasy Anime | YOUKU ANIMATION\",\n        \"Legend of Xianwu ep52 | Ye chen used devil heart power to save shangguan sisters #shorts #donghua\",\n        \"【Legend of Xianwu】EP51-65 FULL | Chinese Fantasy Anime | YOUKU ANIMATION\",\n        \"【仙武传 Legend of Xianwu】EP52 | 精彩看点Highlight | 超燃玄幻国漫 | 优酷动漫 YOUKU ANIMATION\",\n        \"【Legend of Xianwu】EP53 | Chinese Fantasy Anime | YOUKU ANIMATION\"\n    ]\n}\n```\n\n**Output:**\n```json\n{\"index\":0,\"formatted_title\":\"[YouTube] Legend of Xianwu - E52\"}\n```\n### Example 5\n\n**Input:**\n```json\n{\n    \"search_query\": \"Stellar Transformation EP 10\",\n    \"video_titles\": [\n        \"🌟ENG SUB | Stellar Transformations EP 10 | Yuewen Animation\",\n        \"【官方Official】| Stellar Transformations EP10 | Qinglian Mountains | YUEWEN ANIMATION\",\n        \"stellar transformation s5 ep 10 eng sub full episode/#stellartransformation\",\n        \"星辰变第10集，开天辟地！Stellar Transformation Episode 10, Heaven Separated From Earth.\",\n        \"Stellar Transformation [Xing Chen Bian] Season 4 Episode 10 Preview\"\n    ]\n}\n```\n\n**Output:**\n```json\n{\"index\":1,\"formatted_title\":\"[YouTube] Stellar Transformations - E10\"}\n```\n# Notes\n\n- Video titles with popular platforms like Youku, Tencent, Bilibili, Yuewen, and WeTV should be prioritized.\n- The format `[Source] Title - S01E05 [1080p]` includes only the segments present.\n- Omit unavailable segments, leaving just `[Source] Title - Episode`."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "{\"search_query\": \"Legend of Xianwu EP13\", \"video_titles\": [\"【Legend of Xianwu】EP13 | Chinese Fantasy Anime | YOUKU ANIMATION\", \"ENGSUB【仙武传 Legend of Xianwu】EP13预告 | 天价竞拍 群雄混战 | 超燃玄幻国漫 | 优酷动漫 YOUKU ANIMATION\", \"Bisakah hubungan Ye Chen menghidupkan kembali cinta masa lalu!\", \"【Legend of Xianwu】EP13-14! Ye Chen angered two beauties!\", \"Xianwu] Legend of Xianwu EP13 trailer [Xianwu Emperor] Episode13\"]}"
                    }
      ]
    },
    {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "{\"index\":0,\"formatted_title\":\"[YouTube] Legend of Xianwu - E13\"}"
                    }
                ]
            }

    ],
        "response_format":{
                "type": "json_schema",
                "json_schema": {
                    "name": "video_metadata",
                    "schema": {
                        "type": "object",
                        "required": [
                            "index",
                            "formatted_title"
                            ],
                        "properties": {
                            "index": {
                                "type": "number",
                                "description": "The index of the video in a list."
                                },
                            "formatted_title": {
                                "type": "string",
                                "description": "The formatted title of the video."
                                }
                            },
                        "additionalProperties": False
                        },
                    "strict": True
                    }
                },
  "temperature": 1,
  "max_completion_tokens": 2048,
  "top_p": 1,
  "frequency_penalty":0,
  "presence_penalty": 0
}
