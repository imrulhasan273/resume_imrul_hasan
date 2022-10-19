import os
from time import time
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.skills
import pages.projects
import pages.edu
import pages.recommendations

import resources.ast as ast

PAGES = {
    "About": pages.about,
    "Education" : pages.edu,
    "Skills": pages.skills,
    "Projects": pages.projects,
    "Recommendations": pages.recommendations
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me")
    st.sidebar.info(
        """
        If you are looking to hire a Data Scientist, 
        [email me](mailto:imrulhasan273@gmail.com) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/ih273/)
        """
    )

    st.sidebar.title("Additional Info")
    st.sidebar.info(
        """
        This an interactive streamlit app completely created with Python's latest library **streamlit**
        Do reach out to me on [LinkedIn](https://www.linkedin.com/in/abhishek-gupta-/) or 
        at [Mail me](mailto:abhishek.2.gupta@uconn.edu) to know more. 
        Also check the [source code](https://github.com/alphadatagamma/Streamlit-Resume-App) here. 
        """
    )



if __name__ == "__main__":
    main()

'''
Experience
Education
Publications
Technical Skillset
Projects
Online Courses & Specializations
Problem Solving
Achievements
References
'''
#streamlit run home.py

