import redis

import redis


class redisUtils:

    def __init__(self):
        '''
        初始化
        :param host:
        :param port:
        '''
        try:
            self.r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password="swj.", decode_responses=True)
        except Exception as e:
            print("redis连接失败,错误信息为%s" % e)

    def defalut(self):
        self.r.set("cvnu", "6.5025")
        self.r.set("cvmu", "1")
        self.r.set("cvnum", "10")
        self.r.set("cvepison", "1")
        self.r.set("cvstep", "0.1")

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
