import numpy as np
import cv2
from numpy import asarray
from PIL import Image
# SOURCES
# https://towardsdatascience.com/histogram-equalization-a-simple-way-to-improve-the-contrast-of-your-image-bcd66596d815


class ComputerVisionAlgorithms():

    def histogram_equalization(original_img, x1, x2, y1, y2):
        original_img = asarray(original_img)
        # crop image in order to equalize only the histogram of the needed part,
        img_in = original_img[x1:x2, y1:y2]
        # segregate color streams
        try:
            b, g, r, alpha = cv2.split(img_in)
            fourChan = True

        except:
            b, g, r = cv2.split(img_in)
            fourChan = False

        h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256])
        h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
        h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
        # calculate cdf
        cdf_b = np.cumsum(h_b)
        cdf_g = np.cumsum(h_g)
        cdf_r = np.cumsum(h_r)

        # mask all pixels with value=0 and replace it with mean of the pixel values
        cdf_m_b = np.ma.masked_equal(cdf_b, 0)
        cdf_m_b = (cdf_m_b - cdf_m_b.min())*255/(cdf_m_b.max()-cdf_m_b.min())
        cdf_final_b = np.ma.filled(cdf_m_b, 0).astype('uint8')

        cdf_m_g = np.ma.masked_equal(cdf_g, 0)
        cdf_m_g = (cdf_m_g - cdf_m_g.min())*255/(cdf_m_g.max()-cdf_m_g.min())
        cdf_final_g = np.ma.filled(cdf_m_g, 0).astype('uint8')
        cdf_m_r = np.ma.masked_equal(cdf_r, 0)
        cdf_m_r = (cdf_m_r - cdf_m_r.min())*255/(cdf_m_r.max()-cdf_m_r.min())
        cdf_final_r = np.ma.filled(cdf_m_r, 0).astype('uint8')

        # merge the images in the three channels
        img_b = cdf_final_b[b]
        img_g = cdf_final_g[g]
        img_r = cdf_final_r[r]
        if fourChan == True:
            img_out = cv2.merge((img_b, img_g, img_r, alpha))
        else:
            img_out = cv2.merge((img_b, img_g, img_r))
        # validation

        equ_b = cv2.equalizeHist(b)
        equ_g = cv2.equalizeHist(g)
        equ_r = cv2.equalizeHist(r)
        if fourChan == True:
            equ = cv2.merge((img_b, img_g, img_r, alpha))
        else:
            equ = cv2.merge((img_b, img_g, img_r))

        original_img[x1:x2, y1:y2] = equ
        # print(equ)
        cv2.imwrite('equalizedImage.png', original_img)
        original_img = Image.fromarray(original_img)
        return original_img