from grammator import parser, Token

def parse_simple(tokens, result):
    if not tokens or tokens[-1][0] != "ENDL":
        tokens += [('ENDL', '\n')]
    assert parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens + [('ENDMARKER', ''), None]))) == (result + [{"type": "endl", "value": "\n", "space": "", "indent": ""}])

def parse_multi(tokens, result):
    assert parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens + [('ENDMARKER', ''), None]))) == result

def _node(typeu, value, **kwargs):
    if kwargs is not None:
        to_return = {"type": typeu, "value": value}
        to_return.update(kwargs)
        return to_return
    return {"type": typeu, "value": value}

def dotted_as_name(value, before_space="", after_space="", as_=False, target=None):
    return {
        "type": "dotted_as_name",
        "value": value,
        "before_space": before_space,
        "after_space": after_space,
        "as_": as_,
        "target": target,
    }

def from_import(value, targets, before_space=" ", middle_space=" ", after_space=" ", **kwargs):
    return _node("from_import", value, targets=targets, before_space=before_space, middle_space=middle_space, after_space=after_space, **kwargs)

