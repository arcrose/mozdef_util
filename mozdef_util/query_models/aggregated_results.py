#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2017 Mozilla Corporation


def AggregatedResults(input_results):
    converted_results = {
        'meta': {
            'timed_out': input_results.timed_out
        },
        'hits': [],
        'aggregations': {}
    }
    for hit in input_results.hits:
        hit_dict = {
            '_id': hit.meta.id,
            '_index': hit.meta.index,
            '_score': hit.meta.score,
            '_source': hit.to_dict()
        }
        converted_results['hits'].append(hit_dict)

    for agg_name, aggregation in input_results.aggregations.to_dict().items():
        aggregation_dict = {
            'terms': []
        }
        for bucket in aggregation['buckets']:
            aggregation_dict['terms'].append({'count': bucket['doc_count'], 'key': bucket['key']})

        converted_results['aggregations'][agg_name] = aggregation_dict

    return converted_results
