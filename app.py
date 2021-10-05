import tornado.ioloop
import tornado.web
import asyncio


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


app = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    # windowsで実行する場合, イベントループポリシーを変更する
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)

    app.listen(8888)  # http://localhost:8888/
    tornado.ioloop.IOLoop.current().start()
