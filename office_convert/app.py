#
# pl-office-convert ds ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
import os
from os import path
import shutil
from pathlib import Path
from glob import iglob
import logging

import pandas as pd
from tqdm import tqdm

Gstr_title = r"""
 _____  __  __ _           ______ _ _        _____                           _
|  _  |/ _|/ _(_)          |  ___(_) |      /  __ \                         | |
| | | | |_| |_ _  ___ ___  | |_   _| | ___  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __
| | | |  _|  _| |/ __/ _ \ |  _| | | |/ _ \ | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
\ \_/ / | | | | | (_|  __/ | |   | | |  __/ | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |
 \___/|_| |_| |_|\___\___| \_|   |_|_|\___|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|                            
"""

logger = logging.getLogger(__name__)


class OfficeFileConverter(ChrisApp):
    """
    A ChRIS ds plugin for using regular expressions to perform find-and-replace.
    """
    PACKAGE                 = __package__
    TITLE                   = 'Office File Converter'
    CATEGORY                = 'Format'
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 1000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 200  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    SPREADSHEET_EXTENSIONS = ['xlsx', 'xls', 'ods']

    def define_parameters(self):
        # this is a future spec
        # https://github.com/FNNDSC/chrisapp/issues/6
        # self.add_argument(
        #     '-p', '--inputPathFilter',
        #     dest='inputPathFilter',
        #     help='selection (glob) for which files to evaluate.',
        #     default='**',
        #     type=str,
        #     optional=True
        # )
        pass

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print(f'Version: {self.get_version()}')

        # stay in the inputdir as working directory,
        # wite to outputdir by absolute paths
        outputdir = Path(options.outputdir).resolve()
        os.chdir(options.inputdir)

        # not the perfect solution for collecting list of files
        # to process, but it's simple and resolves immediately
        # so tqdm can provide a progress bar.

        input_files = [
            fname for fname in iglob('**', recursive=True)
            if path.isfile(fname)
        ]

        for fname in tqdm(input_files):
            # if files were in subdirectories, we must recreate
            # those subdirectories in the output folder
            parentdir = path.dirname(fname)
            if parentdir:
                os.makedirs(outputdir / parentdir, exist_ok=True)

            if self.is_spreadsheet(fname):
                output_fname = outputdir / self.sub_extension(fname)
                if output_fname.exists():
                    logger.warning('will overwrite %s', output_fname)

                # convert file type
                df = pd.read_excel(fname)
                df.to_csv(output_fname, index=False)
            else:
                shutil.copy(fname, outputdir / fname)

    @staticmethod
    def sub_extension(fname: str, ext='csv'):
        return fname[:fname.rindex('.')] + '.' + ext

    @classmethod
    def is_spreadsheet(cls, fname: str) -> bool:
        for e in cls.SPREADSHEET_EXTENSIONS:
            if fname.endswith(e):
                return True
        return False

    def show_man_page(self):
        self.print_help()
