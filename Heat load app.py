
import streamlit as st

def calculate_heat_load(width, length, height, people, lights, equipment_kw, t_in, t_out):
    area = width * length
    volume = area * height

    # Approximate constants
    sensible_per_person = 75  # W
    latent_per_person = 55    # W
    lighting_per_unit = 15    # W per lamp
    ventilation_rate = 10     # L/s per person
    air_density = 1.2         # kg/m³
    specific_heat = 1.006     # kJ/kg·K

    # Load calculations
    people_load = people * (sensible_per_person + latent_per_person) / 1000  # kW
    lighting_load = lights * lighting_per_unit / 1000  # kW
    equipment_load = equipment_kw  # already in kW
    ventilation_load = (
        people * ventilation_rate * air_density * specific_heat * (t_out - t_in) / 1000
    )  # kW

    total_kw = people_load + lighting_load + equipment_load + ventilation_load
    total_btu = total_kw * 3412.14

    return {
        "Area (m²)": area,
        "Volume (m³)": volume,
        "People Load (kW)": people_load,
        "Lighting Load (kW)": lighting_load,
        "Equipment Load (kW)": equipment_load,
        "Ventilation Load (kW)": ventilation_load,
        "Total Load (kW)": total_kw,
        "Total Load (BTU/hr)": total_btu
    }

st.title("Cooling Load Calculator")

width = st.number_input("Room Width (m)", value=6.0)
length = st.number_input("Room Length (m)", value=5.0)
height = st.number_input("Room Height (m)", value=3.0)
people = st.number_input("Number of People", value=2)
lights = st.number_input("Number of Light Fixtures", value=4)
equipment_kw = st.number_input("Equipment Load (kW)", value=1.5)
t_in = st.number_input("Indoor Temp (°C)", value=25.0)
t_out = st.number_input("Outdoor Temp (°C)", value=35.0)

if st.button("Calculate"):
    result = calculate_heat_load(width, length, height, people, lights, equipment_kw, t_in, t_out)
    st.subheader("Results")
    for key, value in result.items():
        st.write(f"**{key}:** {value:.2f}")
