#
#  MAKINAROCKS CONFIDENTIAL
#  ________________________
#
#  [2017] - [2022] MakinaRocks Co., Ltd.
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
import re
from os import path

from setuptools import find_packages, setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def find_version(*file_path_parts):
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, *file_path_parts), "r") as fp:
        version_file_text = fp.read()

    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file_text,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name="project-template",
    version=find_version("src", "__init__.py"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    author="MakinaRocks",
    author_email="devops@makinarocks.ai",
    description="Projecte teamplate for MakinaRocks",
    keywords="project template",
    url="https://github.com/makinarocks/platorm-project-template",
    project_urls={
        "Documentation": "https://github.com/makinarocks/platorm-project-template",
        "Source Code": "https://github.com/makinarocks/platorm-project-template",
    },
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
