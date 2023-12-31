from setuptools import setup, find_packages

setup(
    name="text_summarisation",
    version="2023.10",
    packages=find_packages(),
    install_requires=["openai", "tqdm", "tenacity"],
    entry_points={"console_scripts": ["text-summarisation = text_summarisation.cli:entrypoint"]},
)
