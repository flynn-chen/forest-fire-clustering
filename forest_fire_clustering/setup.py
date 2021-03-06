import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="forest-fire-clustering", # Replace with your own username
    version="0.0.3",
    author="Flynn Chen",
    author_email="zhanlinchen348@gmail.com",
    description="Clustering Method Inspired by Forest Fire Dynamics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flynn-chen/forest-fire-clustering.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy==1.18.1',
        'scipy==1.4.1',
        'scikit-learn==0.22.2.post1',
	'numba==0.53.1'
    ],
    python_requires='>=3.6',
)
