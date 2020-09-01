import cv2
import numpy as np
import random


#The ImageShape class is created

class imageShape:

    def __init__(self, width, height):

       self.width = width #Width variable is declared
       self.height = height #Height variable is declared

       self.shape = np.zeros((self.height, self.width, 3), dtype= np.uint8) #A black background window of size (width,height) is generated

       self.number = random.randint(0, 4) #A uniformly distributed random number is generated that takes values between 0 and 1


    def generateShape (self): #The first method is generated where an image with a geometric figure is stored

        #The points are defined to centralize the figures

        width_middle = self.width / 2
        height_middle = self.height / 2
        minimum = int(min(self.height, self.width) / 2)


        #If the number is 0, a triangle is shown as figure

        if self.number == 0:
            print('El número aleatorio escogido fue 0') #The value of the chosen number is printed
            p1t = (int(width_middle), int(height_middle - int((np.sqrt(3) / 2) * (minimum / 2)))) #The coordinates of the first vertex are determined
            p2t = (int(width_middle) - int(self.width / 4), int(height_middle + ((np.sqrt(3) / 2) * (minimum / 2)))) #The coordinates of the second vertex are determined
            p3t = (int(width_middle) + int(self.width / 4), int(height_middle + ((np.sqrt(3) / 2) * (minimum / 2)))) #The coordinates for the third and last vertex are determined
            pts = np.array([p1t, p2t, p3t])
            self.shape = cv2.drawContours(self.shape, [pts], 0, (255, 255, 0), -1) #The shape of the figure is generated
            cv2.imshow('triangulo', self.shape)
            cv2.waitKey(0)

        #If the number is 1, a square is shown as a figure.

        elif self.number == 1:

            print('El número aleatorio escogido fue 1') #The value of the chosen number is printed
            p1s = (int(width_middle) - int(minimum / 2), int(height_middle) - int(minimum/ 2)) #The coordinates of the first vertex are determined
            p2s = (int(width_middle) + int(minimum / 2), int(height_middle) + int(minimum / 2)) #The coordinates of the second vertex are determined
            cv2.rectangle(self.shape, p1s, p2s, [255, 255, 0], -1) #The shape of the figure is generated
            rot_sq = cv2.getRotationMatrix2D((int(width_middle), int(height_middle)), 45, 1.0 ) #The figure is rotated 45 °
            self.shape = cv2.warpAffine(self.shape, rot_sq, (self.width, self.height)) #The square rotated 45 ° is generated
            cv2.imshow('cuadrado', self.shape) #Shows the figure
            cv2.waitKey(0)


        #If the number is 2, a rectangle is shown as shown

        elif self.number == 2:
            print('El número aleatorio escogido fue 2')  #The value of the chosen number is printed
            p1r = (int(width_middle) - int(self.width / 4), int(height_middle) - int(self.height / 4)) #The coordinates of the first vertex are determined
            p2r = (int(width_middle) + int(self.width / 4), int(height_middle) + int(self.height / 4)) #The coordinates of the second vertex are determined
            cv2.rectangle(self.shape, p1r, p2r, [255, 255, 0], -1) #The shape of the figure is generated
            cv2.imshow('rectangulo', self.shape) #Shows the figure
            cv2.waitKey(0)

        #If the number is 3, a circle is shown as a figure

        else:
            print('El número aleatorio escogido fue 3') #The value of the chosen number is printed
            cv2.circle(self.shape, (int(width_middle), int(height_middle)), int(minimum / 2), [255, 255, 0], -1) #The shape of the figure is generated
            cv2.imshow('Circulo', self.shape) #Shows the figure
            cv2.waitKey(0)


    def showShape (self): #The second method is created

        cv2.imshow('', self.shape)
        cv2.waitKey(5000)

    def getShape (self):  #The third method is created

        # Print the image obtained according to the random number

        if self.number == 0:
            print('The chosen figure is a triangle')

        elif self.number == 1:
            print('The chosen figure is a square rotated 45 °')

        elif self.number == 2:
            print('The chosen figure is a rectangle')

        #In the case that none of the figures is taken, the system shows a black window

        else:
            print('The chosen figure is a circle')
            cv2.imshow(' ', self.shape)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def whatShape(self):  # The fourth method is create

        #The image stored in self.shape is loaded, then converted to grayscale, binarized, and the outline is found

        image = self.shape
        im_draw = image.copy()
        im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, Ibw_shapes = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # For all generated contours: the image is classified according to the characteristics of its contour

        for i in contours:
            curve = cv2.approxPolyDP(i, 3, True)
            x, y, w, h = cv2.boundingRect(curve)
            if len(curve) == 3:
                print('The figure is a triangle ')
            if len(curve) == 4:
                pp = w / h
                if pp == 1:
                    print('The figure is a square')
                else:
                    print('The figure is a rectangle')
            if len(curve) > 10:
                print('The figure is a circle')

            cv2.drawContours(im_draw, [curve], 0, (0, 0, 255), 2)  # Finally the system draws the contours generated
            cv2.imshow('The final image', im_draw)  # Shows the result
            cv2.waitKey(0)