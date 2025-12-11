"""Discord bot for creating channels."""

import os
from os.path import join, dirname
import yaml
import discord
from dotenv import load_dotenv

# .envファイルを読み込む
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 環境変数の読み込み
token: str| None = os.getenv("TOKEN")
if token is None:
    raise ValueError("TOKEN environment variable is not set.")


# コマンドチャンネルIDのリストを作成
# yamlファイルからchannnel IDのリストを取得
with open("channels.yaml", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# チャンネルIDの辞書を取得
command_channels: dict[str,int] = config["COMMAND_CHANNELS"]
category_channels: dict[str,int] = config["CATEGORY_CHANNELS"]

# インテントの設定
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# クライアントの初期化
client: discord.Client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """イベント: ボットが起動したときに呼び出される。"""
    print('ChannelCreator is ready!')

# コマンドチャンネルでメッセージを監視
@client.event
async def on_message(message: discord.Message):
    """イベント: メッセージが送信されたときに呼び出される。"""
    if message.author == client.user:
        print("Message from bot itself; ignoring.")
        return

    # コマンドチャンネルでメッセージが送信された場合に処理を実行
    if command_channels and message.channel.id in command_channels.values():
        # メッセージが送信されたギルドを取得
        guild: discord.Guild| None = message.guild
        # チャンネルを作成するカテゴリーを取得
        try:
            guild_name_in_dict:str = [k for k, v in command_channels.items() if v == message.channel.id][0]
        except IndexError:
            print("No matching guild found for the command channel.")
            return
        category_channel = client.get_channel(category_channels[guild_name_in_dict])

        if guild is None:
            print("Guild not found.")
            return
        # 新しいテキストチャンネルを作成
        try:
            await category_channel.create_text_channel(name=f"{message.content}")
            print("Channel created successfully!")
        except Exception as e:
            print(f"Error creating channel: {e}")
    else:
        print("Message not in command channels; ignoring.")

# ボットを実行
client.run(token)
