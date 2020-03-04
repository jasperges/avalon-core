"""Library funtions for Cinema4d."""

import contextlib

import c4d


def active_document():
    """Get the active Cinema4d document.

    Returns:
        c4d.document.BaseDocument
    """

    return c4d.documents.GetActiveDocument()


@contextlib.contextmanager
def maintained_selection():
    """Maintain selection during context."""

    doc = active_document()
    previous_selection = doc.GetSelection()

    try:
        yield
    finally:
        if previous_selection:
            # First start a new selection with the first object
            doc.SetSelection(previous_selection[0], c4d.SELECTION_NEW)
            # Then add the other objects to the selections
            for obj in previous_selection[1:]:
                doc.SetSelection(obj, c4d.SELECTION_ADD)
        else:
            doc.SetSelection(None, c4d.SELECTION_NEW)


@contextlib.contextmanager
def undo_chunk():
    """Open a undo chunk during context."""

    doc = active_document()

    try:
        doc.StartUndo()
        yield
    finally:
        doc.EndUndo()


def imprint(node, data):
    """Write `data` to `node` as userDefined attributes

    Arguments:
        node (c4d.BaseObject): The selection object
        data (dict): Dictionary of key/value pairs
    """

    for key, value in data.items():

        if callable(value):
            # Support values evaluated at imprint
            value = value()

        if isinstance(value, bool):
            add_type = c4d.DTYPE_BOOL
        elif isinstance(value, basestring):
            add_type = c4d.DTYPE_STRING
            # Cinema 4D doesn't except unicode, so convert to string
            value = str(value)
        elif isinstance(value, int):
            add_type = c4d.DTYPE_LONG
        elif isinstance(value, float):
            add_type = c4d.DTYPE_REAL
        else:
            raise TypeError("Unsupported type: %r" % type(value))

        base_container = c4d.GetCustomDataTypeDefault(add_type)
        base_container[c4d.DESC_NAME] = key
        base_container[c4d.DESC_SHORT_NAME] = key
        base_container[c4d.DESC_ANIMATE] = c4d.DESC_ANIMATE_OFF
        element = node.AddUserData(base_container)
        node[element] = value

    c4d.EventAdd()
