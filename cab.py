import streamlit as st
from geopy.distance import geodesic

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Durgapur Cab Booking",
    page_icon="🚖",
    layout="centered"
)

st.title("🚖 Durgapur Cab Booking System")

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "data" not in st.session_state:

    st.session_state.data = {

        "cab_rates": {

            "Mini": 12,
            "Sedan": 15,
            "SUV": 20

        },

        "locations": {

            "City Center": (23.5937, 87.3215),
            "Benachity": (23.5658, 87.3020),
            "Bidhannagar": (23.5505, 87.2861),
            "Muchipara": (23.5200, 87.3000),
            "A-Zone": (23.5600, 87.2800),
            "B-Zone": (23.5700, 87.2950)

        },

        "bookings": {},

        "next_booking_id": 1

    }

# -----------------------------------
# BOOKING FORM
# -----------------------------------

with st.form("booking_form", clear_on_submit=True):

    st.subheader("Book Your Cab")

    customer_name = st.text_input("Customer Name")

    phone = st.text_input("Phone Number")

    pickup = st.selectbox(

        "Pickup Location",

        list(st.session_state.data["locations"].keys())

    )

    drop = st.selectbox(

        "Drop Location",

        list(st.session_state.data["locations"].keys())

    )

    cab_type = st.selectbox(

        "Cab Type",

        list(st.session_state.data["cab_rates"].keys())

    )

    submitted = st.form_submit_button("Book Cab")

    if submitted:

        if customer_name.strip() == "" or phone.strip() == "":

            st.warning("Please enter all details.")

        elif pickup == drop:

            st.warning("Pickup and Drop cannot be the same.")

        else:

            pickup_coordinate = st.session_state.data["locations"][pickup]

            drop_coordinate = st.session_state.data["locations"][drop]

            distance = geodesic(

                pickup_coordinate,

                drop_coordinate

            ).km

            distance = round(distance,2)

            rate = st.session_state.data["cab_rates"][cab_type]

            fare = round(distance * rate,2)

            booking_id = st.session_state.data["next_booking_id"]

            st.session_state.data["bookings"][booking_id] = {

                "customer": {

                    "name": customer_name,

                    "phone": phone

                },

                "trip": {

                    "pickup": pickup,

                    "drop": drop,

                    "cab_type": cab_type,

                    "distance": distance,

                    "fare": fare

                },

                "status": {

                    "booked": True,

                    "completed": False

                }

            }

            st.session_state.data["next_booking_id"] += 1

            st.success("Cab Booked Successfully!")

            st.rerun()

# -----------------------------------
# DASHBOARD
# -----------------------------------

total_bookings = len(

    st.session_state.data["bookings"]

)

completed = sum(

    1

    for booking in st.session_state.data["bookings"].values()

    if booking["status"]["completed"]

)

pending = total_bookings - completed

col1, col2, col3 = st.columns(3)

col1.metric("Bookings", total_bookings)

col2.metric("Completed", completed)

col3.metric("Pending", pending)

st.divider()

# -----------------------------------
# DISPLAY BOOKINGS
# -----------------------------------

if total_bookings == 0:

    st.info("No Cab Bookings Available.")

else:

    st.subheader("Booking Details")

    for booking_id, booking in list(

        st.session_state.data["bookings"].items()

    ):

        st.markdown(f"### Booking ID : {booking_id}")

        col1, col2 = st.columns([5,1])

        with col1:

            st.write("👤 Customer :", booking["customer"]["name"])

            st.write("📞 Phone :", booking["customer"]["phone"])

            st.write("📍 Pickup :", booking["trip"]["pickup"])

            st.write("🏁 Drop :", booking["trip"]["drop"])

            st.write("🚖 Cab :", booking["trip"]["cab_type"])

            st.write("🛣 Distance :", booking["trip"]["distance"], "KM")

            st.write("💰 Fare : ₹", booking["trip"]["fare"])

            completed = st.checkbox(

                "Trip Completed",

                value=booking["status"]["completed"],

                key=f"complete_{booking_id}"

            )

            if completed != booking["status"]["completed"]:

                st.session_state.data["bookings"][booking_id]["status"]["completed"] = completed

                st.rerun()

        with col2:

            if st.button("🗑️", key=f"delete_{booking_id}"):

                del st.session_state.data["bookings"][booking_id]

                st.rerun()

        st.divider()

# -----------------------------------
# CLEAR BOOKINGS
# -----------------------------------

if st.button("Clear All Bookings"):

    st.session_state.data["bookings"] = {}

    st.session_state.data["next_booking_id"] = 1

    st.rerun()

# -----------------------------------
# VIEW DATABASE
# -----------------------------------

with st.expander("View Nested Dictionary"):

    st.write(st.session_state.data)
