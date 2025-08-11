from setuptools import setup, find_packages

setup(
    name='addNum_Ranjit',
    version='1.0.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'pandas>=1.1.0',
    ],
    author='Ranjit Maity',
    author_email='ranjitmaity95@gmail.com',
    description='A description of your package',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)