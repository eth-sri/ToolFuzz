from typing import Any


class TaintStr(str):
    separators = set()

    def __new__(cls, value, *args, **kw):
        """Create a tstr() instance. Used internally."""
        return str.__new__(cls, value)

    def __init__(self, value: Any, taint: Any = None, **kwargs) -> None:
        """Constructor.
        `value` is the string value the `tstr` object is to be constructed from.
        `taint` is an (optional) taint to be propagated to derived strings."""
        self.taint: Any = taint

    def create(self, s):
        return TaintStr(s, taint=self.taint)

    def clear(self):
        self.taint = None
        return self.taint

    def __repr__(self):
        """Return a representation."""
        return TaintStr(str.__repr__(self), taint=self.taint)

    def __str__(self) -> str:
        """Convert to string"""
        return str.__str__(self)

    def split(self, sep=' ', maxsplit=-1):
        TaintStr.separators.add(sep)
        return super().split(sep, maxsplit)


class TaintDict(dict):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    acc_keys = []

    def __init__(self, *args, **kwargs):
        TaintDict.acc_keys = []
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        TaintDict.acc_keys.append(key)
        return super().__getitem__(key)

    def get(self, __key):
        return self.__getitem__(__key)

    def __setitem__(self, key, value):
        TaintDict.acc_keys.append(key)
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        TaintDict.acc_keys.append(key)
        return super().__delitem__(key)

    def __contains__(self, key):
        TaintDict.acc_keys.append(key)
        return super().__contains__(key)
