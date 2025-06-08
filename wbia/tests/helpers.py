# -*- coding: utf-8 -*-
import os

import utool as ut

__all__ = ('get_testdata_dir',)

WILDBOOK_IA_MODELS_BASE = os.getenv('WILDBOOK_IA_MODELS_BASE', 'https://wildbookiarepository.azureedge.net')


def get_testdata_dir(ensure=True, key='testdb1'):
    """
    Gets test img directory and downloads it if it doesn't exist
    """
    testdata_map = {
        # 'testdb1': f'{WILDBOOK_IA_MODELS_BASE}/public/data/testdata.zip'}
        'testdb1': f'{WILDBOOK_IA_MODELS_BASE}/data/testdata.zip',
    }
    zipped_testdata_url = testdata_map[key]
    testdata_dir = ut.grab_zipped_url(zipped_testdata_url, ensure=ensure)
    return testdata_dir
