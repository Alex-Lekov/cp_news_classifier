# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kattana_news']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'kattana-news',
    'version': '21.3.16',
    'description': 'Model news classification',
    'long_description': None,
    'author': 'Alex-Lekov',
    'author_email': '61644712+Alex-Lekov@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

