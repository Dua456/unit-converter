import streamlit as st

# App title
st.title("🔄 Advanced Unit Converter App")

# Sidebar for category selection
st.sidebar.header("🛠️ Choose Conversion Type")

category_options = ["📏 Length", "⚖️ Weight", "🌡️ Temperature", "💰 Currency"]
category = st.sidebar.selectbox(
    "Choose an option",
    ["Choose an option"] + category_options,
    index=0,
    label_visibility="collapsed"
)

# Dictionary for unit options
conversion_units = {
    "📏 Length": ["Meters", "Feet", "Kilometers", "Miles", "Centimeters", "Millimeters", "Yards", "Inches"],
    "⚖️ Weight": ["Kilograms", "Pounds", "Grams"],
    "🌡️ Temperature": ["Celsius", "Fahrenheit"],
    "💰 Currency": ["USD", "PKR", "EUR"]
}

# Show unit selection dropdowns if a category is chosen
if category in conversion_units:
    st.subheader(f"🔁 {category.replace('📏 ', '').replace('⚖️ ', '').replace('🌡️ ', '').replace('💰 ', '')} Conversion")

    from_unit = st.selectbox("From", conversion_units[category])
    to_unit = st.selectbox("To", conversion_units[category])

    # Input value
    value = st.number_input("✍️ Enter the value to convert", min_value=0.0, format="%.2f")

    # Conversion function
    def convert_units(value, from_unit, to_unit):
        conversion_factors = {
            # Length conversions
            ("Meters", "Feet"): 3.28084, ("Feet", "Meters"): 1 / 3.28084,
            ("Kilometers", "Miles"): 0.621371, ("Miles", "Kilometers"): 1 / 0.621371,
            ("Centimeters", "Meters"): 0.01, ("Meters", "Centimeters"): 100,
            ("Millimeters", "Meters"): 0.001, ("Meters", "Millimeters"): 1000,
            ("Yards", "Meters"): 0.9144, ("Meters", "Yards"): 1 / 0.9144,
            ("Inches", "Centimeters"): 2.54, ("Centimeters", "Inches"): 1 / 2.54,
            ("Miles", "Meters"): 1609.34, ("Meters", "Miles"): 1 / 1609.34,
            ("Yards", "Feet"): 3, ("Feet", "Yards"): 1 / 3,
            ("Inches", "Feet"): 1 / 12, ("Feet", "Inches"): 12,

            # Weight conversions
            ("Kilograms", "Pounds"): 2.20462, ("Pounds", "Kilograms"): 1 / 2.20462,
            ("Grams", "Kilograms"): 1 / 1000, ("Kilograms", "Grams"): 1000,

            # Temperature conversions (Handled with functions)
            ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
            ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,

            # Currency conversions (Example rates, update dynamically for real use)
            ("USD", "PKR"): 277, ("PKR", "USD"): 1 / 277,
            ("EUR", "USD"): 1.1, ("USD", "EUR"): 1 / 1.1,
            ("PKR", "EUR"): 1 / (277 * 1.1),  # 0.00328
            ("EUR", "PKR"): 277 * 1.1  # 304.7
        }

        # Perform conversion
        if (from_unit, to_unit) in conversion_factors:
            factor = conversion_factors[(from_unit, to_unit)]
            return factor(value) if callable(factor) else value * factor
        return value  # If same unit, return the input value

    # Button to perform conversion
    if st.button("🔄 Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

else:
    st.sidebar.warning("⚠️ Please select a conversion category!")

# Footer
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>Created by Dua Shakir Hussain</h4>", unsafe_allow_html=True)
