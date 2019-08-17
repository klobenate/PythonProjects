friend_names = ["Joe", "Noah", "Jesse"]

friend_names.sort()


#consider print(sorted(friend_names)) -can except reverse=True
for name in friend_names:
	print(name)

friend_names.append("Jacob")

for name in friend_names:
	print("Hello:" + name)

friend_names.insert(0,"Isaiah")

friend_names.reverse()

for name in friend_names:
	print(name)

del friend_names[0]

for name in friend_names:
	print(name)


#consider .pop(idx)
removed_name = friend_names.pop()

for name in friend_names:
	print(name)

friend_names.remove("Noah")

for name in friend_names:
	print(name)

print(len(friend_names))