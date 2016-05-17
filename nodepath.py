#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Functions for working with tree data."""

import numpy
import pandas


__authors__ = 'Markus Englund'
__license__ = 'MIT'
__version__ = '0.1.0'


def get_node_data(series, sep='|'):
    """
    Get the name, rank (category), child-path and parent-path
    for an enumerated path."""
    dropped = series.dropna()
    name = dropped.tail(1)
    result = pandas.Series(
        {
            'name': name[0],
            'category': name.index[0],
            'full_path': sep.join(dropped),
            'parent_path': sep.join(dropped.dropna()[:-1])
        }, index=['name', 'category', 'full_path', 'parent_path'])
    return result


def expand_nodes(frame):
    """Get the full tree with an individual node (row) for each rank."""
    all_nodes_list = []
    num_columns = len(frame.columns)
    for i in range(num_columns):
        distinct_nodes = frame.iloc[:, :num_columns-i].drop_duplicates()
        all_nodes_list.append(distinct_nodes)
    all_nodes = pandas.concat(all_nodes_list)[frame.columns]
    all_distinct_nodes = all_nodes.drop_duplicates()
    sorted_nodes = all_distinct_nodes.sort_values(
        by=list(frame.columns), na_position='first').reset_index(drop=True)
    return sorted_nodes


def get_adjacency_frame(frame, sep='|'):
    """
    Get the name, rank (category), child-path and parent-path
    for each node.
    """
    parent_child_frame = frame.apply(
        lambda x: get_node_data(x, sep=sep), axis=1)
    parent_child_frame.replace('', numpy.nan, inplace=True)
    return parent_child_frame
