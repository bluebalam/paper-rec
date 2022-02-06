from setuptools import setup, find_packages


setup(
    name='paper-rec',
    version='0.1',
    package_dir={"": "src"},
    packages=find_packages("src"),
    url='https://github.com/bluebalam/paper-rec',
    license='mit',
    author='bluebalam',
    author_email='ernesto@libreai.com',
    description='paper recommender'
)
