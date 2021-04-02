from omg.cmd.desc.from_yaml import from_yaml

from omg.cmd.desc.ev_out import ev_out
from omg.cmd.desc.node_out import node_out
from omg.cmd.desc.pod_out import pod_out


# This map and function normalizes/standarizes the different names of object/resources types
# Also returns the function that handles get,describe and output of this object type
# This is how the top level get_main function knows which objects we can handle and how.
# returns None if not an object type that we can't handle


map = [


    {   'type': 'event','aliases': ['events', 'ev'],'need_ns': True,
        'desc_func': from_yaml, 'descout_func': ev_out,
        'yaml_loc': 'namespaces/%s/core/events.yaml' },
        
    {   'type': 'node','aliases': ['nodes'],'need_ns': False,
        'desc_func': from_yaml, 'descout_func': node_out,
        'yaml_loc': 'cluster-scoped-resources/core/nodes' },
        # When yaml_loc is a dir like in this case, we scan *.yaml files in it.

    {   'type': 'pod','aliases': ['pods', 'po'],'need_ns': True,
        'desc_func': from_yaml, 'descout_func': pod_out,
        'yaml_loc': 'namespaces/%s/core/pods.yaml' },
]


def map_res(t):
    if t is not None:
        for x in map:
            # match the input with type: or alias (without case)
            if t.lower() == x['type'].lower() or t.lower() in [y.lower() for y in x['aliases'] ]:
                return x
    return None
