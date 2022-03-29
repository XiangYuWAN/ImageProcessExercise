import numpy as np
import cv2
import copy
class util:
    @staticmethod
    def convertToGray(fname):
        return cv2.imread(fname,cv2.IMREAD_GRAYSCALE)
        #imgArray = np.array(imgI, dtype=np.uint32)
        #return cv2.cvtColor(imgArray, cv2.COLOR_BGR2GRAY)

    #A method of compare two images
    #input 2 images
    @staticmethod
    def compareImages(img1, img2):
        row1 = img1.shape[0]
        col1 = img1.shape[1]
        compare = True
        for i in range(0, row1):
            for j in range(0, col1):
                if img2[i, j] != img1[i, j]:
                    compare = False
        return compare

    #A method transform grade image to binary image
    # input image and threshold
    @staticmethod
    def thresholdImage(img1, threshold):
        # judge img1 is grade or not
        if (img1.max() != 255) or (img1.min() != 0):
            raise ValueError("input image's pixel value must be grade")
        value = threshold  # threshold value
        img2 = img1.copy()
        nrows = img1.shape[0]
        ncols = img1.shape[1]

        for i in range(0, ncols):
            for j in range(0, nrows):
                if img2[i, j] < value:
                    img2[i, j] = 0
                else:
                    img2[i, j] = 255
        return img2


    # A method of Supremum two images
    # input 2 images
    @staticmethod
    def imageSup(img1, img2):
        irow = img1.shape[0]
        icol = img1.shape[1]
        imgSup = img1
        # supremum img1 and img2
        for i in range(0, irow):
            for j in range(0, icol):
                imgSup[i, j] = max(img1[i, j], img2[i, j])
        return imgSup

    # A method of Infimum two images,
    # input 2 images
    @staticmethod
    def imageInf(img1, img2):
        irow = img1.shape[0]
        icol = img1.shape[1]
        imgInf = img1
        # Inf  img1 and img2
        for i in range(0, irow):
            for j in range(0, icol):
                imgInf[i, j] = min(img1[i, j], img2[i, j])
        return imgInf

    @staticmethod
    def getMaxPoint(image, kernel, x,y):
        width,height = kernel.shape
        max=-1
        out=""
        for i in range(0,width):            
                for j in range(0,height):
                    limitX, limitY = image.shape
                    px=x+i-(width-round(width/2))
                    py=y+j-(height-round(height/2))
                    if 0 <= px < limitX and 0 <= py < limitY:
                        point=image[px,py]
                        out=out+str(point)+" "
                        max=point if point> max else max                
                out=out+"\n"
        #print(out, "Max: ",max)        
        return max

    def getMinPoint(image, kernel, x,y):
        width,height = kernel.shape
        max=256
        out=""
        for i in range(0,width):            
                for j in range(0,height):
                    limitX, limitY = image.shape
                    px=x+i-(width-round(width/2))
                    py=y+j-(height-round(height/2))
                    if 0 <= px < limitX and 0 <= py < limitY:
                        point=image[px,py]
                        out=out+str(point)+" "
                        max=point if point< max else max                
                out=out+"\n"
        #print(out, "Max: ",max)        
        return max

    @staticmethod
    def dilate(img, kernelSize):
        imgOutput = img.copy()
        rows, cols = img.shape[0], img.shape[1]
        k = kernelSize

        for i in range(0, rows):
            for j in range(0, cols):
                max = 0
                for x in range(i - k, i + k + 1):
                    for y in range(j - k, j + k + 1):
                        if x >= 0 and x < rows and y >= 0 and y < cols:
                            pixel = img[x, y]
                            if (pixel > max):
                                max = pixel
                imgOutput[i, j] = max
        return imgOutput
        '''
        # width,height = image.shape
        # imgOutput = copy.deepcopy(image)
        #
        # for i in range(width):
        #     for j in range(height):
        #         max=util.getMaxPoint(image, kernel, i,j)
        #         if max<=255:
        #             imgOutput[i,j] = max
        # return imgOutput
        '''

    @staticmethod
    def erode(img, kernelSize):
        imgOutput = img.copy()
        rows, cols = img.shape[0], img.shape[1]
        k = kernelSize

        for i in range(0, rows):
            for j in range(0, cols):
                min = 10000
                for x in range(i - k, i + k + 1):
                    for y in range(j - k, j + k + 1):
                        if x >= 0 and x < rows and y >= 0 and y < cols:
                            pixel = img[x, y]
                            if (pixel < min):
                                min = pixel
                imgOutput[i, j] = min
        return imgOutput
        '''
        # width,height = image.shape
        # imgOutput = copy.deepcopy(image)
        #
        # for i in range(width):
        #     for j in range(height):
        #         min=util.getMinPoint(image, kernel, i,j)
        #         if min >= 0:
        #             imgOutput[i,j] = min
        # return imgOutput
        '''
    #A method of compare two images
    #input 2 images
    @staticmethod
    def isEquals(img1, img2):
        width,height = img1.shape
        for i in range(width):
            for j in range(height):
                if img2[i, j] != img1[i, j]:                    
                    return False
        return True

    #openning
    @staticmethod
    def opening(image, kernelSize):
        ero = util.erode(image,kernelSize)
        result = util.dilate(ero, kernelSize)
        return result

    #closing
    @staticmethod
    def closing(image, kernelSize):
        dia = util.dilate(image, kernelSize)
        result = util.erode(dia, kernelSize)
        return result

    #closing
    @staticmethod
    def compareTxt(image1, Image2, outputName):
        isEquals=0
        if util.isEquals(image1,Image2):
            isEquals=1 
        print("comparación: ",isEquals)
        f = open(outputName, "a")
        f.write(str(isEquals))
        f.close()

    @staticmethod
    def closingOpening(image, size):
        output01 = util.opening(image, size)
        output02 = util.closing(output01, size)
        return output02

    @staticmethod
    def openingClosing(image, size):
        output01 = util.closing(image, size)
        output02 = util.opening(output01, size)
        return output02

############################################################################

