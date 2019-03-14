# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from paddle_hub.tools.logger import logger
from paddle_hub.commands.base_command import BaseCommand
from paddle_hub.tools import utils
from paddle_hub.tools.downloader import default_downloader
from paddle_hub.module.manager import default_manager


class DownloadCommand(BaseCommand):
    def __init__(self):
        super(DownloadCommand, self).__init__()
        # yapf: disable
        self.add_arg('--output_path',  str,  ".",   "path to save the module, default in current directory" )
        self.add_arg('--uncompress',   bool, False,  "uncompress the download package or not" )
        # yapf: enable

    def help(self):
        self.parser.print_help()

    def exec(self, argv):
        module_name = argv[1]
        self.args = self.parser.parse_args(argv[2:])
        if not self.args.output_path:
            self.args.output_path = "."
        utils.check_path(self.args.output_path)

        url = default_downloader.get_module_url(module_name)
        assert url, "can't found module %s" % module_name

        self.print_args()
        if self.args.uncompress:
            default_downloader.download_file_and_uncompress(
                url=url, save_path=self.args.output_path)
        else:
            default_downloader.download_file(
                url=url, save_path=self.args.output_path)


command = DownloadCommand.instance()