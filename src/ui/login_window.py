from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QFrame, QGridLayout, QSizePolicy, QSpacerItem
)
from PyQt6.QtGui import QPixmap, QFont, QPalette, QBrush
from PyQt6.QtCore import Qt
from pathlib import Path


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BenchSmart")
        self.setMinimumSize(1200, 700)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # === LEFT: Background Image ===
        image_label = QLabel()
        image_path = Path(__file__).resolve().parent.parent / "assets/images/login_background.jpg"
        pixmap = QPixmap(str(image_path))
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # === RIGHT: Login Frame ===
        login_frame = QFrame()
        login_frame.setFixedWidth(400)
        login_frame.setStyleSheet("""
            QFrame {
                background-color: #1166bb;
                border-radius: 12px;
                padding: 30px;
            }
        """)

        login_layout = QVBoxLayout()
        login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Login")
        title.setFont(QFont("Arial", 18))
        title.setStyleSheet("color: white; margin-bottom: 20px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Username
        username = QLineEdit()
        username.setPlaceholderText("Username")
        username.setStyleSheet("padding: 10px; border-radius: 5px;")

        # Password
        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setStyleSheet("padding: 10px; border-radius: 5px;")

        # Sign In Button
        signin_btn = QPushButton("Sign In")
        signin_btn.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #333;
            }
        """)

        # Add widgets
        login_layout.addWidget(title)
        login_layout.addWidget(username)
        login_layout.addWidget(password)
        login_layout.addSpacing(10)
        login_layout.addWidget(signin_btn)
        login_frame.setLayout(login_layout)

        # Spacer to center it vertically
        center_layout = QVBoxLayout()
        center_layout.addItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        center_layout.addWidget(login_frame)
        center_layout.addItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        layout.addWidget(image_label)
        layout.addLayout(center_layout)

        self.setLayout(layout)
