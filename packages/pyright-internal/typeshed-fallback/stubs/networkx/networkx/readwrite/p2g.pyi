from networkx.utils.backends import _dispatchable

def write_p2g(G, path, encoding: str = "utf-8") -> None: ...
@_dispatchable
def read_p2g(path, encoding: str = "utf-8"): ...
@_dispatchable
def parse_p2g(lines): ...
