# Discord Channel Creator

特定のチャンネルに投稿されたメッセージを検知し、そのメッセージ内容をチャンネル名として新しいテキストチャンネルを自動で作成するDiscordBotです。

## 機能

- 指定された「コマンド用チャンネル」へのメッセージ投稿をトリガーにします。
- 投稿されたメッセージの内容をそのまま新しいチャンネルの名前にします。
- 指定された「カテゴリ」配下に新しいテキストチャンネルを作成します。

## 使い方

### 1. 準備

#### a. リポジトリのクローン

```bash
git clone https://github.com/your-username/tucc_ChannelCreator.git
cd tucc_ChannelCreator
```

#### b. Python仮想環境の作成と有効化

- Windows:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- macOS / Linux:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### c. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. Botの設定

#### a. DiscordBotのトークンを設定

1. `.env.template` ファイルをコピーして `.env` という名前のファイルを作成します。
2. `.env` ファイルを開き、`PUT_YOUR_BOT_TOKEN` の部分をあなたのDiscordBotのトークンに書き換えます。

    ```.env
    TOKEN=ここにあなたのDiscordBotのトークンを貼り付け
    ```

    > **Note:** BotのトークンはDiscord Developer Portal で取得できます。Botに `Manage Channels` の権限を与えてください。

#### b. チャンネルIDを設定

1. `channels.yaml.template` ファイルをコピーして `channels.yaml` という名前のファイルを作成します。
2. `channels.yaml` ファイルを開き、Botがコマンドを監視するチャンネルのIDと、新しいチャンネルを作成するカテゴリのIDを記述します。

    - `COMMAND_CHANNELS`: Botがメッセージを監視するテキストチャンネルのID。
    - `CATEGORY_CHANNELS`: 新しいチャンネルを作成する先のカテゴリのID。

    `Guild1` のような名前は、どのサーバーの設定かを分かりやすくするためのものです。好きな名前に変更できます。

    **例:**

    ```yaml
    COMMAND_CHANNELS:
      MyServer: 123456789012345678 # コマンドを受け付けるチャンネルのID

    CATEGORY_CHANNELS:
      MyServer: 987654321098765432 # チャンネルを作成するカテゴリのID
    ```

    > **Note:** チャンネルIDやカテゴリIDは、Discordで開発者モードを有効にした後、対象を右クリックして「IDをコピー」することで取得できます。

### 3. Botの実行

設定が完了したら、以下のコマンドでBotを起動します。

```bash
python main.py
```

コンソールに `ChannelCreator is ready!` と表示されれば、Botは正常に起動しています。

### 4. チャンネルの作成

`channels.yaml` で設定した `COMMAND_CHANNELS` のチャンネルに、作成したいチャンネルの名前（例: `新しいプロジェクト`）を投稿すると、`CATEGORY_CHANNELS` で設定したカテゴリ内に `#新しいプロジェクト` という名前のテキストチャンネルが自動で作成されます。
