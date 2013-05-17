# coding: utf-8

try:
    from lxml import etree
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
            except ImportError:
                import elementtree.ElementTree as etree
                # raises ImportError


def create_element_recursively(parent, path):
    nodes = path.split('/')
    node = parent
    for n_str in nodes:
        n = node.find(n_str)
        if n is None:
            node = etree.SubElement(node, n_str)
        else:
            node = n
    return node
