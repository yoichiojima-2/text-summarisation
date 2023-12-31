from argparse import ArgumentParser
from .main import main

def entrypoint():
    parser = ArgumentParser()
    parser.add_argument("--target", "-t", type=str)
    args = parser.parse_args()

    main(args.target)
