# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Example Connection Command

Make sure you can authenticate before running this command.

For example:
    python -m examples.connection
"""

import sys

from examples import common
from openstack import connection


def make_connection(opts):
    return connection.from_config(opts)


def run_connection(opts):
    conn = make_connection(opts)
    print("Connection: %s" % conn)
    for resource in conn.compute.flavors():
        print(resource)
    return


if __name__ == "__main__":
    opts = common.setup()
    sys.exit(common.main(opts, run_connection))
