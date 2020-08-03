import sys
import numpy 
import cv2
import os

MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30


def main():

    trainingImage = cv2.imread(r"C:\Users\MrChocolat3-\Desktop\Ellie_V0_1_03\test\chars.png")

    if trainingImage is None:
        print("Image is none")

    imgGray = cv2.cvtColor(trainingImage, cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.GaussianBlur(imgGray, (5, 5), 0)

    imgFiltered = cv2.adaptiveThreshold(imgBlurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    cv2.imshow("ThursHoldImage", imgFiltered)

    imgfilteredCopy = imgFiltered.copy()

    npaContours, npaHierarchy = cv2.findContours(imgfilteredCopy,        # input image, make sure to use a copy since the function will modify this image in the course of finding contours
                                                              cv2.RETR_EXTERNAL,                 # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE)  

    npaFlattenedImages = numpy.empty(
        (0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))

    intClassifictaion = list()

    intValidChars = [ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9'),
                     ord('A'), ord('B'), ord('C'), ord('D'), ord('E'), ord(
                         'F'), ord('G'), ord('H'), ord('I'), ord('J'),
                     ord('K'), ord('L'), ord('M'), ord('N'), ord('O'), ord(
                         'P'), ord('Q'), ord('R'), ord('S'), ord('T'),
                     ord('U'), ord('V'), ord('W'), ord('X'), ord('Y'), ord('Z')
                     ]
    # ,
    #                  ord('a'), ord('b'), ord('c'), ord('d'), ord('e'), ord(
    #                      'f'), ord('g'), ord('h'), ord('i'), ord('j'),
    #                  ord('k'), ord('l'), ord('m'), ord('n'), ord('o'), ord(
    #                      'p'), ord('q'), ord('r'), ord('s'), ord('t'),
    #                  ord('u'), ord('v'), ord('w'), ord('x'), ord('y'), ord('z')
    for npaContour in npaContours:

        if cv2.contourArea(npaContour) > MIN_CONTOUR_AREA:
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)

            cv2.rectangle(trainingImage, (intX, intY), (intX+intW, intY+intH), (0,0,255), 2)

            imgROI = imgFiltered[intY:intY+intH, intX:intX+intW]

            imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))


            cv2.imshow("imgROI", imgROI)

            cv2.imshow("imgROIResized", imgROIResized)

            cv2.imshow("TrainingImage", trainingImage)

            intChar = cv2.waitKey(0)

            if intChar == 27:
                sys.exit()

            elif intChar in intValidChars:

                 # append classification char to integer list of chars (we will convert to float later before writing to file)
                intClassifictaion.append(intChar)

                # flatten image to 1d numpy array so we can write to file later
                npaFlattenedImage = imgROIResized.reshape(
                    (1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
                # add current flattened impage numpy array to list of flattened image numpy arrays
                npaFlattenedImages = numpy.append(
                    npaFlattenedImages, npaFlattenedImage, 0)
    

    fltClassifications = numpy.array(intClassifictaion, numpy.float32)

    npaClassifications = fltClassifications.reshape((fltClassifications.size, 1))

    print ("Training Complete")

    numpy.savetxt("classifications.txt", npaClassifications)
    numpy.savetxt("flattened_images.txt", npaFlattenedImages)

    cv2.destroyAllWindows()

    return


if __name__ == "__main__":
    main()