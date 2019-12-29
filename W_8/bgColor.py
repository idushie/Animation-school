#* set background color
self.setAutoFillBackground(1)
color = 150
self.p = self.palette()
self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
self.setPalette(self.p)
