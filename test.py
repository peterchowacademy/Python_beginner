# import string
# alphabet = set(string.ascii_uppercase)
# print(alphabet)

###how to display the content from dictionary/json
# dict = {
#     "title" : "this is a title",
#     "content" : "this is a content"
# }
# print(dict["content"])
# print(dict['title'])
# print(f"title is {dict['title']} and content is {dict['content']}")

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favouriate food", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
post = find_post(1)
print(post)