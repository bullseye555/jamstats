from setuptools import setup, find_packages

setup(
    name='jamstats',
    version='0.1.2',    
    description='Data processing, stats and plots on roller derby scoreboard JSON files',
    author='Damon May',
    package_dir={"":"src"},
    packages=find_packages('src', exclude=['test']),
    scripts=['bin/jamstats-plot-pdf', 'bin/jamstats-convert-tsv'],
    install_requires=['pandas>=1.3.4', 'seaborn>=0.11.2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Source': 'https://github.com/dhmay/jamstats',
    },
)

