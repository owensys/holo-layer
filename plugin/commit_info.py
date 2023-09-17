from PyQt6.QtCore import QObject, QRectF, Qt
from PyQt6.QtGui import QColor, QFont, QFontDatabase
from utils import get_emacs_vars, get_emacs_var


class WindowCommitInfo(QObject):

    def __init__(self) -> None:
        super().__init__()

        self.text_color = None

        (text_color, self.font_size) = get_emacs_vars(["holo-layer-window-number-color",
                                                       "holo-layer-window-number-font-size"])

        self.enable_commit_info = get_emacs_var("holo-layer-enable-commit-info")

        self.text_color = QColor(text_color)
        self.font_family = QFontDatabase.systemFont(
            QFontDatabase.SystemFont.FixedFont
        ).family()
        self.font = QFont()
        self.font.setFamily(self.font_family)
        self.font.setPointSize(self.font_size)

        self.margin_left = 20

    def draw(self, painter, emacs_frame_info, cursor_info):
        if self.enable_commit_info:
            if emacs_frame_info and len(cursor_info) > 2:
                [emacs_x, emacs_y, emacs_width, emacs_height] = emacs_frame_info
                cursor_x = cursor_info[0]
                cursor_y = cursor_info[1]
                offset_x = 0
                offset_y = 20
                text_padding = 6
                painter.setBrush(QColor(50, 50, 50, 200))
                painter.drawRect(QRectF(emacs_x + int(cursor_x) + offset_x,
                                        emacs_y + int(cursor_y) + offset_y,
                                        600, 60))
                painter.setPen(QColor(230, 230, 230))
                painter.drawText(QRectF(emacs_x + int(cursor_x) + offset_x + text_padding,
                                        emacs_y + int(cursor_y) + offset_y + text_padding,
                                        580, 60), Qt.AlignmentFlag.AlignLeft, "cursor x:" + cursor_x + ",y:" + cursor_y);
