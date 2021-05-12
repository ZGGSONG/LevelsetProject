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
            self.r = redis.StrictRedis(host='47.98.103.241', port=6060, password="jiaobaba", db=0, decode_responses=True)
        except Exception as e:
            print("redis连接失败,错误信息为%s" % e)

    def mflush(self):
        self.r.flushdb()

    def get_value(self, key):
        '''
        获取key的值
        :param key:
        :return:
        '''
        res = self.r.get(key)
        return res

    def get_ttl(self, key):
        '''
        获取key的过期时间
        :param key:
        :return:
        '''
        return self.r.ttl(key)

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
