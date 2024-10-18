students={'Jonny','Bilbo','Steve','Hendrik','Aaron'}
grade_marks=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
a=students
b=grade_marks
a=sorted(a)
print(a)
a0=a[0]
a1=a[1]
a2=a[2]
a3=a[3]
a4=a[4]
b[0]=Aarons_mark=float((sum(b[0]))/len(b[0]))
b[1]=Bilbos_mark=float((sum(b[1]))/len(b[1]))
b[2]=Hendriks_mark=float((sum(b[2]))/len(b[2]))
b[3]=Jonnys_mark=float((sum(b[3]))/len(b[3]))
b[4]=Steves_mark=float((sum(b[4]))/len(b[4]))
class_journal={a0:b[0],a1:b[1], a2:b[2],a3:b[3], a4:b[4]}
print(class_journal)



