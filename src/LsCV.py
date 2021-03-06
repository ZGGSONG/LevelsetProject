import cv2
from pylab import *

from src.redis_drive import redisUtils
from src.redis_drive_db1 import redisUtils_db1


class LsCV:

    def __init__(self):
        # 读入原图
        # Image = cv2.imread('../img/default.bmp', 1)
        re = redisUtils_db1()
        Image = cv2.imread(re.get_value("img_path"), 1)
        # print(re.get_value("img_path"))
        # 画初始轮廓
        image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        img = np.array(image, dtype='float64')

        # 初始化水平集函数
        IniLSF = np.ones([img.shape[0], img.shape[1]], img.dtype)
        IniLSF[30:80, 30:80] = -1
        IniLSF = -IniLSF

        # 模型参数
        # nu = 0.003 * 255 * 255
        # mu = 1
        # num = 10
        # epison = 1
        # step = 0.1
        r = redisUtils()
        # 长度约束系数
        nu = float(r.get_value("cvnu")) * 255 * 255
        # 惩罚项系数
        mu = float(r.get_value("cvmu"))
        # 迭代次数
        num = int(r.get_value("cvnum"))
        # 规则化参数
        epison = float(r.get_value("cvepison"))
        # 演变步长
        step = float(r.get_value("cvstep"))
        LSF = IniLSF
        for i in range(1, num):
            LSF = self.CV(LSF, img, nu, mu, epison, step)
            if i % 1 == 0:
                plt.imshow(Image), plt.xticks([]), plt.yticks([])
                plt.contour(LSF, [0], linewidths=3.0, colors='r')
                plt.draw(), plt.show()

    # CV函数
    def CV(self, LSF, img, nu, mu, epison, step):
        Drc = (epison / math.pi) / (epison * epison + LSF * LSF)
        #    Hea = 0.5*(1+(2/math.pi)*mat_math(LSF/epison,'atan'))
        Hea = 0.5 * (1 + (2 / math.pi) * np.arctan(LSF / epison))
        Iy, Ix = np.gradient(LSF)  ##q4#
        #    s = mat_math(Ix*Ix+Iy*Iy,"sqrt")
        s = np.sqrt(Ix * Ix + Iy * Iy)
        Nx = Ix / (s + 0.000001)
        Ny = Iy / (s + 0.000001)
        Mxx, Nxx = np.gradient(Nx)
        Nyy, Myy = np.gradient(Ny)
        cur = Nxx + Nyy

        Length = nu * Drc * cur

        Area = mu * Drc

        s1 = Hea * img
        s2 = (1 - Hea) * img
        s3 = 1 - Hea
        C1 = s1.sum() / Hea.sum()
        C2 = s2.sum() / s3.sum()

        CVterm = Drc * (-1 * (img - C1) * (img - C1) + 1 * (img - C2) * (img - C2))
        LSF = LSF + step * (Length + Area + CVterm)
        return LSF


if __name__ == '__main__':
    LsCV()
