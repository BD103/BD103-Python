import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BD103",
    version="0.1.5",
    author="BD103",
    author_email="dont@stalk.me",
    description="Assorted Developer Functions by BD103",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bd103.github.io",
    project_urls={
      "Documentation": "https://github.com/BD103/Package/wiki",
      "Repository": "https://github.com/BD103/Package",
      "Issues": "https://github.com/BD103/Package/issues"
    },
    packages=setuptools.find_packages(),
    classifiers=[
				"Development Status :: 4 - Beta",
				"Intended Audience :: Developers",
				"Natural Language :: English",
        "Programming Language :: Python :: 3.8",
				"Programming Language :: Python :: 3 :: Only",
				"Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)