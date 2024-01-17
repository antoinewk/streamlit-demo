from functools import partial
from streamlit_elements import mui, editor, sync, lazy
from .dashboard import Dashboard


class Answer(Dashboard.Item):
    DEFAULT_CONTENT = "Given the chunks, attention is all you need."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._editor_box_style = {
            "flex": 1,
            "minHeight": 0,
            "borderBottom": 1,
            "borderTop": 1,
            "borderColor": "divider",
        }

    def update_content(self, content=None):
        pass

    def __call__(self, content=None):
        with mui.Paper(
            key=self._key,
            sx={
                "display": "flex",
                "flexDirection": "column",
                "borderRadius": 3,
                "overflow": "hidden",
            },
            elevation=1,
        ):
            with self.title_bar(dark_switcher=False):
                mui.icon.FormatQuote()
                mui.Typography("Answer")

            content = content if content else self.DEFAULT_CONTENT

            with mui.Box(sx=self._editor_box_style):
                editor.Monaco(
                    css={"padding": "0 2px 0 2px"},
                    defaultValue=content,
                    onChange=self.update_content,
                    options={"wordWrap": True},
                )
