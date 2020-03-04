"""Host API required Work Files tool"""
import os

import c4d
from . import lib


def file_extensions():
    return [".c4d"]


def has_unsaved_changes():
    doc = lib.active_document()
    if doc:
        return doc.GetChanged()


def save_file(filepath):
    doc = lib.active_document()
    if doc:
        # Cinema4D does not update the current document path and name when
        # you save because the same function is used to export data.
        # If you rename current document after saving then it assumed
        # it has been changed again which we can't seem to disable.
        # So we update the work file path and name beforehand
        doc.SetDocumentPath(os.path.dirname(filepath))
        doc.SetDocumentName(os.path.basename(filepath))

        return c4d.documents.SaveDocument(
            doc,
            str(filepath),
            c4d.SAVEDOCUMENTFLAGS_NONE,
            c4d.FORMAT_C4DEXPORT,
        )


def open_file(filepath):
    filepath = str(filepath)  # C4D LoadFile fails on unicode
    return c4d.documents.LoadFile(filepath)


def current_file():
    doc = lib.active_document()
    if doc:
        root = doc.GetDocumentPath()
        fname = doc.GetDocumentName()
        if root and fname:
            return os.path.join(root, fname)


def work_root(session):

    work_dir = session["AVALON_WORKDIR"]
    scene_dir = session.get("AVALON_SCENEDIR")
    if scene_dir:
        return os.path.join(work_dir, scene_dir)
    else:
        return work_dir
