from setuptools import setup, find_packages

setup(
    name="cli_tool_for_todoist",
    version="0.3",
    description="A CLI tool for managing Todoist tasks",
    author="Anshuman Agrawal",
    author_email="asquare567@gmail.com",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "todo=todoist_cli.cli:main",  # Main entry point only
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
