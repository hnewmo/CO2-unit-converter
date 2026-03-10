import streamlit as st

# App constants
MW = 43.8892
STD_VOL = 379.48  # scf/lb-mol
LB_PER_TONNE = 2204.62

st.title("CO2 Flowrate Converter")
st.write(f"**Molecular Weight:** {MW} g/mol")

# Input layout
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Flowrate:", value=1.0, format="%.4f")
with col2:
    unit = st.selectbox("Current Unit:", ["MMSCFD", "tonne/day", "lb/hr"])

# Conversion Logic
# First, convert everything to lb/hr as a baseline
if unit == "MMSCFD":
    lb_hr = (value * 1e6 / 24) * (MW / STD_VOL)
elif unit == "tonne/day":
    lb_hr = (value * LB_PER_TONNE) / 24
else:
    lb_hr = value

# Calculate others from lb/hr
mmscfd = (lb_hr * 24 / 1e6) * (STD_VOL / MW)
tonne_day = (lb_hr * 24) / LB_PER_TONNE

# Output Display
st.divider()
st.subheader("Results")
res_col1, res_col2, res_col3 = st.columns(3)

res_col1.metric("MMSCFD", f"{mmscfd:.4f}")
res_col2.metric("Metric Tonne/Day", f"{tonne_day:.4f}")
res_col3.metric("lb/hr", f"{lb_hr:.2f}")

st.info(f"Note: Calculations assume Standard Conditions (60°F, 14.696 psia) where 1 lb-mol = {STD_VOL} scf.")
