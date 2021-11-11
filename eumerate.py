values = ["a", "b", "c"]

for value in values:
    print(value)

print("end")

for count, value in enumerate(values):
     print(count, value)

print(" ")

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favouriate food", "content": "I like pizza", "id": 2}]

for p in my_posts:
    if p["id"] == id:
        print(p)