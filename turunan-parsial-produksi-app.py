import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Judul Aplikasi
st.title("Aplikasi Interaktif: Turunan Parsial dan Visualisasi 3D")

# Inisialisasi simbol
z, y = sp.symbols('z y')

# Input fungsi dan titik evaluasi
func_input = st.text_input("Masukkan fungsi f(z, y):", "0.5*z**2 + 0.3*y**2 + 3*z*y")
point_z = st.number_input("Nilai z (misalnya 20):", value=20)
point_y = st.number_input("Nilai y (misalnya 5):", value=5)

try:
    # Interpretasi fungsi
    f = sp.sympify(func_input)

    # Hitung turunan parsial
    f_z = sp.diff(f, z)
    f_y = sp.diff(f, y)

    # Evaluasi fungsi dan turunannya
    f_val = f.subs({z: point_z, y: point_y})
    fz_val = f_z.subs({z: point_z, y: point_y})
    fy_val = f_y.subs({z: point_z, y: point_y})

    # Tampilkan hasil analitik
    st.subheader("Hasil Turunan Parsial dan Evaluasi Titik")
    st.latex(f"f(z, y) = {sp.latex(f)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial z}} = {sp.latex(f_z)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(f_y)}")
    st.write(f"f({point_z}, {point_y}) = {f_val}")
    st.write(f"∂f/∂z({point_z}, {point_y}) = {fz_val}")
    st.write(f"∂f/∂y({point_z}, {point_y}) = {fy_val}")

    # Visualisasi grafik
    st.subheader("Visualisasi Permukaan dan Bidang Singgung")
    z_vals = np.linspace(point_z - 10, point_z + 10, 50)
    y_vals = np.linspace(point_y - 10, point_y + 10, 50)
    Z, Y = np.meshgrid(z_vals, y_vals)
    f_func = sp.lambdify((z, y), f, 'numpy')
    F = f_func(Z, Y)
    tangent = float(f_val) + float(fz_val)*(Z - point_z) + float(fy_val)*(Y - point_y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(Z, Y, F, alpha=0.6, cmap='viridis', label="Permukaan")
    ax.plot_surface(Z, Y, tangent, alpha=0.5, color='red')
    ax.scatter(point_z, point_y, float(f_val), color='black', s=50)
    ax.set_xlabel("z")
    ax.set_ylabel("y")
    ax.set_zlabel("f(z, y)")
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
