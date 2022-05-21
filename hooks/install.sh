#
#  MAKINAROCKS CONFIDENTIAL
#  ________________________
#
#  [2017] - [2020] MakinaRocks Co., Ltd.
#  All Rights Reserved.
#
#  NOTICE:  All information contained herein is, and remains
#  the property of MakinaRocks Co., Ltd. and its suppliers, if any.
#  The intellectual and technical concepts contained herein are
#  proprietary to MakinaRocks Co., Ltd. and its suppliers and may be
#  covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law. Dissemination
#  of this information or reproduction of this material is
#  strictly forbidden unless prior written permission is obtained
#  from MakinaRocks Co., Ltd.
#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)

# Install pre-commit
rm -f $REPO_ROOT/.git/hooks/pre-commit && rm -f $REPO_ROOT/.git/hooks/pre-commit.legacy
pip install pre-commit
cd $REPO_ROOT && pre-commit install

# Add and update all submodules
python hooks/add_submodules.py $REPO_ROOT
git submodule init
git submodule update --recursive

# ipynb diff
pip install nbdime
nbdime config-git --enable
git config diff.jupyternotebook.command "git-nbdiffdriver diff -s"

# track ipynb with lfs
git lfs install
git config diff.lfs.textconv cat
