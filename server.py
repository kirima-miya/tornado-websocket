from pathlib import Path
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.options
import asyncio
import signal
from logging import getLogger

logger = getLogger(__name__)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    # 接続開始
    def open(self):
        logger.info('WebSocket is open.')

    # 受信
    def on_message(self, message):
        logger.info('WebSocket message received: ' + message)
        self.write_message('Hello client!')

    # 接続終了
    def on_close(self):
        logger.info('WebSocket is closed.')


class ShutdownManager():
    """サーバー停止機能を管理"""
    def __init__(self):
        self.shutdown_flag = False  # 次のイベントループでシャットダウンするかどうか

    def reserve_shutdown(self, signum, frame):
        logger.info('shutdown reserved')
        self.shutdown_flag = True

    def try_shutdown(self):
        if self.shutdown_flag:
            tornado.ioloop.IOLoop.current().stop()
            logger.info('shutdown success')


app = tornado.web.Application(
    [
        (r'/', MainHandler),
        (r'/websocket', WebSocketHandler),
    ],
    template_path=Path('templates'),
    static_path=Path('static'),
)
shutdown_manager = ShutdownManager()


def main():
    # windowsで実行する場合, イベントループポリシーを変更する
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)

    # ターミナルにデバック情報を表示する
    tornado.options.parse_command_line()

    # SIGINT(Ctrl + C)でサーバーを停止できるようにする
    signal.signal(signal.SIGINT, shutdown_manager.reserve_shutdown)
    tornado.ioloop.PeriodicCallback(shutdown_manager.try_shutdown, 100).start()

    # サーバー起動
    app.listen(8888)  # http://localhost:8888/
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
