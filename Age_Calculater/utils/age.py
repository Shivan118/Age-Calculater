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