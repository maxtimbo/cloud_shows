import argparse
import logging

def Main():
    parser = argparse.ArgumentParser(description=helptext.HELPTEXT)
    group = parser.add_mutually_exclusive_group()
    subparsers = parser.add_subparsers(dest="subparser")

    group.add_argument('--new_config', help="create a new blank config file")
    group.add_argument('--setup', help="instructions to configure or modify config file", action="store_true")

    normal_run = subparsers.add_parser("run")
    normal_run.add_argument('-c', '--config', help="specify config file")
    normal_run.add_argument('-v', '--verbose', help='verbose output', action='store_true')
    normal_run.add_argument('-e', '--email', help='enable email notifications', action='store_true')

    validate_config = subparsers.add_parser("validate")
    validate_config.add_argument('-c', '--config', help='specify config file to validate')
    validate_config.add_argument('-e', '--email', help='validate email configuration', action='store_true')

    args = parser.parse_args()

if __name__ == "__main__":
    Main()
