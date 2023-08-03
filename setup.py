from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="ARPZ",
    description="Its a small project demo for DVC working explanation for it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aqibrehmanpirzada/My-dvc-project.git",
    author_email="aqibrehmanpirzada75@gmail.com",
    packages=["src"],
    license="GNU",
    python_requires=">=3.8",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)
