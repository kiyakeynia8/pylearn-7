import cv2
import numpy as np
import matplotlib.pyplot as plt
from KNN_main import KNN

class FindingNemo:
    def __init__(self, train_image):
        self.knn = KNN(k=3)
        X_train, Y_train = self.convert_image_to_dataset(train_image)
        self.knn.fit(X_train, Y_train)
    
    def convert_image_to_dataset(self, image):
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        light_orange = (1, 100, 100)
        dark_orange = (60, 255, 255)
        light_white = (0, 0, 150)
        dark_white = (145, 60, 255)
        light_black = (0, 0, 0)
        dark_black = (255, 255, 50)

        mask_orange = cv2.inRange(image_hsv, light_orange, dark_orange)
        mask_white = cv2.inRange(image_hsv, light_white, dark_white)
        mask_black = cv2.inRange(image_hsv, light_black, dark_black)

        final_mask = mask_orange + mask_white + mask_black

        pixels_list_hsv = image_hsv.reshape(-1, 3)
        X_train = pixels_list_hsv / 255

        Y_train = final_mask.reshape(-1,) // 255

        return X_train, Y_train

    def remove_background(self, test_image):
        test_image = cv2.resize(test_image, (0, 0), fx= 0.25, fy=0.25)
        test_image_hsv = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        X_test = test_image_hsv.reshape(-1, 3) / 255
        Y_pred = self.knn.predict(X_test)

        output = np.array(Y_pred).reshape(test_image.shape[:2])
        output = output.astype('uint8')
        final_result = cv2.bitwise_and(test_image, test_image, mask= output)

        return final_result

if __name__ == "__main__":
    image_train = cv2.imread("nemo.jpg")
    image_test = cv2.imread("dadash_nemo.jpg")
    findingnemo = FindingNemo(image_train)
    image = findingnemo.remove_background(image_test)
    plt.imshow(image, cmap="gray")
    plt.show()