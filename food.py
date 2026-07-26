import streamlit as st
from geopy.distance import geodesic

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Durgapur Food Delivery",
    page_icon="🍔",
    layout="centered"
)

# -----------------------------------
# RESTAURANT DATABASE
# -----------------------------------

restaurants = {

    "Food Plaza" : {

        "location" : (23.5204, 87.3119),

        "menu" : {

            "Burger" : 120,
            "Pizza" : 350,
            "Pasta" : 220,
            "Cold Drink" : 60

        }

    },

    "Spicy Hub" : {

        "location" : (23.5500, 87.2900),

        "menu" : {

            "Chicken Biryani" : 280,
            "Mutton Biryani" : 380,
            "Kebab" : 180,
            "Roll" : 120

        }

    },

    "Green Bowl" : {

        "location" : (23.5400, 87.3200),

        "menu" : {

            "Veg Salad" : 150,
            "Paneer Wrap" : 180,
            "Smoothie" : 140,
            "Fruit Bowl" : 200

        }

    }

}

# -----------------------------------
# DELIVERY LOCATIONS
# -----------------------------------

locations = {

    "City Center" : (23.5937, 87.3215),

    "Bidhannagar" : (23.5505, 87.2861),

    "Benachity" : (23.5658, 87.3020),

    "Muchipara" : (23.5200, 87.3000),

    "A-Zone" : (23.5600, 87.2800),

    "B-Zone" : (23.5700, 87.2950)

}

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🍔 Durgapur Food Delivery App")

st.write("Order food from popular restaurants in Durgapur")

# -----------------------------------
# RESTAURANT SELECTION
# -----------------------------------

restaurant = st.selectbox(

    "Choose Restaurant",

    list(restaurants.keys())

)

# -----------------------------------
# MENU
# -----------------------------------

st.subheader("📜 Menu")

menu = restaurants[restaurant]["menu"]

food_item = st.selectbox(

    "Choose Food Item",

    list(menu.keys())

)

food_price = menu[food_item]

st.success(
    "Food Price : ₹ " +
    str(food_price)
)

# -----------------------------------
# DELIVERY LOCATION
# -----------------------------------

delivery_location = st.selectbox(

    "Choose Delivery Location",

    list(locations.keys())

)

# -----------------------------------
# ORDER BUTTON
# -----------------------------------

if st.button("🍽️ Order Food"):

    # RESTAURANT COORDINATES

    restaurant_coordinates = (
        restaurants[restaurant]["location"]
    )

    # CUSTOMER COORDINATES

    customer_coordinates = (
        locations[delivery_location]
    )

    # DISTANCE CALCULATION

    distance = geodesic(

        restaurant_coordinates,
        customer_coordinates

    ).km

    distance = round(distance, 2)

    # DELIVERY CHARGE

    delivery_charge = distance * 10

    delivery_charge = round(delivery_charge, 2)

    # TOTAL AMOUNT

    total_amount = (
        food_price +
        delivery_charge
    )

    # ESTIMATED TIME

    estimated_time = (
        distance * 5
    )

    estimated_time = round(estimated_time)

    # -----------------------------------
    # ORDER SUMMARY
    # -----------------------------------

    st.subheader("🧾 Order Summary")

    st.write(
        "Restaurant : ",
        restaurant
    )

    st.write(
        "Food Item : ",
        food_item
    )

    st.write(
        "Delivery Location : ",
        delivery_location
    )

    st.write(
        "Distance : ",
        distance,
        " KM"
    )

    st.write(
        "Delivery Charge : ₹ ",
        delivery_charge
    )

    st.write(
        "Estimated Delivery Time : ",
        estimated_time,
        " Minutes"
    )

    st.success(
        "Total Amount Payable : ₹ " +
        str(total_amount)
    )

    st.success("🎉 Order Placed Successfully")

