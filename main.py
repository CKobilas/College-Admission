TestScore = float(input("Enter your Test Score: "))
ClassRank = float(input("Enter your Class Rank: "))

if TestScore >= 90 and ClassRank >= 25:
    output = "Accept"
elif TestScore >= 80 and ClassRank >= 50:
    output = "Accept"
elif TestScore >= 70 and ClassRank >= 75:
    output = "Accept"
else:
    output = "Reject"

print(output)
    
  
 