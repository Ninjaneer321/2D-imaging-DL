import numpy as np
def dicom_to_rgb(img,bt,wt):

        # enforce boundary conditions
        img = np.clip(img,bt,wt)

        # linear transformation
        # multiplicative
        img = np.multiply(img,-255/(wt-bt)).astype(np.int)
        # additive
        img += 255

        # stack thrice on the last axis for R G B
        rgb_img = np.stack([img]*3,axis=-1)

        return rgb_img



bt = 0
wt = 1400

dicom_file = dicom.read_file(filename)
img = np.array(dicom_file.pixel_array)

rgb = dicom_to_rgb(img,wt,bt)
