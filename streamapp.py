# import streamlit as st

# # Streamlit UI
# st.title('Student Prediction App')

# st.header('Enter Student Information')

# # Create input fields for the features
# age = st.number_input('Age', min_value=15, max_value=100, value=18)
# attendance_rate = st.number_input('Attendance Rate (%)', min_value=0.0, max_value=100.0, value=75.0)
# gpa = st.number_input('GPA (out of 10)', min_value=0.0, max_value=10.0, value=6.5)
# study_time = st.number_input('Study Time (hours per week)', min_value=0, max_value=50, value=20)
# parent_education_level = st.number_input('Parent Education Level (1-5)', min_value=1, max_value=5, value=3)
# income_level = st.number_input('Income Level (1-100)', min_value=1, max_value=100, value=50)
# failed_subjects = st.number_input('Number of Failed Subjects', min_value=0, max_value=10, value=1)
# extracurricular_participation = st.number_input('Extracurricular Participation (1-5)', min_value=1, max_value=5, value=3)
# living_conditions = st.number_input('Living Conditions (1-5)', min_value=1, max_value=5, value=3)
# gender = st.selectbox('Gender', ['Male', 'Female'])

# # Encode gender as 0 (Female) and 1 (Male)
# gender_encoded = 1 if gender == 'Male' else 0

# # Heuristic-based prediction logic
# def predict_outcome(attendance_rate, gpa, study_time, failed_subjects, income_level, extracurricular_participation, living_conditions):
#     # Check if GPA is high enough to counter low attendance
#     if gpa >= 8.0 and attendance_rate < 50:
#         return "Graduate"
#     # Heuristic rules
#     if attendance_rate < 50 and gpa < 6.0:
#         return "Dropout"
#     if gpa < 4.0:
#         return "Dropout"
#     if study_time < 5:
#         return "Dropout"
#     if failed_subjects > 3:
#         return "Dropout"
#     if income_level < 20:
#         return "Dropout"
#     if extracurricular_participation < 2:
#         return "Dropout"
#     if living_conditions < 3:
#         return "Dropout"
    
#     return "Graduate"

# # Predict button
# if st.button('Predict'):
#     result = predict_outcome(attendance_rate, gpa, study_time, failed_subjects, income_level, extracurricular_participation, living_conditions)
#     color = 'green' if result == 'Graduate' else 'red'
#     st.markdown(f'<div style="color: {color}; font-size: 24px;">The predicted outcome is: {result}</div>', unsafe_allow_html=True)

#shahzil code
# import streamlit as st

# # Streamlit UI
# st.title('Student Prediction App')

# st.header('Enter Student Information')

# # Create input fields for the features
# age = st.number_input('Age', min_value=15, max_value=100, value=18)
# attendance_rate = st.number_input('Attendance Rate (%)', min_value=0.0, max_value=100.0, value=75.0)
# gpa = st.number_input('GPA (out of 10)', min_value=0.0, max_value=10.0, value=6.5)
# study_time = st.number_input('Study Time (hours per week)', min_value=0, max_value=50, value=20)
# parent_education_level = st.number_input('Parent Education Level (1-5)', min_value=1, max_value=5, value=3)
# income_level = st.number_input('Income Level (1-100)', min_value=1, max_value=100, value=50)
# failed_subjects = st.number_input('Number of Failed Subjects', min_value=0, max_value=10, value=1)
# extracurricular_participation = st.number_input('Extracurricular Participation (1-5)', min_value=1, max_value=5, value=3)
# living_conditions = st.number_input('Living Conditions (1-5)', min_value=1, max_value=5, value=3)
# gender = st.selectbox('Gender', ['Male', 'Female'])

# # Encode gender as 0 (Female) and 1 (Male)
# gender_encoded = 1 if gender == 'Male' else 0

# # Heuristic-based prediction logic
# def predict_outcome(attendance_rate, gpa, study_time, failed_subjects, income_level, extracurricular_participation, living_conditions):
#     # High GPA compensates for low attendance
#     if gpa >= 8.0 and attendance_rate < 50:
#         return "Graduate"
    
#     # Detailed conditions based on attendance, GPA, study time, and failed subjects
#     if attendance_rate < 40:
#         if gpa < 5.0 or study_time < 5 or failed_subjects > 4:
#             return "Dropout"
#         return "Graduate"
    
#     if attendance_rate < 60:
#         if gpa < 6.0 or study_time < 10 or failed_subjects > 3:
#             return "Dropout"
#         return "Graduate"
    
#     if gpa < 4.0:
#         return "Dropout"
    
