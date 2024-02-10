
import pickle
import streamlit as st

# Load the trained model from the pickle file
with open('Supply_chain_management_model.pkl','rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Supply Chain Management Prediction Model")

# Input fields
num_refill_req_l3m = st.text_input("Refilling request received in last 3 months (0-100)",  value=" ")
Competitor_in_mkt = st.text_input("Number of competitors in the market (0-100)", value=" ")
retail_shop_num = st.text_input("Number of retail shops (1000-15000)", value=" ")
distributor_num = st.text_input("Number of distributors (10-100)", value=" ")
dist_from_hub = st.text_input("Distance from the warehouse to production (10-300)", value=" ")
storage_issue_reported_l3m = st.text_input("storage issues reported in the last 3months (0-50)", value=" ")
Large = st.text_input("Is capacity size Large? (0 / 1)", value=" ")
Mid = st.text_input("Is capacity size Mid? (0 / 1)", value=" ")
Small = st.text_input("Is capacity size Small? (0 / 1)", value=" ")

# Submit Button
st.button("Predict")

# Predict product_wg_ton based on the input values
input_features = [[num_refill_req_l3m, Competitor_in_mkt, retail_shop_num, distributor_num, dist_from_hub, storage_issue_reported_l3m, Large, Mid, Small]]
predicted_product_wg_ton = model.predict(input_features)

# Display the predicted weight
st.write("<b> Predicted Product Weight in ton: ", predicted_product_wg_ton[0], "</b>", unsafe_allow_html=True)



