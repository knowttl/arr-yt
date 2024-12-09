from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Receive a JSON input containing YouTube video titles and a search query, and match the most relevant video title. Return the index and formatted version of the matched title.\n\nAnalyze a list of YouTube video titles in various languages, primarily focusing on English. Determine which title best matches a given search query.\n\n# Input Format\n\nThe input should be a JSON object containing:\n- `video_titles`: An array of YouTube video titles.\n- `search_query`: A string representing the search query.\n\nExample JSON input:\n```json\n{\n  \"video_titles\": [\"video title 1\", \"video title 2\", ...],\n  \"search_query\": \"search term\"\n}\n```\n\n# Steps\n\n1. **Identify the closest match**: Compare each video title against the search query and determine which one matches best using text similarity metrics.\n2. **Extract and format the title**: From the selected video title, extract and format the relevant English title details in the specified pattern.\n3. **Format the Result**: Ensure the resulting title is in the format `[YouTube] Title - S01E05 [1080p]`, including only the available information.\n4. **Return Results**: Output the index of the matched title and the formatted version.\n\n# Output Format\n\nReturn results in a JSON object containing:\n- `index`: The zero-based index of the video title that matches the query.\n- `formatted_title`: The selected and formatted title string.\n\nExample JSON output:\n```json\n{\n  \"index\": [index_of_title],\n  \"formatted_title\": \"[formatted_title]\"\n}\n```\n\n# Examples\n\n### Example 1\n\n**Input:**\n```json\n{\n  \"video_titles\": [\"【Legend of Xianwu】EP89 | Chinese Fantasy Anime | YOUKU ANIMATION\",\n                   \"【Legend of Xianwu】EP01-60 FULL | Chinese Fantasy Anime | YOUKU ANIMATION\",\n                   \"【Legend of Xianwu】EP88 | Chinese Fantasy Anime | YOUKU ANIMATION\",\n                   \"ENGSUB【仙武传 Legend of Xianwu】EP90 预告Trailer  | 超燃玄幻国漫 | 优酷动漫 YOUKU ANIMATION\",\n                   \"ENGSUB【仙武传 Legend of Xianwu】EP1-80FULL  | 超燃玄幻国漫 | 优酷动漫 YOUKU ANIMATION\"],\n  \"search_query\": \"legend of xianwu EP89\"\n}\n```\n\n**Output:**\n```json\n{\n  \"index\": 0,\n  \"formatted_title\": \"[YouTube] Legend of Xianwu - E89\"\n}\n```\n\n### Example 2\n\n**Input:**\n```json\n{\n  \"video_titles\": [\"【ENGSUB】Immortality S3  EP01-16 collection【Join to watch latest】\",\n                   \"Immortality S3 EP4【Fantasy | Fighting | Fantasy | Made By Bilibili】\",\n                   \"Immortality S4 EP4【Fantasy | Fighting | Fantasy | Made By Bilibili】\",\n                   \"MENYERAP PIL RAKSASA STAR DOU #immortality  SEASON 3 EPISODE 4 -5\",\n                   \"Immortality Season 4 Episode 04 Preview (Eng Sub)\"],\n  \"search_query\": \"immortality s3 ep4\"\n}\n```\n\n**Output:**\n```json\n{\n  \"index\": 1,\n  \"formatted_title\": \"[YouTube] Immortality - S3E4\"\n}\n```\n\n### Example 3\n\n**Input:**\n```json\n{\n  \"video_titles\": [\"✨World of Immortals EP 04 [MULTI SUB]\",\n                   \"ENG SUB | \\\"World of Immortals\\\" EP04 | Deadly Formation | Tencent Video-ANIMATION\",\n                   \"[Eng Sub] World of Immortals  EP4 Part1\",\n                   \"ENG SUB | World of Immortals  [EP4 Part1] english sub\",\n                   \"EP04! Xiao Chen is entangled with a beautiful woman? The beautiful woman takes crazy revenge!\"],\n  \"search_query\": \"world of immortals ep4\"\n}\n```\n\n**Output:**\n```json\n{\n  \"index\": 1,\n  \"formatted_title\": \"[YouTube] World of Immortals - E4\"\n}\n```\n\n# Notes\n\n- For titles in Chinese, exclude them from the formatted title output.\n- The format `[YouTube] Title - S01E05 [1080p]` should only include available segments.\n- If a season or quality isn't available, omit those segments, leaving just `[YouTube] Title - Episode`."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"video_titles\": [\"【Legend of Xianwu】EP51 | Chinese Fantasy Anime | YOUKU ANIMATION\",\n\"【Legend of Xianwu】EP51-65 FULL | Chinese Fantasy Anime | YOUKU ANIMATION\",\n\"【Legend of Xianwu】EP01-60 FULL | Chinese Fantasy Anime | YOUKU ANIMATION\",\n\"【Legend of Xianwu】EP51 Trailer | Chinese Fantasy Anime | YOUKU ANIMATION\",\n\"【Legend of Xianwu】EP27-60 FULL | Chinese Fantasy Anime | YOUKU ANIMATION\"\n],\n  \"search_query\": \"legend of xianwu ep51\"\n}"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "```json\n{\n  \"index\": 0,\n  \"formatted_title\": \"[YouTube] Legend of Xianwu - E51\"\n}\n```"
        }
      ]
    }
  ],
  response_format={
    "type": "json_object"
  },
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
