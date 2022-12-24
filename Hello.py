import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout= "wide",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

# tab1, tab2, tab3 = st.tabs(['📈_Plotting_Demo', '📊_Chart_Demo', '📚_Text_Demo'])

# with tab1:
#     st.header('Plotting Demo')
#     st.write('This is a demo of Streamlit\'s plotting capabilities.')
#     st.write('You can use `st.line_chart`, `st.area_chart`, `st.bar_chart`, and `st.pyplot` to draw charts.')
#     st.write('You can also use `st.map` to draw maps.')
#     st.write('---')
#     st.write('### Line Chart')
#     st.line_chart({
#         'first': [1, 2, 3, 4],
#         'second': [10, 20, 30, 40],
#         'third': [5, 4, 3, 2],
#     })
#     st.write('### Area Chart')
#     st.area_chart({
#         'first': [1, 2, 3, 4],
#         'second': [10, 20, 30, 40],
#         'third': [5, 4, 3, 2],
#     })
#     st.write('### Bar Chart')
#     st.bar_chart({
#         'first': [1, 2, 3, 4],
#         'second': [10, 20, 30, 40],
#         'third': [5, 4, 3, 2],
#     })
#     st.write('### Pyplot')
#     st.pyplot()
#     st.write('### Map')
#     st.map({
#         'San Francisco': (37.76, -122.4),
#         'New York': (40.71, -74.0),
#         'Austin': (30.28, -97.7),
#     })