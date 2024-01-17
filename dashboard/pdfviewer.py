from streamlit_elements import mui, html
from .dashboard import Dashboard
import base64


# TODO:
# - make pdf file an input variable
# - should be changeable
class PdfViewer(Dashboard.Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
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
                mui.icon.PictureAsPdf()
                mui.Typography("Pdf Viewer", sx={"flex": 1})

            with open("1706.03762.pdf", "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")
            html.iframe(src=f"data:application/pdf;base64,{base64_pdf}", height="100%")
