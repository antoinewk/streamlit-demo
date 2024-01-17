import streamlit as st

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event, mui
from types import SimpleNamespace

from dashboard import Dashboard
from dashboard.pdfviewer import PdfViewer
from dashboard.question import Question
from dashboard.chunk import Chunk
from dashboard.answer import Answer


def main():
    st.write(
        """
        # RAG demo
        """
    )

    with st.expander("GETTING STARTED"):
        st.write((Path(__file__).parent / "README.md").read_text())

    if "w" not in state:
        board = Dashboard()
        w = SimpleNamespace(
            dashboard=board,
            question=Question(board, 0, 0, 6, 3, minW=3, minH=3),
            chunks=[Chunk(board, 0, 0, 6, 4) for i in range(3)],
            pdfviewer=PdfViewer(board, 6, 0, 6, 15, minH=10),
            answer=Answer(board, 0, 12, 12, 3, minW=3, minH=3),
        )
        state.w = w
    else:
        w = state.w

    with elements("demo"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

        with w.dashboard(rowHeight=57):
            w.question()
            _ = [i("test") for i in w.chunks]
            w.pdfviewer()
            w.answer()


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
