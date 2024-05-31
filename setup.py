from setuptools import setup


requirements = ["requests"]


long_description = open("README.rst").read()


setup(
    name="shinypony",
    version=version,
    author="eevelweezel",
    author_email="eevel.weezel@gmail.com",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    description="My Shiny Happy Contrived Packaging Example Project",
    license="Creative Commons",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Framework :: AsyncIO",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development",
        "Framework :: AsyncIO",
    ],
    url="https://github.com/eevelweezel/sparklepony",
    platforms=["any"],
    packages=["sparklepony"],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=requirements,
)
