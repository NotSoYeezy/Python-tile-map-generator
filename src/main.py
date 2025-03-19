import sys
from app import TileMapWindow
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = TileMapWindow()
    window.setWindowTitle("Tile Map Generator")
    window.show()
    return app.exec()


if __name__ == '__main__':
    main()