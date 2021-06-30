#!/usr/bin/python3

# Copyright 2021 Google LLC
# Copyright 2021 Fraunhofer FKIE
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""An example of fuzzing in Python."""

import struct
import sys

import atheris

with atheris.instrument(include=["example_library"]):
  from example_library import CodeBeingFuzzed


def TestOneInput(data):
  """The entry point for our fuzzer.

  This is a callback that will be repeatedly invoked with different arguments
  after Fuzz() is called.
  We translate the arbitrary byte string into a format our function being fuzzed
  can understand, then call it.

  Args:
    data: Bytestring coming from the fuzzing engine.
  """
  if len(data) != 4:
    return  # Input must be 4 byte integer.

  number, = struct.unpack('<I', data)
  CodeBeingFuzzed(number)


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
