
"""About page shown when the user enters the application"""
import streamlit as st
import streamlit.components.v1 as cmp


def write():
    """Used to write the about page in the app.py file"""
    st.title("Un Esprit Curieux - A curious mind! :sleuth_or_spy:")
    st.markdown(
            """

            """,unsafe_allow_html=True,
    )
    HtmlFile = open("pages/templates/about.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    cmp.html(source_code)


if __name__ == "__main__":
    write()


