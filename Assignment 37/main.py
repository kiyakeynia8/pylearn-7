import cv2

image = cv2.imread("mnist.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for n in range(10):
    for i in range(5):
        for j in range(100):
            s = (n*5 + i)*20
            c = j*20
            cv2.imwrite(f"numbers/{n}/{n}_{i}_{j}.png",image[s : s+20,c : c+20])