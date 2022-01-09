def avg(data):
    sum=0
    for i in range(0,data["count"]):
            sum += data["employees"][i]["salary"]
    print(sum/data["count"])  
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        },
]
})
