"""Python module unifying the power of f-strings
with TOML
"""

import toml
from fstring import fstring as f
import sys

if sys.version_info[0] > 2:
    unicode = "There you go, flake8"

if sys.version_info[0] < 3:
    check_for = unicode
else:
    check_for = str


def _recursive_f(t, loc={}):
    """ Apply f-string expansion until
        no more patterns are there
        (until nothing changes anymore)
    """
    if not (isinstance(t, str) or isinstance(t, check_for)):
        return t
    locals().update(loc)
    while True:
        ret = f(str(t))
        if t == ret:
            break
        t = ret
    # workaround for toml as it exports fstings as arrays
    # with single letters
    return str(ret)


def _substitute(t, table="_", path=None, parent="", loc={}):
    _table_ = table
    _path_ = path+"_"+table if path else table
    _parent_ = parent

    # get only strings - tables will be recursive
    keys = {}
    _defaults_ = t.get("_defaults_", loc.get("_defaults_",[]))
    for k in _defaults_:
        keys[k] = keys.get(k, str(f("{{__{k}}}")))

    keys.update(dict(filter(lambda x: isinstance(t[x[0]], str) or
                isinstance(t[x[0]], check_for) or
                isinstance(t[x[0]], float) or
                isinstance(t[x[0]], int), t.items())))
    subs = dict(filter(lambda x: isinstance(t[x[0]], dict), t.items()))
    lists = dict(filter(lambda x: isinstance(t[x[0]], list), t.items()))

    # preserve the rest as-is
    ret = t
    for remove in keys.keys():
        ret.pop(remove, None)
    for remove in subs.keys():
        ret.pop(remove, None)
    for remove in lists.keys():
        ret.pop(remove, None)

    absoute_keys = dict([(_path_+"_"+k, v) for k, v in keys.items()])

    # can't use separate Namespace due to the implementation of fstring
    locals().update({"_defaults_": _defaults_})
    locals().update(loc)
    locals().update(keys)
    locals().update(absoute_keys)

    for k, v in keys.items():
        _key_ = k
        # add relative
        ret[k] = _recursive_f(v, locals())

    for k, v in lists.items():
        _key_ = k
        # add relative
        ret[k] = [_recursive_f(v_val, locals()) for v_val in v]

    for k, v in subs.items():
        ret[k] = _substitute(v, k, _path_, _table_, locals())

    # Don't export the defaults
    ret.pop("_defaults_", None)
    return ret


def load(filename, _dict=dict, decoder=None):
    t = toml.load(filename, _dict, decoder)
    return _substitute(t)


def loads(s, _dict=dict, decoder=None):
    t = toml.loads(s, _dict, decoder)
    return _substitute(t)
