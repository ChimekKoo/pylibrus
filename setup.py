import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pylibrus",
    version="0.0.0",
    author="Joachim Kołodziejski",
    author_email="kolodziejski.joachim@gmail.com",
    description="Librus (polish school e-register) unofficial API client written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChimekKoo/pylibrus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Source': 'https://github.com/ChimekKoo/pylibrus',
        'Bug Tracker': 'https://github.com/ChimekKoo/pylibrus/issues',
    },
    install_requires = [
        'requests>=2.0.0'
    ]
)
