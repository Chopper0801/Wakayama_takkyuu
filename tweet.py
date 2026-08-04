import os
import tweepy

# GitHub Secretsから認証情報を取得
API_KEY = os.environ.get("X_API_KEY")
API_SECRET = os.environ.get("X_API_SECRET")
ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("X_ACCESS_TOKEN_SECRET")

# --- OAuth 1.0a 認証設定 ---
auth = tweepy.OAuth1UserHandler(
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

# API v1.1 インスタンス生成（投稿用）
api = tweepy.API(auth)

# 投稿メッセージ
tweet_text = """【自動更新】近畿の卓球大会スケジュールを更新しました！

最新の大会日程・要項はこちらからチェックしてください🏓
https://chopper0801.github.io/kinki-tabletennis/

#卓球 #近畿卓球 #大会情報
"""

try:
    # v1.1 の update_status メソッドでポスト
    status = api.update_status(status=tweet_text)
    print("Tweet successfully posted! ID:", status.id)
except Exception as e:
    print("Error posting tweet:", e)
