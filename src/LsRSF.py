# coding:utf-8
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math


class LsRSF:
    def DrawContour(self, LSF, p1, p2):
        plt.clf()
        plt.imshow(self.Image), plt.xticks([]), plt.yticks([])
        plt.contour(LSF, [0], color=p1, linewidth=p2)
        plt.show()

    def mat_math(self, intput, str):
        output = intput
        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                if str == "atan":
                    output[i, j] = math.atan(intput[i, j])
                if str == "sqrt":
                    output[i, j] = math.sqrt(intput[i, j])
        return output

    def RSF(self, LSF, img, mu, nu, epison, step, lambda1, lambda2, kernel):
        Drc = (epison / math.pi) / (epison * epison + LSF * LSF)
        Hea = 0.5 * (1 + (2 / math.pi) * self.mat_math(LSF / epison, "atan"))
        Iy, Ix = np.gradient(LSF)
        s = self.mat_math(Ix * Ix + Iy * Iy, "sqrt")
        Nx = Ix / (s + 0.000001)
        Ny = Iy / (s + 0.000001)
        Mxx, Nxx = np.gradient(Nx)
        Nyy, Myy = np.gradient(Ny)
        cur = Nxx + Nyy
        Length = nu * Drc * cur

        Lap = cv2.Laplacian(LSF, -1)
        Penalty = mu * (Lap - cur)

        KIH = cv2.filter2D(Hea * img, -1, kernel)
        KH = cv2.filter2D(Hea, -1, kernel)
        f1 = KIH / KH
        KIH1 = cv2.filter2D((1 - Hea) * img, -1, kernel)
        KH1 = cv2.filter2D(1 - Hea, -1, kernel)
        f2 = KIH1 / KH1
        R1 = (lambda1 - lambda2) * img * img
        R2 = cv2.filter2D(lambda1 * f1 - lambda2 * f2, -1, kernel)
        R3 = cv2.filter2D(lambda1 * f1 * f1 - lambda2 * f2 * f2, -1, kernel)
        RSFterm = -Drc * (R1 - 2 * R2 * img + R3)

        LSF = LSF + step * (Length + Penalty + RSFterm)
        # plt.show(s, cap ='gray'),plt.show();
        return LSF

    Image = cv2.imread('img/default.bmp', 1)
    image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    img = np.float64(image)

    # Kernel
    sig = 3
    kernel = np.ones((sig * 4 + 1, sig * 4 + 1), np.float64) / (sig * 4 + 1) ** 2

    IniLSF = np.ones((img.shape[0], img.shape[1]), img.dtype)
    IniLSF[30:80, 30:80] = -1
    IniLSF = -IniLSF

    Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
    plt.figure(1)
    DrawContour(IniLSF, 'r', 2)

    def __init__(self):
        mu = 1
        nu = 0.003 * 255 * 255
        num = 50
        epison = 1
        step = 0.1
        lambda1 = lambda2 = 1
        LSF = self.IniLSF

        for i in range(1, num):
           LSF = self.RSF(LSF, self.img, mu, nu, epison, step, lambda1, lambda2, self.kernel)
        self.DrawContour(LSF, 'r', 2)


if __name__ == '__main__':
    LsRSF()