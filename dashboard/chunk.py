from streamlit_elements import mui, editor, sync, lazy
from .dashboard import Dashboard


# TODO:
# - write/update chunk position in the header
# - make collapse-able
class Chunk(Dashboard.Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._editor_box_style = {
            "flex": 1,
            "minHeight": 0,
            "borderBottom": 1,
            "borderTop": 1,
            "borderColor": "divider",
        }

    DEFAULT_CONTENT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Id eu nisl nunc mi ipsum faucibus vitae aliquet. Nam aliquam sem et tortor consequat id. Sed enim ut sem viverra aliquet eget. Sed sed risus pretium quam vulputate dignissim. Volutpat est velit egestas dui id. Commodo viverra maecenas accumsan lacus vel. Ante in nibh mauris cursus. Volutpat blandit  aliquam etiam erat velit. Adipiscing enim eu turpis egestas. Diam sollicitudin tempor id eu nisl nunc mi. Placerat in egestas erat imperdiet sed euismod. Odio pellentesque diam volutpat commodo sed egestas egestas."""

    def update_content(self, content):
        pass

    def __call__(self, content):
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
            with self.title_bar(padding="0px 15px 0px 15px", dark_switcher=False):
                mui.icon.Notes()
                mui.Typography("Chunk")

            with mui.Box(sx=self._editor_box_style):
                mui.Typography(self.DEFAULT_CONTENT)
