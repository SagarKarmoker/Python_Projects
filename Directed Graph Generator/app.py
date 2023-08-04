import networkx as nx
import streamlit as st

# python -m streamlit run app.py

st.set_page_config(
    page_title="Directed Graph Generator App",
    page_icon="🔃",
    initial_sidebar_state="expanded"
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

st.header("Directed Graph Generator")

edges = st.text_input("Edges",  "A->B, B->C, C->D")
st.text('Input Format: A->B, B->C, C->D')
g = nx.DiGraph()

edge_list = [edge.strip() for edge in edges.split(",")]
for edge in edge_list:
    source, target = edge.split("->")
    g.add_edge(source.strip(), target.strip(), weight=1)


st.set_option('deprecation.showPyplotGlobalUse', False)
pos = nx.circular_layout(g)
st.write("Graph:")
img = st.pyplot(nx.draw(g, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10))
with open(img, "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
          )
