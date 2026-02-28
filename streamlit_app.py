# Streamlit UI for ML Salary Prediction
import numpy as np
import pickle
import streamlit as st
import os

# Page config
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Load model with error handling
@st.cache_resource
def load_model():
    """Load the trained ML model from pickle file."""
    try:
        # Try current directory first
        if os.path.exists('model.pkl'):
            model = pickle.load(open('model.pkl', 'rb'))
        else:
            # Try parent directory (for Streamlit Cloud compatibility)
            model = pickle.load(open('model.pkl', 'rb'))
        return model
    except FileNotFoundError:
        st.error("❌ Model file not found. Ensure 'model.pkl' is in the project root.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()


def predict_salary(years_experience: float) -> float:
    """Predict salary from years of experience."""
    model = load_model()
    return float(model.predict([[np.array(years_experience)]])[0])


def main():
    # Title & Description
    st.title("💰 Salary Predictor")
    st.write("Predict your salary based on years of work experience")
    st.markdown("---")

    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        years_of_experience = st.number_input(
            "Enter Years of Experience",
            min_value=0.0,
            max_value=100.0,
            step=0.5,
            format="%.1f",
            help="Enter your total years of work experience"
        )

    with col2:
        predict_button = st.button("🔮 Predict", use_container_width=True)

    st.markdown("---")

    # Prediction section
    if predict_button:
        try:
            salary = predict_salary(years_of_experience)
            
            # Display result with styling
            col1, col2 = st.columns(2)
            with col1:
                st.metric(
                    label="Years of Experience",
                    value=f"{years_of_experience:.1f}",
                    delta=None
                )
            
            with col2:
                st.metric(
                    label="Predicted Salary",
                    value=f"Rs. {salary:,.2f}",
                    delta=None
                )
            
            st.success(f"✅ Based on your {years_of_experience:.1f} years of experience, your predicted salary is **Rs. {salary:,.2f}**")
            
        except Exception as e:
            st.error(f"❌ Prediction failed: {str(e)}")

    # Footer
    st.markdown("---")
    st.info("📊 This model is trained on historical salary data. Results are estimates only.")


if __name__ == "__main__":
    main()
