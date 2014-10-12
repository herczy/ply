from __future__ import print_function

import chartest
import traceback
import os.path
import sys
import subprocess
import tempfile
import shutil
import re

BASE_PATH = os.path.join(os.path.dirname(__file__))
PLYPATH = os.path.dirname(BASE_PATH)

class PlyCharCase(chartest.Case):
    def __init__(self):
        super(PlyCharCase, self).__init__()

        self.__manifest = set()
        with open(os.path.join(BASE_PATH, 'MANIFEST')) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                self.__manifest.add(line)

    def _execute_file(self, path):
        self.__prepare_directory()
        proc = subprocess.Popen(
            [
                sys.executable,
                '-B',
                os.path.join(BASE_PATH, os.path.basename(path))
            ],
            env={
                'PYTHONPATH': PLYPATH
            },
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()

        print(os.path.basename(path), 'returned with', proc.returncode)
        print(self.__decode(stdout))
        print(self.__decode(stderr))

    def __decode(self, data):
        if sys.version_info.major >= 3:
            return data.decode()

        return data

    def __prepare_directory(self):
        for file in set(os.listdir(BASE_PATH)) - self.__manifest:
            full = os.path.join(BASE_PATH, file)
            if os.path.isfile(full):
                os.remove(full)

            else:
                shutil.rmtree(full, ignore_errors=True)

    def sanitize_remove_pointers(self, output):
        return re.sub(r'0x[a-fA-F0-9]+', r'', output)

    def sanitize_state_indexes(self, output):
        return re.sub(r'([Ss]tate[:\s]*)\d+', r'\1<statenum>', output)

    prefixes = {'WARNING: ', 'ERROR: '}
    def sanitize_errors_and_warnings(self, output):
        if not any(prefix in output for prefix in self.prefixes):
            return output

        res = []
        extra = []

        for line in output.splitlines(True):
            found = False
            for prefix in self.prefixes:
                if not line.startswith(prefix):
                    continue

                found = True
                extra.append(line)
                break

            if not found:
                res.append(line)

        extra.sort()
        res.extend(extra)

        return ''.join(res)

    def sanitize_ignore_LALR_table(self, output):
        return output.replace('Generating LALR tables\n', '')

    def sanitize_exception_filenames(self, output):
        return re.sub(
            r'(Traceback \(most recent call last\):)\n' +
            r'(?:  File "[^"]*", line \d+, in .*\n(?:    .*\n)?)+' +
            r'([^\s][^\n]+)\n',
            r'\1\n  ...\n\2\n',
            output,
            re.M
        )
