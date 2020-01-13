if layout.count(): # if layout has any children
  for i in range(layout.count()):
    item = layout.itemAt(i)
    widget = item.widget()
    if widget:
      if widget.objectName() == "someName":
        widget.deleteLater()
