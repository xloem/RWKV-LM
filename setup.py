from setuptools import setup

setup(
    name = 'RWKV-LM',
    version = '0.1.0',
    description = 'A RNN with transformer-level performance.',
    long_decription = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/BlinkDL/RWKV-LM',
    keywords = [
        'NLP',
        'deep learning',
        'deep', 'learning',
        'transformer', 'rnn',
        'pytorch', 'GPT-2'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    packages = [
        'rwkv_lm'
    ],
    package_dir = {
        'rwkv_lm': 'src'
    },
    install_requires = [
        'torch'
    ]
)
