import opencv as cv2

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian

    return cv2.Laplacian(image, cv2.CV_64F).var()
