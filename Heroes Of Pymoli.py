# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
df = pd.read_csv(file_to_load)

# Display the total number of players
player_count = len(df['SN'].value_counts())

player_count_df = pd.DataFrame({"Total number of players:": [player_count]})
player_count_df

# Run basic calculations to obtain number of unique items, average price, etc.

unique_items = len(df['Item ID'].value_counts())
average_price = df['Price'].mean()
purchases = df['Item ID'].count()
revenue = df['Price'].sum()

summary_df = pd.DataFrame({"Unique Items": [unique_items], 
                           "Average Price": [average_price],
                           "Number of Purchases": [purchases], 
                           "Total Revenue": [revenue]})
summary_df

# Gender Analysis
# # group by gender & count
gender_grouped = df[["SN", "Gender"]]

# utilize .drop_duplicates to strip "repetitive players"
gender_grouped = gender_grouped.drop_duplicates()
gender_count = gender_grouped["Gender"].value_counts()

# List of values
total_count_by_group = [gender_count['Male'],gender_count['Female'],gender_count['Other / Non-Disclosed']]
percentage_by_group = [round((gender_count['Male']/player_count)*100,2),
                       round((gender_count['Female']/player_count)*100,2),
                       round((gender_count['Other / Non-Disclosed']/player_count)*100,2)]

# Creating DataFrame & setting index
gender_demographics_df = pd.DataFrame({"Total Count": total_count_by_group, "Percentage of Players": percentage_by_group})

gender_demographics_df.index = (["Male", "Female", "Other / Non-Disclosed"])
gender_demographics_df

#Purchasing Analaysis
gender_grouped = df[["SN","Gender","Price"]]
counts_g = gender_grouped["Gender"].value_counts()

# Purchase counts
purchase_counts = [counts_g[0],counts_g[1],counts_g[2]]

gender_grouped = gender_grouped.groupby("Gender")
total_spent = gender_grouped.sum()
total_spent

# Average Purchase Price
avg_purchase_g = [total_spent.iloc[1,0]/counts_g[1], 
                  total_spent.iloc[0,0]/counts_g[0], 
                  total_spent.iloc[2,0]/counts_g[2]]

# Total Purchase Value
total_purchase_value_g = [total_spent.iloc[1,0], 
                          total_spent.iloc[0,0], 
                          total_spent.iloc[2,0]]

# Normalized Totals
avg_total_g = [total_spent.iloc[1,0]/gender_count[1], 
              total_spent.iloc[0,0]/gender_count[0], 
              total_spent.iloc[2,0]/gender_count[2]]

# Creating DataFrame & setting index
purchase_analysis_g_df = pd.DataFrame({
    "Purchase Count": purchase_counts,
    "Average Purchase Price": avg_purchase_g,
    "Total Purchase Value": total_purchase_value_g,
    "Average Total Purchase/Person": avg_total_g,
    "Gender": ["Male", "Female", "Other / Non-Disclosed"]
})
purchase_analysis_g_df = purchase_analysis_g_df.set_index("Gender")
purchase_analysis_g_df = purchase_analysis_g_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value",
                                                 "Average Total Purchase/Person"]]

purchase_analysis_g_df

# Age Demographics
df2 = df[["SN","Age"]]
df2 = df2.drop_duplicates()

# Player age count
age_10 = df2[df2["Age"] < 10].count()[0]
age_14 = df2[(df2["Age"] >= 10) & (df2["Age"] <= 14)].count()[0]
age_19 = df2[(df2["Age"] >= 15) & (df2["Age"] <= 19)].count()[0]
age_24 = df2[(df2["Age"] >= 20) & (df2["Age"] <= 24)].count()[0]
age_29 = df2[(df2["Age"] >= 25) & (df2["Age"] <= 29)].count()[0]
age_34 = df2[(df2["Age"] >= 30) & (df2["Age"] <= 34)].count()[0]
age_39 = df2[(df2["Age"] >= 35) & (df2["Age"] <= 39)].count()[0]
age_40 = df2[df2["Age"] >= 40].count()[0]
player_ages = [age_10, age_14, age_19, age_24, age_29, age_34, age_39, age_40]

