# exceptions.py
class JsonCanvasException(Exception):
    """Base exception for all JsonCanvas errors."""

    pass


class InvalidJsonError(JsonCanvasException):
    """Raised when the JSON is invalid or malformed."""

    pass


class NodeNotFoundError(JsonCanvasException):
    """Raised when a specified node is not found."""

    pass


class EdgeNotFoundError(JsonCanvasException):
    """Raised when a specified edge is not found."""

    pass


class InvalidNodeTypeError(JsonCanvasException):
    """Raised when a node has an invalid or unsupported type."""

    pass


class InvalidNodeAttributeError(JsonCanvasException):
    """Raised when a node attribute is invalid or missing."""

    pass


class InvalidEdgeConnectionError(JsonCanvasException):
    """Raised when an edge's connection points are invalid."""

    pass


class InvalidEdgeAttributeError(JsonCanvasException):
    """Raised when an edge attribute is invalid or missing."""

    pass


class NodeIDConflictError(JsonCanvasException):
    """Raised when two nodes have the same ID."""

    pass


class EdgeIDConflictError(JsonCanvasException):
    """Raised when two edges have the same ID."""

    pass


class InvalidColorValueError(JsonCanvasException):
    """Raised when a color value is invalid or not supported."""

    pass


class InvalidPositionError(JsonCanvasException):
    """Raised when a node's position is outside the allowed range."""

    pass


class InvalidDimensionError(JsonCanvasException):
    """Raised when a node's dimensions are invalid."""

    pass


class InvalidGroupOperationError(JsonCanvasException):
    """Raised for invalid operations on group nodes."""

    pass


class OrphanEdgeError(JsonCanvasException):
    """Raised when an edge refers to a non-existent node."""

    pass


class UnsupportedFileTypeError(JsonCanvasException):
    """Raised when a file node points to an unsupported file type."""

    pass


class FileReadError(JsonCanvasException):
    """Raised when there is an error reading a file."""

    pass


class FileWriteError(JsonCanvasException):
    """Raised when there is an error writing to a file."""

    pass


class InvalidEdgeConnectionError(JsonCanvasException):
    """Raised when an edge's connection points are invalid."""

    pass


class RenderingError(JsonCanvasException):
    """Raised when there is an error during rendering."""

    pass


class CanvasValidationError(JsonCanvasException):
    """Raised when the canvas does not pass validation checks."""

    pass
