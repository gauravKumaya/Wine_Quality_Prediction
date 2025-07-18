import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()
    

__version__ = "0.0.0"

REPO_NAME = "Wine_Qaulity_Prediction"
AUTHOR_USER_NAME = "gauravKumaya"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "gauravkumaya@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Trackers": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)