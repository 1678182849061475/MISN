from setuptools import setup, find_packages

setup(
    name="enchanted_forest",
    version="0.1",
    author="Your Name",
    author_email="youremail@example.com",
    packages=find_packages(),
    install_requires=[
        'pygame>=2.0',
    ],
    entry_points={
        'console_scripts': [
            'enchanted_forest=main:main',
        ],
    },
)
