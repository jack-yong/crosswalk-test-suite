#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import os
import sys
import commands
import shutil

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)


def setUp():
    global  XwalkPath, PackTools 

    PackTools = ConstPath +  "/../tools/crosswalk-app-tools/src/"

    XwalkPath = ConstPath + "/../tools/"
    if "crosswalk-app-tools" not in os.listdir(XwalkPath):
        print "Please check if the crosswalk-app-tools exists in " + ConstPath + "/../tools/"
        sys.exit(1)

def clear(pkg):
    try:
        shutil.rmtree(XwalkPath + pkg)
    except Exception,e:
        os.system("rm -rf " + XwalkPath + pkg + " &>/dev/null")

def create(self):
    setUp()
    os.chdir(XwalkPath)
    clear("org.xwalk.test")
    cmd = PackTools + "crosswalk-app create org.xwalk.test"
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(packstatus[0], 0)
    self.assertIn("org.xwalk.test", os.listdir(os.getcwd()))

def build(self, cmd):
    buildstatus = commands.getstatusoutput(cmd)
    self.assertEquals(buildstatus[0], 0)
    self.assertIn("pkg", os.listdir(XwalkPath + "org.xwalk.test"))
    os.chdir('pkg')
    self.assertIn("test.ipa", os.listdir(os.getcwd()))
