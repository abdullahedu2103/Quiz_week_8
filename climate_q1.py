import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect("climate.db")
cursor = connection.cursor() 

cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
result = cursor.fetchall()

print("Year   | CO2    | Temperature")
print("-----------------------------")
for r in result:
    print(f"{r[0]:<7} | {r[1]:<7} | {r[2]:<11}")

years = []
co2 = []
temp = []

for r in result:
    year, co2_value, temp_value = r
    years.append(year)
    co2.append(co2_value)
    temp.append(temp_value)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.show()
plt.savefig("co2_temp_1.png")
