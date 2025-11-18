"""
Component Widgets - Visual widgets for rendering process components
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
import json


class SeparatorWidget(QWidget):
    """Widget for rendering a separator component"""

    def __init__(self, config, label="", parent=None):
        super().__init__(parent)
        self.config = config if isinstance(config, dict) else {}
        self.label = label
        self.init_ui()

    def init_ui(self):
        """Initialize UI"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 10, 5, 10)

        # Get configuration
        color = self.config.get('color', '#ff6b6b')
        thickness = self.config.get('thickness', 2)
        style = self.config.get('style', 'solid')

        # Create separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFixedHeight(thickness)

        # Map style to Qt style
        border_style = 'solid'
        if style == 'dashed':
            border_style = 'dashed'
        elif style == 'dotted':
            border_style = 'dotted'
        elif style == 'double':
            thickness = max(4, thickness)  # Double needs more space
            separator.setFixedHeight(thickness)

        separator.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border: none;
                border-top: {thickness}px {border_style} {color};
            }}
        """)

        main_layout.addWidget(separator)


class NoteWidget(QWidget):
    """Widget for rendering a note component"""

    def __init__(self, config, label="", content="", parent=None):
        super().__init__(parent)
        self.config = config if isinstance(config, dict) else {}
        self.label = label
        self.content = content
        self.init_ui()

    def init_ui(self):
        """Initialize UI"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Get configuration
        background = self.config.get('background', '#fff3cd')
        icon = self.config.get('icon', '💡')

        # Create note container
        note_widget = QFrame()
        note_widget.setStyleSheet(f"""
            QFrame {{
                background-color: {background};
                border-left: 4px solid #f39c12;
                border-radius: 4px;
                padding: 10px;
            }}
        """)

        note_layout = QHBoxLayout(note_widget)

        # Icon
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 20pt;")
        note_layout.addWidget(icon_label)

        # Content
        display_text = self.content or self.label or "Nota informativa"
        content_label = QLabel(display_text)
        content_label.setStyleSheet("color: #333333; font-size: 10pt;")
        content_label.setWordWrap(True)
        note_layout.addWidget(content_label, stretch=1)

        main_layout.addWidget(note_widget)


class AlertWidget(QWidget):
    """Widget for rendering an alert component"""

    def __init__(self, config, label="", content="", parent=None):
        super().__init__(parent)
        self.config = config if isinstance(config, dict) else {}
        self.label = label
        self.content = content
        self.init_ui()

    def init_ui(self):
        """Initialize UI"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Get configuration
        alert_type = self.config.get('type', 'warning')
        title = self.config.get('title', 'Atención')

        # Colors by type
        colors = {
            'info': '#3498db',
            'warning': '#f39c12',
            'error': '#e74c3c',
            'success': '#2ecc71'
        }
        color = colors.get(alert_type, '#f39c12')

        # Icons by type
        icons = {
            'info': 'ℹ️',
            'warning': '⚠️',
            'error': '❌',
            'success': '✅'
        }
        icon = icons.get(alert_type, '⚠️')

        # Create alert container
        alert_widget = QFrame()
        alert_widget.setStyleSheet(f"""
            QFrame {{
                background-color: {color}22;
                border-left: 4px solid {color};
                border-radius: 4px;
                padding: 10px;
            }}
        """)

        alert_layout = QVBoxLayout(alert_widget)

        # Header with icon and title
        header_layout = QHBoxLayout()

        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 18pt;")
        header_layout.addWidget(icon_label)

        title_label = QLabel(title)
        title_label.setStyleSheet(f"color: {color}; font-size: 11pt; font-weight: bold;")
        header_layout.addWidget(title_label, stretch=1)

        alert_layout.addLayout(header_layout)

        # Content
        display_text = self.content or self.label
        if display_text:
            content_label = QLabel(display_text)
            content_label.setStyleSheet("color: #333333; font-size: 9pt; padding-left: 30px;")
            content_label.setWordWrap(True)
            alert_layout.addWidget(content_label)

        main_layout.addWidget(alert_widget)


class GroupWidget(QWidget):
    """Widget for rendering a group component"""

    def __init__(self, config, label="", parent=None):
        super().__init__(parent)
        self.config = config if isinstance(config, dict) else {}
        self.label = label
        self.init_ui()

    def init_ui(self):
        """Initialize UI"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Get configuration
        color = self.config.get('color', '#007acc')
        collapsible = self.config.get('collapsible', True)
        expanded = self.config.get('expanded', True)

        # Create group container
        group_widget = QFrame()
        group_widget.setStyleSheet(f"""
            QFrame {{
                background-color: #2d2d2d;
                border: 2px solid {color};
                border-radius: 6px;
            }}
        """)

        group_layout = QVBoxLayout(group_widget)
        group_layout.setContentsMargins(0, 0, 0, 0)
        group_layout.setSpacing(0)

        # Header
        header = QPushButton(f"📁 {self.label or 'Grupo'}")
        header.setCheckable(collapsible)
        header.setChecked(expanded)
        header.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        header.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                text-align: left;
                padding: 8px;
                border: none;
                font-weight: bold;
                font-size: 10pt;
                border-radius: 4px 4px 0 0;
            }}
            QPushButton:hover {{
                background-color: {color}dd;
            }}
        """)
        group_layout.addWidget(header)

        # Info label (placeholder for grouped items)
        info_label = QLabel("   Los items del grupo aparecerán aquí durante la ejecución")
        info_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 8pt;
                font-style: italic;
                padding: 8px;
            }
        """)
        group_layout.addWidget(info_label)

        main_layout.addWidget(group_widget)


def create_component_widget(component_type, config, label="", content="", parent=None):
    """
    Factory function to create the appropriate component widget

    Args:
        component_type: Type of component ('separador', 'nota', 'alerta', 'grupo')
        config: Configuration dictionary or JSON string
        label: Label text
        content: Content text
        parent: Parent widget

    Returns:
        Component widget instance
    """
    # Parse config if it's a JSON string
    if isinstance(config, str):
        try:
            config = json.loads(config)
        except json.JSONDecodeError:
            config = {}

    # Create appropriate widget based on type
    if component_type == 'separador':
        return SeparatorWidget(config, label, parent)
    elif component_type == 'nota':
        return NoteWidget(config, label, content, parent)
    elif component_type == 'alerta':
        return AlertWidget(config, label, content, parent)
    elif component_type == 'grupo':
        return GroupWidget(config, label, parent)
    else:
        # Unknown component type - return empty widget
        return QWidget(parent)
