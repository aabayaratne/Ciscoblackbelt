Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

splitsesids=Sessions_Attended['sessions'].split(",")

print(splitsesids)
j=0
for i in splitsesids:
	if (i.isdecimal()):
		j=j+1

print("I have attended " + str(j) + " sessions!!")








