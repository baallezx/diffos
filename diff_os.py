"""
A library for doing diffs on different computers.

This is useful for checking all different process
versions, os versions, etc.
which should help on debugging issues.
"""

"""
The MIT License (MIT)

Copyright (c) <2014> <alex balzer alex.balzer@hp.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

import os
import sys

__version__ = "0.1.0"
__author__ = "alex balzer alex.balzer@hp.com"

class Box(object):
  """
  A Box object represents a single machine or node
  it holds all of its version information
  
  Ex. 
  OS = {"type":"Ubuntu" , "version":"14.04"}
  RVM = {"version":"1.25.31" , "paths":["/home/user/.rvm/...","/tmp/rvm/craziness"]}
  RUBY = { ... }
  GEMS = { ... } 
  VAGRANT = { ... }
  VIRTUALBOX = { ... }
  """
  def __init__(self):
    self.OS = self.get_os()
    self.RVM = self.get_rvm()
    self.RUBY = self.get_ruby()
    self.GEMS = self.get_gems()
    self.VAGRANT = self.get_vagrant()
    self.VIRTUALBOX = self.get_virtualbox()

  def get_os(self):
    """ return all the information about the machines operating system. """
    chk = "cat /etc/*-release" or "lsb_release -a"
    result = os.popen3(chk)
    #TODO: get the correct reults from os.popen3(chk). then parse the results to a dictionary object as described above.
    return result

  def get_rvm(self):
    pass

  def get_ruby(self):
    pass

  def get_gems(self):
    pass

  def get_vagrant(self):
    pass

  def get_virtualbox(self):
    pass
