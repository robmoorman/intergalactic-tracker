from setuptools import find_packages, setup


setup(
    name='intergalactic-tracker',
    package_dir={
        '': 'src'
    },
    packages=find_packages('src'),
    include_package_data=True
)
