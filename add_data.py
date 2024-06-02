import lyricsgenius
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import requests

def get_lyrics(title, artist):
  try:
      return genius.search_song(title, artist).lyrics
  except:
      return 'not found'

# Function to return sentiment score of each song
def get_lyric_sentiment(lyrics):
  sentiment = sid_obj.polarity_scores(lyrics)
  return sentiment


''' 원본 파일에서 가수, 제목을 통해서 가사 + 감정 점수 불러오기'''

# genius API 사용을 위한 토큰
genius = lyricsgenius.Genius(
    "lgHGVg-7RZ_QLMNZ-jeVn9lrCUfhyeR-FWe2QulGyeTU2DFYtfRVxwkGhLdCZIAa")
sid_obj = SentimentIntensityAnalyzer()
df = pd.read_csv('./Data-Preprocessing/lyrics_sentiment_dataset.csv')

df.loc[-1] = ['21744', 'Rap', 'Sohn SooKyoung', '2024', '''Even in this moment, sitting in the lecture hallMy mind is complicated, endless questionsSookmyung Women's University, that professorWhy do you make my life so difficult.
ISTP, my inner passion and angerEven when I argue logically, all I get is silenceI want to challenge, raise my voiceProfessor, here's what I want to say to you
Professor, please understand my feelingsDon't ignore the cries of a studentThe walls of Sookmyung Women's University are too highI can't stand it anymore, please listen to my words
My time trapped in piles of assignmentsMy passion that doesn't reach the professorISTP, my independent soulShould I fight, in this unfairness?
On the campus of Sookmyung Women's UniversityI'm wandering to find my dreamIn conflicts with the professor
Professor, please understand my feelingsDon't ignore the cries of a studentThe walls of Sookmyung Women's University are too highI can't stand it anymore, please listen to my words
ISTP, finding my own pathTogether with the professorStudent's anger, heading towards tomorrowWe walk together, holding onto hope''', '0.6576'] 

df.to_csv("./lyrics_sentiment_dataset.csv", index=False)