"""Main module for the streamlit Dyslexia app"""

import streamlit as st


import pages.home
import pages.quiz
import pages.survey


PAGES = {
    "Home": pages.home,
    "Quiz": pages.quiz,
    "Survey": pages.survey
}


def main():

    st.sidebar.title("DyslexiaML")
    st.sidebar.text("AI for Dyslexia")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))

    

    with st.spinner(f"Loading {page} ..."):
        PAGES[page].main()

    st.sidebar.title("About App")

    st.sidebar.info(
        """
        This App uses Machine Learning to Detect Dyslexia.  
        It uses Streamlit for implemention of beatiful and easy web app.
        """
    )

    st.sidebar.title("Contact Developer")
    st.sidebar.info(
        """
        This app is develop by Dyslexiaworkin Organization. You can contact us at
        [Dyslexiaworkin](https://github.com/dyslexiaworkin).
"""
    )

   #st.sidebar.markdown("[![Github](https://github.com/aryanc55/NLPJenny/blob/master/assests/github.png?raw=true)](https://github/aryanc55)")

    st.sidebar.markdown(
        """  [Github](https://github.com/dyslexiaworkin)""")  # change all thses three to  to iamge
    st.sidebar.markdown("""  [Twitter](https://twitter.com/aryanc55)""")
    """)

    st.sidebar.title("Souce Code")
    st.sidebar.info(
        "This an free to use template repository and you are very welcome to **contribute** your awesome "
        "comments, questions, resources and apps as "
        "[issues](https://github.com/dyslexiaworkin/DyslexiaML/issues) of or "
        "[pull requests](https://github.com/dyslexiaworkin/DyslexiaML/pulls) "
        "to the [source code](https://github.com/dyslexiaworkin/DyslexiaML). "
    )


if __name__ == "__main__":
    main()