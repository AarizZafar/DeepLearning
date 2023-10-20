import setuptools

with open('README.md', 'r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME          = 'DeepLearning'
AUTHOR_USER_NAME   = 'AarizZafar'
SRC_REPO           = 'cnnClassifier'
AUTHOR_EMAIL       = 'aariz.zafar01@gmail.com'

setuptools.setup(
    name                           = SRC_REPO,
    version                        = __version__,
    author                         = AUTHOR_USER_NAME,
    aunthor_email                  = AUTHOR_EMAIL,
    description                    = 'SMALL PYTHON PACKAGE FOR CNN APP',
    long_description               = long_description,
    long_description_content       = 'text/markdown',
    url                            = f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_url = {
                                    'Bug Tracker ' : f'https://github.com.{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir                    = {'' : 'src'},
    packages                       = setuptools.find_packages(where = 'src')
)