import streamlit as st
from datetime import datetime, date
import calendar

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)
    
    age = today - birth_date
    age_years = age.days // 365
    age_months = (age.days % 365) // 30
    age_days = (age.days % 365) % 30
    
    total_months = age_years * 12 + age_months
    total_days = age.days
    total_hours = total_days * 24
    total_minutes = total_hours * 60
    total_seconds = total_minutes * 60
    
    next_birthday = date(today.year, birth_month, birth_day)
    if next_birthday <= today:
        next_birthday = date(today.year + 1, birth_month, birth_day)
    days_until_birthday = (next_birthday - today).days
    
    return {
        "years": age_years,
        "months": age_months,
        "days": age_days,
        "total_months": total_months,
        "total_days": total_days,
        "total_hours": total_hours,
        "total_minutes": total_minutes,
        "total_seconds": total_seconds,
        "days_until_birthday": days_until_birthday
    }

st.title("Age Calculator")

birth_year = st.number_input("Enter your birth year", min_value=1900, max_value=datetime.now().year, value=2000)
birth_month = st.selectbox("Select your birth month", range(1, 13), format_func=lambda x: calendar.month_name[x])

# Calculate the number of days in the selected month and year
_, days_in_month = calendar.monthrange(birth_year, birth_month)

birth_day = st.number_input("Enter your birth day", min_value=1, max_value=days_in_month, value=1)

if st.button("Calculate Age"):
    age_data = calculate_age(birth_year, birth_month, birth_day)
    
    st.header("You have been living for:")
    st.write(f"Your Age: {age_data['years']} years, {age_data['months']} months, and {age_data['days']} days")
    st.write(f"Months: {age_data['total_months']} months since your birth")
    st.write(f"Days: {age_data['total_days']} days since your birth")
    st.write(f"Hours: {age_data['total_hours']} hours since your birth")
    st.write(f"Minutes: {age_data['total_minutes']} minutes since your birth")
    st.write(f"Seconds: {age_data['total_seconds']} seconds since your birth")
    st.write(f"Next Birthday: {age_data['days_until_birthday']} days left for your next birthday")

st.sidebar.text("Created with Streamlit")