#     if study_time < 5:
#         if failed_subjects > 3:
#             return "Dropout"
#         return "Graduate"
    
#     if failed_subjects > 3:
#         return "Dropout"
    
#     # Additional conditions for other factors
#     if income_level < 20:
#         return "Dropout"
    
#     if extracurricular_participation < 2:
#         return "Dropout"
    
#     if living_conditions < 3:
#         return "Dropout"
    
#     return "Graduate"

# # Predict button
# if st.button('Predict'):
#     result = predict_outcome(attendance_rate, gpa, study_time, failed_subjects, income_level, extracurricular_participation, living_conditions)
#     color = 'green' if result == 'Graduate' else 'red'
#     st.markdown(f'<div style="color: {color}; font-size: 24px;">The predicted outcome is: {result}</div>', unsafe_allow_html=True)


#vallabh code
import streamlit as st

# Streamlit UI
st.title('Student Prediction App')

st.header('Enter Student Information')

# Create input fields for the features
age = st.number_input('Age', min_value=15, max_value=100, value=18)
attendance_rate = st.number_input('Attendance Rate (%)', min_value=0.0, max_value=100.0, value=75.0)
gpa = st.number_input('GPA (out of 10)', min_value=0.0, max_value=10.0, value=6.5)
study_time = st.number_input('Study Time (hours per week)', min_value=0, max_value=50, value=20)
parent_education_level = st.number_input('Parent Education Level (1-5)', min_value=1, max_value=5, value=3)
income_level = st.number_input('Income Level (1-100)', min_value=1, max_value=100, value=50)
failed_subjects = st.number_input('Number of Failed Subjects', min_value=0, max_value=10, value=1)
extracurricular_participation = st.number_input('Extracurricular Participation (1-5)', min_value=1, max_value=5, value=3)
living_conditions = st.number_input('Living Conditions (1-5)', min_value=1, max_value=5, value=3)
gender = st.selectbox('Gender', ['Male', 'Female'])

# Encode gender as 0 (Female) and 1 (Male)
gender_encoded = 1 if gender == 'Male' else 0

# Improved prediction logic to mimic ML behavior
def predict_outcome(attendance_rate, gpa, study_time, failed_subjects, income_level, extracurricular_participation, 
                   living_conditions, parent_education_level, gender_encoded):
    # If GPA is very high and study time is consistent, likely to graduate
    if gpa >= 8.5 and study_time >= 15 and failed_subjects <= 1:
        return "Graduate"
    
    # Very low attendance coupled with low GPA and failed subjects suggests dropout
    if attendance_rate < 35 and gpa < 5.0 and failed_subjects >= 3:
        return "Dropout"
    
    # Attendance below 50 and GPA lower than 6 are significant dropout indicators
    if attendance_rate < 50 and gpa < 6.0:
        if study_time < 10 or failed_subjects >= 3:
            return "Dropout"
        return "Graduate"
    
    # If attendance is between 50 and 70, GPA between 5 and 7, look at other factors
    if 50 <= attendance_rate <= 70:
        if gpa >= 7.0 and study_time >= 12:
            return "Graduate"
        if parent_education_level >= 4 and extracurricular_participation >= 3:
            return "Graduate"
        if failed_subjects >= 2 or living_conditions < 3:
            return "Dropout"
    
    # High-income level can help overcome poor performance in some cases
    if income_level > 80 and gpa >= 6.0 and attendance_rate > 60:
        return "Graduate"
    
    # If both extracurricular and parent education level are very low, even a decent GPA may not help
    if extracurricular_participation <= 2 and parent_education_level <= 2:
        return "Dropout"
    
    # If study time is extremely low, it becomes a strong dropout indicator regardless of GPA
    if study_time < 5:
        return "Dropout"
    
    # Consider gender-based biases (optional)
    if gender_encoded == 0 and income_level < 30:
        if attendance_rate < 60:
            return "Dropout"
    
    # Safe fallback: If most conditions are moderate
    if gpa >= 6.0 and attendance_rate >= 60 and failed_subjects <= 2:
        return "Graduate"
    
    return "Graduate"  # Default to Graduate if no strong dropout indicators

# Predict button
if st.button('Predict'):
    result = predict_outcome(attendance_rate, gpa, study_time, failed_subjects, income_level, 
                             extracurricular_participation, living_conditions, parent_education_level, gender_encoded)
    color = 'green' if result == 'Graduate' else 'red'
    st.markdown(f'<div style="color: {color}; font-size: 24px;">The predicted outcome is: {result}</div>', unsafe_allow_html=True)
