#
# Copyright (c) 2012 Citrix Systems, Inc.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import arguments
import connect

def add_subparser(subparsers):
    description = """Lock a VM instance on a device."""

    parser = subparsers.add_parser("lock-vm-instance",
                                   help="lock VM instance",
                                   description=description)

    arguments.add_output_args(parser, suppress=True)

    parser.add_argument("vm_instance",
                        metavar="VM_INSTANCE_UUID",
                        action=arguments.StoreSingleNonEmptyValue,
                        help="VM instance uuid")

    parser.set_defaults(func=_run)

def _run(args, config):
    connection = connect.connect(args, config)
    cursor = connection.cursor()

    cursor.callproc("sync_admin.lock_vm_instance",
                    keywordParameters={
                        "vm_instance_uuid": args.vm_instance})
