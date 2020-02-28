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

    # TODO (jasper): seeing the `Selection` object, this might be the way to
    # go. In the GUI you even have the option 'restore' selection. Then the
    # workflow would be: create `Selection` with currently selected objects
    # (default from GUI) → do stuff → restore selection from `Selection` →
    # remove `Selection`.

    doc = active_document()
    previous_selection = doc.GetSelection()

    try:
        yield
    finally:
        if previous_selection:
            doc.SetSelection(previous_selection, mode=c4d.SELECTION_NEW)
        else:
            # This is probably wrong, but it seems to work.
            # As far as I understand it creates an empty list of type Opolygon.
            # Then set the selection to this empty list, effectively selecting
            # nothting.
            doc.SetSelection(c4d.BaseList2D(c4d.Opolygon), c4d.SELECTION_NEW)
