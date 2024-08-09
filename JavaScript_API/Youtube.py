from youtube_transcript_api import YouTubeTranscriptApi

# Replace 'video_id' with the actual ID of the YouTube video
# video_id = 'd6iQrh2TK98'

from youtube_transcript_api import YouTubeTranscriptApi

url = 'https://www.youtube.com/watch?v=TYSc4Xg3xLs'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

# print(transcript)

output=''
for x in transcript:
  sentence = x['text']
  output += f' {sentence}\n'

print(output)