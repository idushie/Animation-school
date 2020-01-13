from PySide2 import QtWidgets, QtGui, QtCore
from shiboken2 import wrapInstance
# Maya Python API 2.0
from maya.api.OpenMaya import MGlobal

# Maya Python API 1.0
from maya.OpenMayaUI import MQtUtil


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = MQtUtil.mainWindow() # Python API 1.0
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        button = QtWidgets.QPushButton("Print Error", self)
        button.clicked.connect(self.close)

    def print_error(self):
        MGlobal.displayError("Python API 2.0 Error Message") # Python API 2.0


if __name__ == "__main__":

    try:
        test_dialog.close() # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()
