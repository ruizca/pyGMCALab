# -*- coding: utf-8 -*-
import time

import matplotlib.pyplot as plt
import numpy as np
from pyredwave import RedWave, mad_std
from scipy.misc import face

# process several slices in parallel (each line of x)
x = np.array([[1.0, 2.0, 3, 4], [3, 4, 3, 4]])
print("Input matrix:")
print(x)
# parametrize wavelets
wave_filter = "Haar"
number_of_scales = 2
isometric = True
wave_dimensions = 1
wave = RedWave(x, wave_dimensions, wave_filter, number_of_scales, isometric)
wx = wave.forward(x)
print("Output matrix (wavelet performed on dimension 1, on 2 slices):")
print(wx)
x2 = wave.backward(wx)
# in place transformation
wave.transform(x, wx, 1)
# create a wavelet object for inputs of size Face
print("Wavelet can be performed on any 1 or 2 dimensions.")
# load an image
face = face()
# convert it to double
face = face.astype("float64")
wave_dimensions = (1, 0)
wave_filter = "Daubechies-4"
wave = RedWave(face, wave_dimensions, wave_filter, number_of_scales, isometric)
# convert Face into wavelets
wface = wave.forward(face)
# show Face in the wavelet domain
plt.imshow(wface, cmap=plt.cm.gray)
plt.show()
#collect()

# Only the first coarse scale is actually used for backward computation
print("Only the first coarse scale is actually used for backward computation.")
wface = wave.remove_coarse_scales(wface, inplace=True, keep_actual_coarse_scale=True)
plt.imshow(wface, cmap=plt.cm.gray)
plt.show()

print("In isometric mode, norms are kept (after removing redundant coarse scales):")
print("- norm of Face: %s." % np.linalg.norm(face))
print("- norm of Face wavelet coefficients: %s." % np.linalg.norm(wface))
time.sleep(2)
print("One can also easily get estimate the noise on each scale using ")
print("extract_scale_vals with the mad estimator (or any other).")
scale_mad = wave.extract_scale_vals(wface, mad_std)
print("Mad estimate on each scale:")
print(scale_mad)
print("From there, one can make a full matrix using make_full_vals.")
# wavelet thresholding
lambdas = 50 * np.ones(wface.shape)
# do not penalize coarse scales
lambdas = wave.remove_coarse_scales(lambdas, inplace=True, keep_actual_coarse_scale=False)
smooth_face = wave.sparse_proximal(face, lambdas, number_of_iterations=6)
print("This toolbox can also compute the wavelet sparse analysis proximal")
print("operator using the Generalized Forward-Backward algorithm (displayed")
print("results), and the sparse analysis inversion using Chambolle-Pock\nalgorithm.")
plt.imshow(smooth_face, cmap=plt.cm.gray)
plt.show()
#collect()

