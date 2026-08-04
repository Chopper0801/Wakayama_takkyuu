import os
import tweepy

# GitHub Secretsから認証情報を取得
API_KEY = os.environ.get("X_API_KEY")
API_SECRET = os.environ.get("X_API_SECRET")
ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("X_ACCESS_TOKEN_SECRET")

# --- v2 API Client の初期化 ---
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# 投稿メッセージ
tweet_text = """【自動更新】近畿の卓球大会スケジュールを更新しました！

最新の大会日程・要項はこちらからチェックしてください🏓
https://chopper0801.github.io/kinki-tabletennis/

#卓球 #近畿卓球 #大会情報
"""

try:
    # v2 API の create_tweet メソッドでポスト
    response = client.create_tweet(text=tweet_text)
    print("Tweet successfully posted! ID:", response.data['id'])
except Exception as e:
    print("Error posting tweet:", e)
