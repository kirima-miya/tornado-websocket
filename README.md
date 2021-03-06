# 概要

Tornado(Python web framework)を用いた WebSocket 通信

# 実行環境

- Anaconda (Python3.8.12 + ライブラリ群)
- VSCode

# 操作

## サーバー

- サーバー起動: `server.py` を実行
- サーバー停止: `Ctrl + C`

## クライアント用ページ

- http://localhost:8888/
- http://127.0.0.1:5500/ (Live Server プラグイン。自動更新できるので楽)

- アクセス時、WebSocket コネクション確立。<br>
  サーバーから受信したオブジェクト ID をコンソールに表示。<br>

- sent ボタン押下で、サーバー側ターミナルにメッセージ表示。

# フォルダ構成

| フォルダ・ファイル名 | 説明                                                  |
| :------------------- | :---------------------------------------------------- |
| static               | 静的ファイル（HTML, CSS, JavaScript, img）などを格納  |
| templates            | テンプレート（HTML）を格納 <br>※ 動的に生成するページ |
| index.html           | Live Server プラグイン用<br>※ 自動更新できるので楽。  |
| `server.py`          | サーバー機能                                          |

# 参考文献

- [Tornado 公式ドキュメント](https://www.tornadoweb.org/en/stable/)
- [Tornado 公式 GitHub](https://github.com/tornadoweb/tornado/tree/stable)
  ※Demo 有
