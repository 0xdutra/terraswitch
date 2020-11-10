from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='terraswitch',
    author="Gabriel Dutra",
    author_email="0xdutra@gmail.com",
    version='1.1.0',
    description="Teraswitch is a tool for management terraform versions.",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xdutra/terraswitch",
    platforms=["any"],
    packages=['terraswitch'],
    package_dir={"terraswitch": "terraswitch"},
    entry_points={
        "console_scripts": ["terraswitch = terraswitch.__main__:main"]
    },
    keywords=["Terraform", "versions", "hashicorp"],
    install_requires=[
        "beautifulsoup4", "certifi", "chardet", "click", "idna", "lxml",
        "requests", "soupsieve", "urllib3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Email"
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
