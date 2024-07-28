



five =[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

for i in five:
    print(i)



"""

[131, 673, 234, 103, 18]
[201, 96, 342, 965, 150]
[630, 803, 746, 422, 111]
[537, 699, 497, 121, 956]
[805, 732, 524, 37, 331]



Staring from the top left
Find the lowest cost to move to each value.

So obviously top left is what it is 131.
Then items 1,0 and 0,1
So to get to 201 it costs 201+131 = 332
And item 673 costs 673+131 = 804

So now our grid looks like

[131, 332, 234, 103, 18]
[804, 96, 342, 965, 150]
[630, 803, 746, 422, 111]
[537, 699, 497, 121, 956]
[805, 732, 524, 37, 331]


So what is the cheapest way now to get to 96.
Start at either 332 or 804 and find out.
And well obviously the cheapest way is from 332.
So now our grid is

[131, 332, 234, 103, 18]
[804, 428, 342, 965, 150]
[630, 803, 746, 422, 111]
[537, 699, 497, 121, 956]
[805, 732, 524, 37, 331]

Then go down in an J fashion. From 234 down and to the left up untill 630.
Also I can manipulate the grid in place, since if I know the cheapest way to get to 234, that will affect the path to 342.


Also I may want to manipulate the grid beforehand.
Change certain values. And create a list of lists, of lists.
So back to the grid.
[[131,0], [332,1],
[[804,1], [96,2],

Where 0 means the value is locked and the fastest path is found for it and the value is no longer a starting point.
1 means the cheapest value has been found and it is still used as a starting point.
2 means it is just a regular value that hasn't been used to find the fastest point.


Basic Idea
[1, 8, 234, 103, 18]
[3, 1, 1, 965, 150]
[630, 803, 746, 422, 111]
[537, 699, 497, 121, 956]
[805, 732, 524, 37, 331]

So let's say that we are starting at 234.
So the direct way is from 8. However that is not the shortest route.
The other starting position are 3 and 1, from the same J formation as 234.
So I need to look at all routes from those locations.
So let's try 3.
Going down is higher than 8+234. So I knock that off the list of potential directions.
Then try right, which is smaller. Down is more, Up is more, right works. And from that position the fastest is Up.
So the new lowest is 3+1+1+234.
Then I try from the other starting position 1.
So Up is too much it is greater than the new lowest path.
Left is ok.
however from there everything is too much to I can't go left.
Down is too much.
Right is ok. And same idea keep trying all paths.





"""


















