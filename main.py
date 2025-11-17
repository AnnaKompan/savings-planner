from tabulate import tabulate
import random

nums = [random.randint(50,650) for i in range(100)]
total = sum(nums)
scale = 40000/total
nums  = [round(n*scale) for n in nums]
diff = 40000 - sum(nums)
nums[0]+=diff
total2 = sum(nums)

print(scale, nums, total2)

table = [nums[i:i+10] for i in range(0, 100, 10)] #start stop step

table_html = tabulate(table, tablefmt="html")

html = f"""
<html>
<head>
    <title> Table </title>
    <style>
        table{{border-collapse: collapse;}}
        td,th {{border: 1px solid black; padding: 5px; text-align: center;}}
    </style>
</head>
<body>
    <h2>Random table that sums to {sum(nums)}</h2>
    {table_html}
</body>
</html>
"""

with open("table.html", "w") as f:
    f.write(html)

print("Page is saved as table.html")