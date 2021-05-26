import redis

import redis


class redisUtils_db1:

    def __init__(self):
        '''
        初始化
        :param host:
        :param port:
        '''
        try:
            # self.r = redis.StrictRedis(host='*******', port=****, password="*******", db=0, decode_responses=True)
            self.r = redis.StrictRedis(host='127.0.0.1', port=6379, db=1, password="swj.", decode_responses=True)
        except Exception as e:
            print("redis连接失败,错误信息为%s" % e)

    def default(self):
        self.r.set("img_path", "/Users/zggsong/PycharmProjects/levelsetproject/src/img/default.bmp")

    def mflush(self):
        '''
        清空数据库
        :return:
        '''
        self.r.flushdb()

    def get_value(self, key):
        '''
        获取key的值
        :param key:
        :return:
        '''
        res = self.r.get(key)
        return res

    def set_key_value(self, key, value):
        '''
        往redis中设值
        :param key:
        :param value:
        :return:
        '''
        self.r.set(key, value)


if __name__ == '__main__':
    pass
