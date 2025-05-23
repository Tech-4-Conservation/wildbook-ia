#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import cv2
import numpy as np
import utool

from wbia.plottool import draw_func2 as df2
from wbia.plottool import viz_image2
from wbia.plottool.tests.test_helpers import dummy_bbox

WILDBOOK_IA_MODELS_BASE = os.getenv('WILDBOOK_IA_MODELS_BASE', 'https://wildbookiarepository.azureedge.net')


def _test_viz_image(img_fpath):
    # Read image
    img = cv2.imread(img_fpath)
    tau = np.pi * 2  # References: tauday.com
    # Create figure
    fig = df2.figure(fnum=42, pnum=(1, 1, 1))
    # Clear figure
    fig.clf()
    # Build parameters
    bbox_list = [dummy_bbox(img), dummy_bbox(img, (-0.25, -0.25), 0.1)]
    showkw = {
        'title': 'test axis title',
        # The list of bounding boxes to be drawn on the image
        'bbox_list': bbox_list,
        'theta_list': [tau * 0.7, tau * 0.9],
        'sel_list': [True, False],
        'label_list': ['test label', 'lbl2'],
    }
    # Print the keyword arguments to illustrate their format
    print('showkw = ' + utool.repr2(showkw))
    # Display the image in figure-num 42, using a 1x1 axis grid in the first
    # axis. Pass showkw as keyword arguments.
    viz_image2.show_image(img, fnum=42, pnum=(1, 1, 1), **showkw)
    df2.set_figtitle('Test figure title')


if __name__ == '__main__':
    TEST_IMAGES_URL = f'{WILDBOOK_IA_MODELS_BASE}/data/testdata.zip'
    test_image_dir = utool.grab_zipped_url(TEST_IMAGES_URL, appname='utool')
    imgpaths = utool.list_images(
        test_image_dir, fullpath=True, recursive=False
    )  # test image paths
    # Get one image filepath to load and display
    img_fpath = imgpaths[0]
    # Run Test
    _test_viz_image(img_fpath)
    # Magic exec which displays or puts you into IPython with --cmd flag
    exec(df2.present())
