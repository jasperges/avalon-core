"""Host API required Work Files tool"""
import os

import c4d


def file_extensions():
    return [".c4d"]
    
    
def _document():
    return c4d.documents.GetActiveDocument()


def has_unsaved_changes():
    doc = _document()
    if doc:
        return doc.GetChanged()


def save_file(filepath):
    doc = _document()
    if doc:
            return c4d.documents.SaveDocument(doc, 
                                              filepath, 
                                              c4d.SAVEDOCUMENTFLAGS_NONE,
                                              c4d.FORMAT_C4DEXPORT)


def open_file(filepath):
    filepath = str(filepath)    # C4D LoadFile fails on unicode
    return c4d.documents.LoadFile(str(filepath))


def current_file():
    doc = _document()
    if doc:
        root = doc.GetDocumentPath()
        fname = doc.GetDocumentName()
        if root and fname:
            return os.path.join(root, fname)


def work_root():
    from avalon import Session

    work_dir = Session["AVALON_WORKDIR"]
    scene_dir = Session.get("AVALON_SCENEDIR")
    if scene_dir:
        return os.path.join(work_dir, scene_dir)
    else:
        return work_dir
