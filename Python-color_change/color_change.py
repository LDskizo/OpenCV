# -*- coding: utf-8 -*-
import cv2
import numpy as np

if __name__ == '__main__':

    # 画像取得
    im_in = cv2.imread("test.jpg",1)

    # im_inと同じサイズのオブジェクト生成
    im_o =np.zeros((im_in.shape[0],im_in.shape[1],im_in.shape[2]),np.uint8)

    # 複数色チャンネルの分割
    im_in_bgr = cv2.split(im_in)

    # 青→赤、緑→青、赤→緑に変更
    im_o[:,:,0] = im_in_bgr[2]
    im_o[:,:,1] = im_in_bgr[0]
    im_o[:,:,2] = im_in_bgr[1]

    # 画像表示
    cv2.imshow("Change Color Image",im_o)

    # キー入力待機
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("after_test.jpg", im_o)
