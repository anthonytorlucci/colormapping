"""Predicates
"""

# TODO: create a custom Excecption is_acceptable_colorspace 

def is_acceptable_colorspace_3tuple(cspace:str) -> bool:
    """Predicate to test whether an input color space for tuple of 3 values is one of the 
    defined colorspaces in colorspacious.

    :param cspace: color space
    :type cspace: str
    :return: boolean value for predicate
    :rtype: bool
    """
    acceptable_colorspaces_3tuple = ["sRGB1", "sRGB255", "XYZ1", "XYZ100", "xyY100", "xyY1", "CAM02-UCS",
        "CIELab", "CIELCh", "JCh", "JMh", "Jsh", "JCH", "JMH", "JsH", "QCh", "QMh", "Qsh",
        "QCH", "QMH", "QsH"]
    if cspace in acceptable_colorspaces_3tuple:
        return True
    else: 
        return False