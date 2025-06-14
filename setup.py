import setuptools

REQUIREMENTS = [
    "requests == 2.*",
]

setuptools.setup(
    name="github-actions-test",
    version="0.1.0",
    description="Test GitHub Actions.",
    url="http://github.com/Justintime50/github-actions-test",
    author="Justintime50",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
)
