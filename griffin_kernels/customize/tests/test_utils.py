# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------

#
# Licensed under the terms of the MIT License
# (see griffin_kernels/__init__.py for details)
# -----------------------------------------------------------------------------

import os
import sys

from griffin_kernels.customize.utils import create_pathlist


def test_user_sitepackages_in_pathlist():
    """Test that we include user site-packages in pathlist."""
    if sys.platform.startswith('linux'):
        user_path = 'local'
    elif (sys.platform == 'darwin' or sys.platform.startswith('freebsd')):
        user_path = os.path.expanduser('~/.local')
    else:
        user_path = 'Roaming'

    assert any([user_path in path for path in create_pathlist()])
