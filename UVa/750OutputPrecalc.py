answers = [[0,1,5,8,6,3,7,2,4],[0,1,6,8,3,7,4,2,5],[0,1,7,4,6,8,2,5,3],[0,1,7,5,8,2,4,6,3],[0,2,4,6,8,3,1,7,5],[0,2,5,7,1,3,8,6,4],[0,2,5,7,4,1,8,6,3],[0,2,6,1,7,4,8,3,5],[0,2,6,8,3,1,4,7,5],[0,2,7,3,6,8,5,1,4],[0,2,7,5,8,1,4,6,3],[0,2,8,6,1,3,5,7,4],[0,3,1,7,5,8,2,4,6],[0,3,5,2,8,1,7,4,6],[0,3,5,2,8,6,4,7,1],[0,3,5,7,1,4,2,8,6],[0,3,5,8,4,1,7,2,6],[0,3,6,2,5,8,1,7,4],[0,3,6,2,7,1,4,8,5],[0,3,6,2,7,5,1,8,4],[0,3,6,4,1,8,5,7,2],[0,3,6,4,2,8,5,7,1],[0,3,6,8,1,4,7,5,2],[0,3,6,8,1,5,7,2,4],[0,3,6,8,2,4,1,7,5],[0,3,7,2,8,5,1,4,6],[0,3,7,2,8,6,4,1,5],[0,3,8,4,7,1,6,2,5],[0,4,1,5,8,2,7,3,6],[0,4,1,5,8,6,3,7,2],[0,4,2,5,8,6,1,3,7],[0,4,2,7,3,6,8,1,5],[0,4,2,7,3,6,8,5,1],[0,4,2,7,5,1,8,6,3],[0,4,2,8,5,7,1,3,6],[0,4,2,8,6,1,3,5,7],[0,4,6,1,5,2,8,3,7],[0,4,6,8,2,7,1,3,5],[0,4,6,8,3,1,7,5,2],[0,4,7,1,8,5,2,6,3],[0,4,7,3,8,2,5,1,6],[0,4,7,5,2,6,1,3,8],[0,4,7,5,3,1,6,8,2],[0,4,8,1,3,6,2,7,5],[0,4,8,1,5,7,2,6,3],[0,4,8,5,3,1,7,2,6],[0,5,1,4,6,8,2,7,3],[0,5,1,8,4,2,7,3,6],[0,5,1,8,6,3,7,2,4],[0,5,2,4,6,8,3,1,7],[0,5,2,4,7,3,8,6,1],[0,5,2,6,1,7,4,8,3],[0,5,2,8,1,4,7,3,6],[0,5,3,1,6,8,2,4,7],[0,5,3,1,7,2,8,6,4],[0,5,3,8,4,7,1,6,2],[0,5,7,1,3,8,6,4,2],[0,5,7,1,4,2,8,6,3],[0,5,7,2,4,8,1,3,6],[0,5,7,2,6,3,1,4,8],[0,5,7,2,6,3,1,8,4],[0,5,7,4,1,3,8,6,2],[0,5,8,4,1,3,6,2,7],[0,5,8,4,1,7,2,6,3],[0,6,1,5,2,8,3,7,4],[0,6,2,7,1,3,5,8,4],[0,6,2,7,1,4,8,5,3],[0,6,3,1,7,5,8,2,4],[0,6,3,1,8,4,2,7,5],[0,6,3,1,8,5,2,4,7],[0,6,3,5,7,1,4,2,8],[0,6,3,5,8,1,4,2,7],[0,6,3,7,2,4,8,1,5],[0,6,3,7,2,8,5,1,4],[0,6,3,7,4,1,8,2,5],[0,6,4,1,5,8,2,7,3],[0,6,4,2,8,5,7,1,3],[0,6,4,7,1,3,5,2,8],[0,6,4,7,1,8,2,5,3],[0,6,8,2,4,1,7,5,3],[0,7,1,3,8,6,4,2,5],[0,7,2,4,1,8,5,3,6],[0,7,2,6,3,1,4,8,5],[0,7,3,1,6,8,5,2,4],[0,7,3,8,2,5,1,6,4],[0,7,4,2,5,8,1,3,6],[0,7,4,2,8,6,1,3,5],[0,7,5,3,1,6,8,2,4],[0,8,2,4,1,7,5,3,6],[0,8,2,5,3,1,7,4,6],[0,8,3,1,6,2,5,7,4],[0,8,4,1,3,6,2,7,5]]

T = int(input())
for t in range(T):
  inp = []
  while (len(inp) == 0):
    inp = [int(a) for a in input().split()]
  targetR = inp[0]
  targetC = inp[1]
  if (t != 0):
      print("")
    
  print("SOLN       COLUMN")
  print(" #      1 2 3 4 5 6 7 8\n")

  solnNo = 1
  for soln in answers:
    if soln[targetC] == targetR: #good
      if (solnNo < 10):
        print(" ",end="")
      print("%d      %d %d %d %d %d %d %d %d" % (solnNo,soln[1],soln[2],soln[3],soln[4],soln[5],soln[6],soln[7],soln[8]))
      solnNo = solnNo + 1;
    