# Player age count percentages
percent_10 = round((age_10/player_count)*100,2)
percent_14 = round((age_14/player_count)*100,2)
percent_19 = round((age_19/player_count)*100,2)
percent_24 = round((age_24/player_count)*100,2)
percent_29 = round((age_29/player_count)*100,2)
percent_34 = round((age_34/player_count)*100,2)
percent_39 = round((age_39/player_count)*100,2)
percent_40 = round((age_40/player_count)*100,2)
percent_ages = [percent_10, percent_14, percent_19, percent_24, percent_29, percent_34, percent_39, percent_40]

# Create dictionary for ages/%
age_demographics = {"Total Count": player_ages,
            "Percent of Players": percent_ages}
    
# Creating DataFrame & setting index
age_demographics_df = pd.DataFrame(age_demographics)
age_demographics_df.index = (["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "> 40"])
age_demographics_df

#Purchasing Analysis for Age

# Purchase Count
purchase_10 = df[df["Age"] < 10].count()[0]
purchase_14 = df[(df["Age"] >= 10) & (df["Age"] <= 14)].count()[0]
purchase_19 = df[(df["Age"] >= 15) & (df["Age"] <= 19)].count()[0]
purchase_24 = df[(df["Age"] >= 20) & (df["Age"] <= 24)].count()[0]
purchase_29 = df[(df["Age"] >= 25) & (df["Age"] <= 29)].count()[0]
purchase_34 = df[(df["Age"] >= 30) & (df["Age"] <= 34)].count()[0]
purchase_39 = df[(df["Age"] >= 35) & (df["Age"] <= 39)].count()[0]
purchase_40 = df[df["Age"] >= 40].count()[0]
purchases_age = [purchase_10, purchase_14, purchase_19, purchase_24, purchase_29, purchase_34, purchase_39, purchase_40]

# Total Purchase Value
total_10 = df.loc[df['Age'] < 10, 'Price'].sum()
total_14 = df.loc[(df['Age'] >= 10) & (df['Age'] <=14), 'Price'].sum()
total_19 = df.loc[(df['Age'] >= 15) & (df['Age'] <=19), 'Price'].sum()
total_24 = df.loc[(df['Age'] >= 20) & (df['Age'] <=24), 'Price'].sum()
total_29 = df.loc[(df['Age'] >= 25) & (df['Age'] <=29), 'Price'].sum()
total_34 = df.loc[(df['Age'] >= 30) & (df['Age'] <=34), 'Price'].sum()
total_39 = df.loc[(df['Age'] >= 35) & (df['Age'] <=39), 'Price'].sum()
total_40 = df.loc[df['Age'] >= 40, 'Price'].sum()
totals_age = [total_10, total_14, total_19, total_24, total_29, total_34, total_39, total_40]

# Average Purchase Price
avg_price_age = [total_10/purchase_10, total_14/purchase_14, total_19/purchase_19, total_24/purchase_24, total_29/purchase_29,
              total_34/purchase_34, total_39/purchase_39, total_40/purchase_40]

# Normalized Totals
avg_total_purchase_person = [total_10/age_10, total_14/age_14, total_19/age_19, total_24/age_24, total_29/age_29, total_34/age_34,
           total_39/age_39, total_40/age_40]

# Creating dictionary
puchase_analysis_age = {"Purchase Count": purchases_age,
                        "Average Purchase Price": avg_price_age,
                        "Total Purchase Value": totals_age,
                        "Average Total Purchase per Person": avg_total_purchase_person}

# Creating DataFrame & setting index
purchase_analysis_age_df = pd.DataFrame(puchase_analysis_age)
purchase_analysis_age_df = purchase_analysis_age_df[['Purchase Count', 'Average Purchase Price', 'Total Purchase Value',
                                                     'Average Total Purchase per Person']]
purchase_analysis_age_df.index = (["<10", "10-14","15-19","20-24","25-29","30-34","34-39",">40"])
purchase_analysis_age_df

# Top Spenders

df3 = df[["SN","Price","Item Name"]]
total_spent = df3.groupby("SN").sum()
total_spent.sort_values(by = "Price", ascending = False, inplace = True)

# Top Spender SN
names = list(total_spent.index.values)
top_names = [names[0],names[1],names[2],names[3],names[4]]

# Total Purchase Values
total_purchase_values_1 = total_spent.iloc[0,0]
total_purchase_values_2 = total_spent.iloc[1,0]
total_purchase_values_3 = total_spent.iloc[2,0]
total_purchase_values_4 = total_spent.iloc[3,0]
total_purchase_values_5 = total_spent.iloc[4,0]
top_purchase_values = [total_spent.iloc[0,0], 
                       total_spent.iloc[1,0], 
                       total_spent.iloc[2,0], 
                       total_spent.iloc[3,0],
                       total_spent.iloc[4,0]]

# Purchase Counts
top_purchase_counts_1 = df3[df3["SN"] == names[0]].count()[0]
top_purchase_counts_2 = df3[df3["SN"] == names[1]].count()[0]
top_purchase_counts_3 = df3[df3["SN"] == names[2]].count()[0]
top_purchase_counts_4 = df3[df3["SN"] == names[3]].count()[0]
top_purchase_counts_5 = df3[df3["SN"] == names[4]].count()[0]
top_purchase_counts = [top_purchase_counts_1, 
                       top_purchase_counts_2, 
                       top_purchase_counts_3, 
                       top_purchase_counts_4,
                       top_purchase_counts_5]

# Average Purchas Prices
avg_price_1 = total_purchase_values_1/top_purchase_counts_1
avg_price_2 = total_purchase_values_2/top_purchase_counts_2
avg_price_3 = total_purchase_values_3/top_purchase_counts_3
avg_price_4 = total_purchase_values_4/top_purchase_counts_4
avg_price_5 = total_purchase_values_5/top_purchase_counts_5
avg_prices = [avg_price_1, avg_price_2, avg_price_3, avg_price_4, avg_price_5]

# Dictionary of values
top_spenders_dict = {"Purchase Count": top_purchase_counts,
                     "Average Purchase Price": avg_prices,
                     "Total Purchase Value": top_purchase_values,
                     "SN": top_names}

# Creating DataFrame & setting index
top_spenders_df = pd.DataFrame(top_spenders_dict)
top_spenders_df = top_spenders_df.set_index("SN")
top_spenders_df = top_spenders_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]
top_spenders_df

# Most Popular Items

df4 = df[["Item ID", "Item Name", "Price"]]
pop_items = df4.groupby("Item ID").count()
pop_items.sort_values(by = "Item Name", ascending = False, inplace = True)
df4 = df4.drop_duplicates(["Item ID", "Item Name"])

# Item IDs
item_ids = [pop_items.index[0], 
            pop_items.index[1], 
            pop_items.index[2], 
            pop_items.index[3], 
            pop_items.index[4]]

# Item Names
name_1 = df4.loc[df4["Item ID"] == item_ids[0], "Item Name"].item()
name_2 = df4.loc[df4["Item ID"] == item_ids[1], "Item Name"].item()
name_3 = df4.loc[df4["Item ID"] == item_ids[2], "Item Name"].item()
name_4 = df4.loc[df4["Item ID"] == item_ids[3], "Item Name"].item()
name_5 = df4.loc[df4["Item ID"] == item_ids[4], "Item Name"].item()
pop_item_names = [name_1, name_2, name_3, name_4, name_5]

# Purchase Counts
item_counts = [pop_items.iloc[0,0], 
               pop_items.iloc[1,0], 
               pop_items.iloc[2,0], 
               pop_items.iloc[3,0], 
               pop_items.iloc[4,0]]

# Item Prices
price_1 = df4.loc[df4["Item Name"] == pop_item_names[0], "Price"].item()
price_2 = df4.loc[df4["Item Name"] == pop_item_names[1], "Price"].item()
price_3 = df4.loc[df4["Item Name"] == pop_item_names[2], "Price"].item()
price_4 = df4.loc[df4["Item Name"] == pop_item_names[3], "Price"].item()
price_5 = df4.loc[df4["Item Name"] == pop_item_names[4], "Price"].item()
item_prices = [price_1,price_2,price_3,price_4,price_5]

# Total Purchase Value
total_values = [pop_items.iloc[0,0]*price_1, 
                pop_items.iloc[1,0]*price_2, 
                pop_items.iloc[2,0]*price_3, 
                pop_items.iloc[3,0]*price_4, 
                pop_items.iloc[4,0]*price_5]

# Creating DataFrame & setting index
pop_items_df = pd.DataFrame({
    "Item ID": item_ids,
    "Item Name": pop_item_names,
    "Purchase Count": item_counts,
    "Item Price": item_prices,
    "Total Purchase Value": total_values
})
pop_items_df = pop_items_df.set_index(["Item ID", "Item Name"])
pop_items_df = pop_items_df[["Purchase Count", "Item Price", "Total Purchase Value"]]
pop_items_df

# Most Profitable Items

df4 = df[["Item ID", "Item Name", "Price"]]
profit_items = df4.groupby("Item ID").sum()
profit_items.sort_values(by = "Price", ascending = False, inplace = True)
df4 = df4.drop_duplicates(["Item ID", "Price"])

# Item IDs
item_ids = [profit_items.index[0], profit_items.index[1], profit_items.index[2], profit_items.index[3], profit_items.index[4]]

# Item Names
name_1 = df4.loc[df4["Item ID"] == item_ids[0], "Item Name"].item()
name_2 = df4.loc[df4["Item ID"] == item_ids[1], "Item Name"].item()
name_3 = df4.loc[df4["Item ID"] == item_ids[2], "Item Name"].item()
name_4 = df4.loc[df4["Item ID"] == item_ids[3], "Item Name"].item()
name_5 = df4.loc[df4["Item ID"] == item_ids[4], "Item Name"].item()
profit_names = [name_1, name_2, name_3, name_4, name_5]

# Total Purchase Value
values = [profit_items.iloc[0,0],
          profit_items.iloc[1,0],
          profit_items.iloc[2,0],
          profit_items.iloc[3,0],
          profit_items.iloc[4,0]]

# Item Price
price_1 = df4.loc[df4["Item ID"] == item_ids[0], "Price"].item()
price_2 = df4.loc[df4["Item ID"] == item_ids[1], "Price"].item()
price_3 = df4.loc[df4["Item ID"] == item_ids[2], "Price"].item()
price_4 = df4.loc[df4["Item ID"] == item_ids[3], "Price"].item()
price_5 = df4.loc[df4["Item ID"] == item_ids[4], "Price"].item()
profit_prices = [price_1,price_2,price_3,price_4,price_5]

# Purchase counts
df5 = df[["Item ID", "Item Name", "Price"]].groupby("Item Name").count()
count_1 = df5.loc[df5.index == profit_names[0], "Item ID"].item()
count_2 = df5.loc[df5.index == profit_names[1], "Item ID"].item()
count_3 = df5.loc[df5.index == profit_names[2], "Item ID"].item()
count_4 = df5.loc[df5.index == profit_names[3], "Item ID"].item()
count_5 = df5.loc[df5.index == profit_names[4], "Item ID"].item()
counts = [count_1, count_2, count_3, count_4, count_5]

# Creating DataFrame & setting index
profit_items_df = pd.DataFrame({
    "Item ID": item_ids,
    "Item Name": profit_names,
    "Purchase Count": counts,
    "Item Price": profit_prices,
    "Total Purchase Value": values
})
profit_items_df = profit_items_df.set_index(["Item ID", "Item Name"])
profit_items_df = profit_items_df[["Purchase Count", "Item Price", "Total Purchase Value"]]
profit_items_df