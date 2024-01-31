import pandas as pd

#Write a Pandas program to convert year-month string to dates adding a specified day of the month.
year_month_strings = pd.Series(['2022-01', '2022-02', '2022-03', '2022-04'])
specified_day = 6

dates_with_specified_day = pd.to_datetime(year_month_strings + '-' + str(specified_day), format='%Y-%m-%d')

result_df = pd.DataFrame({
    'Year-Month String': year_month_strings,
    'Converted Date': dates_with_specified_day
})

print(result_df)
