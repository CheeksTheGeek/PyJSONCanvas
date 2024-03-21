# validate.py


# second param for no exceptions only return bool
def validate_node(node) -> bool:
    from .models import (
        GenericNode,
        NodeType,
        GroupNodeBackgroundStyle,
        GroupNode,
        TextNode,
        FileNode,
        LinkNode,
        Color,
    )
    from .exceptions import InvalidNodeTypeError, InvalidNodeAttributeError

    """Validates  the node, and if is a inherited class from Node, then checks those special attributes."""
    if not isinstance(node, GenericNode):
        raise InvalidNodeTypeError("Node is not a valid instance of Node.")

    if not isinstance(node.id, str):
        raise InvalidNodeAttributeError("Node ID is invalid or missing.")

    if not isinstance(node.type, NodeType):
        raise InvalidNodeTypeError("Node type is invalid or missing.")

    if not isinstance(node.x, int):
        raise InvalidNodeAttributeError("Node x is invalid or missing.")

    if not isinstance(node.y, int):
        raise InvalidNodeAttributeError("Node y is invalid or missing.")

    if not isinstance(node.width, int):
        raise InvalidNodeAttributeError("Node width is invalid or missing.")

    if not isinstance(node.height, int):
        raise InvalidNodeAttributeError("Node height is invalid or missing.")

    if node.color is not None and not isinstance(node.color, Color):
        raise InvalidNodeAttributeError("Node color is invalid or missing.")

    if isinstance(node, TextNode) and not isinstance(node.text, str):
        raise InvalidNodeAttributeError("TextNode text is invalid or missing.")

    if isinstance(node, FileNode):
        if not isinstance(node.file, str):
            raise InvalidNodeAttributeError("FileNode file is invalid or missing.")
        if node.subpath is not None and not isinstance(node.subpath, str):
            raise InvalidNodeAttributeError("FileNode subpath is invalid or missing.")

    if isinstance(node, LinkNode) and not isinstance(node.url, str):
        raise InvalidNodeAttributeError("LinkNode url is invalid or missing.")

    if isinstance(node, GroupNode):
        if node.label is not None and not isinstance(node.label, str):
            raise InvalidNodeAttributeError("GroupNode label is invalid or missing.")

        if node.background is not None and not isinstance(node.background, str):
            raise InvalidNodeAttributeError(
                "GroupNode background is invalid or missing."
            )

        if node.backgroundStyle is not None and not isinstance(
            node.backgroundStyle, GroupNodeBackgroundStyle
        ):
            raise InvalidNodeAttributeError(
                "GroupNode backgroundStyle is invalid or missing."
            )

    return True


def validate_edge(edge) -> bool:
    from .models import (
        Edge,
        EdgesFromEndValue,
        EdgesFromSideValue,
        EdgesToEndValue,
        EdgesToSideValue,
        Color,
    )
    from .exceptions import InvalidEdgeAttributeError, InvalidEdgeConnectionError

    if not isinstance(edge, Edge):
        raise InvalidEdgeAttributeError("Edge is not a valid instance of Edge.")

    if not isinstance(edge.id, str):
        raise InvalidEdgeAttributeError("Edge ID is invalid or missing.")

    if not isinstance(edge.fromNode, str):
        raise InvalidEdgeConnectionError("Edge fromNode is invalid or missing.")

    if edge.fromSide is not None and not isinstance(edge.fromSide, EdgesFromSideValue):
        raise InvalidEdgeAttributeError("Edge fromSide is invalid or missing.")

    if edge.fromEnd is not None and not isinstance(edge.fromEnd, EdgesFromEndValue):
        raise InvalidEdgeAttributeError("Edge fromEnd is invalid or missing.")

    if not isinstance(edge.toNode, str):
        raise InvalidEdgeConnectionError("Edge toNode is invalid or missing.")

    if edge.toSide is not None and not isinstance(edge.toSide, EdgesToSideValue):
        raise InvalidEdgeAttributeError("Edge toSide is invalid or missing.")

    if edge.toEnd is not None and not isinstance(edge.toEnd, EdgesToEndValue):
        raise InvalidEdgeAttributeError("Edge toEnd is invalid or missing.")

    if edge.color is not None and not isinstance(edge.color, Color):
        raise InvalidEdgeAttributeError("Edge color is invalid or missing.")

    if edge.label is not None and not isinstance(edge.label, str):
        raise InvalidEdgeAttributeError("Edge label is invalid or missing.")

    return True
