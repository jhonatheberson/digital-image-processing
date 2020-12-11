def prof_kmeans(img):
    nClusters = 8
    nRodadas = 5

    samples = img.copy()
    samples = np.array(samples.reshape(-1, 3))
    samples = samples.astype(np.float32)

    ret, label, center = cv.kmeans(samples,
                                   nClusters,
                                   None,
                                   (cv.TERM_CRITERIA_MAX_ITER | cv.TERM_CRITERIA_EPS, 10000, 0.0001),
                                   nRodadas,
                                   cv.KMEANS_PP_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape(img.shape)

    return res2