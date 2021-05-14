import imageio as imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2d
from src.lsca.drlse import gauss2D, drlse_edge
from src.redis_drive import redisUtils
from src.redis_drive_db1 import redisUtils_db1

class LsDRLSE:
    def __init__(self):
        # 读入原图
        # img = imageio.imread('./img/gray_r_01.bmp')
        re = redisUtils_db1()
        img = imageio.imread(re.get_value("img_path"))
        # If the image is not gray scale
        # img = img[:,:,0]

        # parameter setting
        timestep = 1
        mu = 0.2 / timestep
        iter_inner = 5
        iter_outer = 20
        lamda = 5
        alfa = -3
        # alfa  =1.5
        epsilon = 1.5
        sigma = 0.8
        # sigma = 1.5
        G = gauss2D((15, 15), sigma)
        img_smooth = conv2d(img, G, 'same')
        ix, iy = np.gradient(img_smooth)
        f = np.square(ix) + np.square(iy)
        g = 1.0 / (1 + f)

        # initialize LSF as binary step function
        c0 = 2;
        initialLSF = c0 * np.ones(img.shape)
        # generate the initial region R0 as two rectangles
        initialLSF[24:35, 19:25] = -c0
        initialLSF[24:35, 39:50] = -c0
        phi = initialLSF
        # imshow(phi)
        # ipdb.set_trace()
        # print(phi[24:35, 39:50])
        # phi0 = drlse_edge(phi, g, lamda, mu, alfa, lamda, epsilon, iter_inner, 'single-well')
        # ipdb.set_trace()

        # ax = plt.figure(1).gca(projection='3d')
        x_ = np.arange(img.shape[0])
        y_ = np.arange(img.shape[1])
        [x, y] = np.meshgrid(x_, y_)

        # plt.figure(1)
        # plt.imshow(img, cmap = 'gray_r')
        # plt.contour(x,y,phi[x,y],0)
        # imshow(img)
        # plt.show()
        potential = 2
        if potential == 1:
            potentialFunction = 'single-well'
        elif potential == 2:
            potentialFunction = 'double-well'
        else:
            potentialFunction = 'double-well'
        for i in range(iter_outer):
            ph = phi
            phi = drlse_edge(ph, g, lamda, mu, alfa, epsilon, timestep, iter_inner, potentialFunction)

        alfa = 0
        iter_refine = 10
        phi = drlse_edge(phi, g, lamda, mu, alfa, epsilon, timestep, iter_refine, potentialFunction)
        finalLSF = phi

        # ipdb.set_trace()
        # plt.imshow(img,interpolation='none', extent=(0, 59, 0, 77))
        # ax.plot_surface(x,y,-finalLSF[x,y],cmap=cm.Accent,linewidth=0.0, antialiased=True)
        # print(phi[:,22])

        fig, (ax1) = plt.subplots(nrows=1, figsize=(5, 5))
        ax1.imshow(img, cmap='gray', aspect='auto', interpolation='nearest')
        ax1.contour(y, x, finalLSF[x, y], 0, colors='r', linewidths=4)
        plt.show()


if __name__ == '__main__':
    LsDRLSE()