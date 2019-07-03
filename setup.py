from setuptools import setup, find_packages

requirements = [
    'pyyaml',
    'scapy',
    'netfilterqueue'
]

setup(
    name='spam-vnf',
    version='0.0.1',
    description='Spam Filtering VNF',
    url='https://github.com/qarawlus/fi-vnf',
    author='VNF Devs',
    author_email='qarawlus@mail.upb.de',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'spam-vnf=spamvnf.main:main',
        ],
    },
)
