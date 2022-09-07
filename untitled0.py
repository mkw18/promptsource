# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:13:02 2022

@author: mkw
"""

import yaml
import typing

class Loader(yaml.SafeLoader):
    pass

class Tagged(typing.NamedTuple):
    tag: str
    value: object
    
def construct_undefined(loader, node):
    if isinstance(node, yaml.nodes.ScalarNode):
        value = loader.construct_scalar(node)
    elif isinstance(node, yaml.nodes.SequenceNode):
        value = loader.construct_sequence(node)
    elif isinstance(node, yaml.nodes.MappingNode):
        value = loader.construct_mapping(node)
    else:
        assert False, f"unexpected node: {node!r}"
    return Tagged(node.tag, value)

Loader.add_constructor(None, construct_undefined)
tmpl = yaml.load(open("promptsource/templates/gigaword/nl/templates.yaml"), Loader=Loader)
