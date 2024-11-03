from setuptools import setup, find_packages

setup(
    name="cli_tool_for_todoist",
    version="0.1",
    description="A CLI tool for managing Todoist tasks",
    author="Anshuman Agrawal",
    author_email="asquare567@gmail.com",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "todo-add=todoist_cli.cli:main",
            "todo-delete=todoist_cli.cli:main",
            "todo-list=todoist_cli.cli:main",
            "todo-sync=todoist_cli.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
