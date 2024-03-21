# encoder.py

from json import JSONEncoder

from .models import (
    NodeType,
    GroupNodeBackgroundStyle,
    EdgesFromEndValue,
    EdgesFromSideValue,
    EdgesToEndValue,
    EdgesToSideValue,
    Edge,
    GenericNode,
    TextNode,
    FileNode,
    LinkNode,
    GroupNode,
    Color,
)


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(
            obj,
            (
                NodeType,
                GroupNodeBackgroundStyle,
                EdgesFromEndValue,
                EdgesFromSideValue,
                EdgesToEndValue,
                EdgesToSideValue,
            ),
        ):
            return obj.value  # or however you want to represent NodeType
        if isinstance(obj, Color):
            return obj.color  # Serialize Color instances as their color attribute
        if isinstance(
            obj, (Edge, GenericNode, TextNode, FileNode, LinkNode, GroupNode)
        ):
            return obj.to_dict()  # Use the to_dict method to serialize these objects

        # Call the base class implementation which takes care of raising exceptions for unsupported types
        return JSONEncoder.default(self, obj)
