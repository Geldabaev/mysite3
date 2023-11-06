posts = ['python', "C++", "Dart"]
"list -это упорядоченный, изменяемый тип данных"

posts.append("C#")
print(posts[0])

posts = ["python", "c++", "kotlin", "java"]
posts2 = {'python': 'django', "c#": "pandas"}

test = {'posts': posts, "posts2": posts2}
print(type(test))
"dict -это изменяемый, неупорядоченный пары ключ и занчения"
print(test['posts2']["python"])


x3 = {'a': ['python', 'js', 'kotlin'], 'b': {'dart': 'flutter', 'python': 'django'}}




for i in 'yunus':
    print(i)

for i in range(10):
    print(i)

posts2 = {'python': 'django', "c#": "pandas"}
for post in posts2:
    print(posts2[post])
