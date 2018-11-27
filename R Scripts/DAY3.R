student<-list(sname="Ram", rollno.="12", gender="male", marks=c(75,87,56,77,87))
mean(student$marks)
another<-c(student$rollno.,student$marks)
student$marks[5]=100
sub<-c("english","maths","hindi","science","french")
student [5]=sub
M<-matrix(1:4,nrow=2)

B=2*M
X<- matrix (c(1,1,3,5,2,6,-2,-1,-3),nrow=3,byrow=TRUE)
T<-X%*%X%*%X
P<- matrix (c(10,-10,10),nrow=15,ncol=3,byrow=TRUE)
Z<-t(P)
P%*%Z
O<- matrix ((1:15),nrow=3,ncol=5)
colnames(O)=c("p1", "p2", "p3", "p4", "p5")
rownames(O)=c("Alice", "Bill", "Sara")
avg<- c(mean(O[,1]),mean(O[,2]),mean(O[,3]),mean(O[,4]),mean(O[,5]))