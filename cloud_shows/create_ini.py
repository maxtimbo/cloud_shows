import configparser
from pathlib import Path

def new_ini(filename):
    cwd = Path.cwd()
    path = cwd.joinpath(filename)
    if Path.is_file(path):
        print(f'{filename} already exists')
    else:
        config = configparser.ConfigParser()
        config['directories'] = {
                'remote': '',
                'download': '',
                'destination': '',
                'logdir': ''
        }

        config['metadata'] = {
                'artist': '',
                'title': ''
        }

        config['email'] = {
                'mailhost': '',
                'port': '587',
                'from_name': '',
                'subject': '',
                'recipients': '',
                'username': '',
                'password': '',
                'secure': ''
        }

        with open(filename, 'w') as file_obj:
            config.write(file_obj)

        print(f'{path} created')
