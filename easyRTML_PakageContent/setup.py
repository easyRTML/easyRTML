from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='easyRTML',
    version='1.5',
    description='A package for signal classification and deployment in any microcontroller board with no expertise required.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Aryan Jadhav',
    author_email='easiestrtml@gmail.com',
    url='https://github.com/yourusername/easyRTML',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'xgboost',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'tqdm',
        'pyserial', 
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
)
