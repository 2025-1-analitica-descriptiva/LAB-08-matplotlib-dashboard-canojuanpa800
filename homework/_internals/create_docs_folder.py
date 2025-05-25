import os


def create_docs_folder():
    if not os.path.exists("docs"):
        os.makedirs("docs")