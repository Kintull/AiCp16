from PathFinder import PathFinder

triangle_blocks = [[(1,8),(1,2),(1,4)],
                           [(5,4),(2,1),(8,1)],
                           [(9,8),(6,5),(9,2)],
                           [(2,9),(5,6),(8,9)]]
PF  = PathFinder()
print PF.inTriangle((2,5),((1,8),(1,2),(4,5)))

