import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

st.title("🎨 رسمة بالأشكال")

# إدخال من المستخدم
shape = st.text_input("اكتب الشكل اللي تحب ترسمه (مربع / مثلث / دائرة):")

fig, ax = plt.subplots()

if shape == "مربع":
    square = plt.Rectangle((-1, -1), 2, 2, fill=None, edgecolor="red", linewidth=3)
    ax.add_patch(square)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    st.pyplot(fig)

elif shape == "مثلث":
    triangle = plt.Polygon([[-1, -1], [1, -1], [0, 1]], fill=None, edgecolor="green", linewidth=3)
    ax.add_patch(triangle)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    st.pyplot(fig)

elif shape == "دائرة":
    circle = plt.Circle((0, 0), 1, fill=None, edgecolor="blue", linewidth=3)
    ax.add_patch(circle)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    st.pyplot(fig)

elif shape != "":
    st.error("⚠ الشكل غير معروف، اكتب (مربع / مثلث")