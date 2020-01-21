#!/usr/bin/env python
#
# Copyright 2017 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from fastavro.schema import parse_schema, load_schema


def loads(schema):
    """
    Returns an Avro Schema from a string

    :param str schema: Schema string to be parsed
    :returns: Parsed Avro Schema
    :rtype: Dict
    """
    """ Parse a schema given a schema string """
    return parse_schema(schema)


def load(avsc):
    """
    Returns an Avro Schema from a file path.

    :param str avsc: Path to Avro Schema file
    :returns: Parsed Schema
    :rtype: dict
    """
    """ Parse a schema from a file path """
    return load_schema(fp)
