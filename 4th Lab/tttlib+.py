class ttt:

 T=[0,0,0,0,0,0,0,0,0]
 
#printBoard
 def printBoard(self):
     L=[0,1,2,3,4,5,6,7,8]    
     for i in range(0,9):
         if(len(T)!=9)or((T[i]!=1)and(T[i]!=2)and(T[i]!=0)):
             return(False)
         else:
              if T[i]==0:
                 L[i]=i
              elif T[i]==1:
                 L[i]='X'
              elif T[i]==2:
                 L[i]='O'

     print (L[0],'|',L[1],'|',L[2])
     print ('---|---|---')
     print (L[3],'|',L[4],'|',L[5])
     print ('---|---|---') 
     print (L[6],'|',L[7],'|',L[8])
     return(True)


#analyzeBoard(T)
 def analyzeBoard(self):
     for i in range(0,9):
         if(len(T)!=9)or((T[i]!=1)and(T[i]!=2)and(T[i]!=0)):
             return(-1)
         else:
            if(T[0]==T[1]==T[2]==1)or(T[3]==T[4]==T[5]==1)or(T[6]==T[7]==T[8]==1)or(T[0]==T[3]==T[6]==1)or(T[1]==T[4]==T[7]==1)or(T[2]==T[5]==T[8]==1)or(T[0]==T[4]==T[8]==1)or(T[6]==T[4]==T[2]==1):
                return(1)
            if(T[0]==T[1]==T[2]==2)or(T[3]==T[4]==T[5]==2)or(T[6]==T[7]==T[8]==2)or(T[0]==T[3]==T[6]==2)or(T[1]==T[4]==T[7]==2)or(T[2]==T[5]==T[8]==2)or(T[0]==T[4]==T[8]==2)or(T[6]==T[4]==T[2]==2):
                return(2)
            else:
               if(T[0]!=0)and(T[1]!=0)and(T[2]!=0)and(T[3]!=0)and(T[4]!=0)and(T[5]!=0)and(T[6]!=0)and(T[7]!=0)and(T[8]!=0):
                   return(3)
               else:
                   return(0)



#Random Move
 def genRandomMove(self,player):
     for i in range(0,9):
          if(len(T)!=9)or((T[i]!=1)and(T[i]!=2)and(T[i]!=0)):
              return(-1)
     from random import randint
     Random_choose=randint(0,8)
     if(T[int(Random_choose)]!='1')and(T[int(Random_choose)]!='2'):
         return(Random_choose)
     else:
         return(-1)


#Wining Move
 def genWinningMove(self,player):
      for i in range(0,9):
           if(len(T)!=9)or((T[i]!=1)and(T[i]!=2)and(T[i]!=0)):
               return(-1)
      if((player!=1)and(player!=2)):
         return(-1)
      else:
	      if(player==1):
		      if((T[0]==T[1]==1)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[2]==1)and(T[1]==0)):
			      return(1)
		      if((T[1]==T[2]==1)and(T[0]==0)):
			      return(0)
		      if((T[3]==T[4]==1)and(T[5]==0)):
			      return(5)
		      if((T[3]==T[5]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[5]==1)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[7]==1)and(T[8]==0)):
			      return(8)
		      if((T[6]==T[8]==1)and(T[7]==0)):
			      return(7)
		      if((T[7]==T[8]==1)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[3]==1)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[6]==1)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[3]==1)and(T[0]==0)):
			      return(0)
		      if((T[1]==T[4]==1)and(T[7]==0)):
			      return(7)
		      if((T[1]==T[7]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[7]==1)and(T[1]==0)):
			      return(1)
		      if((T[2]==T[5]==1)and(T[8]==0)):
			      return(8)
		      if((T[2]==T[8]==1)and(T[5]==0)):
			      return(5)
		      if((T[5]==T[8]==1)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[4]==1)and(T[8]==0)):
			      return(8)
		      if((T[0]==T[8]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[8]==1)and(T[0]==0)):
			      return(0)
		      if((T[6]==T[4]==1)and(T[2]==0)):
			      return(2)
		      if((T[6]==T[2]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[2]==1)and(T[6]==0)):
			      return(6)
	      if(player==2):
		      if((T[0]==T[1]==2)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[2]==2)and(T[1]==0)):
			      return(1)
		      if((T[1]==T[2]==2)and(T[0]==0)):
			      return(0)
		      if((T[3]==T[4]==2)and(T[5]==0)):
			      return(5)
		      if((T[3]==T[5]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[5]==2)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[7]==2)and(T[8]==0)):
			      return(8)
		      if((T[6]==T[8]==2)and(T[7]==0)):
			      return(7)
		      if((T[7]==T[8]==2)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[3]==2)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[6]==2)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[3]==2)and(T[0]==0)):
			      return(0)
		      if((T[1]==T[4]==2)and(T[7]==0)):
			      return(7)
		      if((T[1]==T[7]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[7]==2)and(T[1]==0)):
			      return(1)
		      if((T[2]==T[5]==2)and(T[8]==0)):
			      return(8)
		      if((T[2]==T[8]==2)and(T[5]==0)):
			      return(5)
		      if((T[5]==T[8]==2)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[4]==2)and(T[8]==0)):
			      return(8)
		      if((T[0]==T[8]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[8]==2)and(T[0]==0)):
			      return(0)
		      if((T[6]==T[4]==2)and(T[2]==0)):
			      return(2)
		      if((T[6]==T[2]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[2]==2)and(T[6]==0)):
			      return(6)

#NonLoser Move
 def genNonLoser(self,player):
      for i in range(0,9):
           if(len(T)!=9)or((T[i]!=1)and(T[i]!=2)and(T[i]!=0)):
               return(-1)
      if((player!=1)and(player!=2)):
         return(-1)
      else:
	      if(player==2):
		      if((T[0]==T[1]==1)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[2]==1)and(T[1]==0)):
			      return(1)
		      if((T[1]==T[2]==1)and(T[0]==0)):
			      return(0)
		      if((T[3]==T[4]==1)and(T[5]==0)):
			      return(5)
		      if((T[3]==T[5]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[5]==1)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[7]==1)and(T[8]==0)):
			      return(8)
		      if((T[6]==T[8]==1)and(T[7]==0)):
			      return(7)
		      if((T[7]==T[8]==1)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[3]==1)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[6]==1)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[3]==1)and(T[0]==0)):
			      return(0)
		      if((T[1]==T[4]==1)and(T[7]==0)):
			      return(7)
		      if((T[1]==T[7]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[7]==1)and(T[1]==0)):
			      return(1)
		      if((T[2]==T[5]==1)and(T[8]==0)):
			      return(8)
		      if((T[2]==T[8]==1)and(T[5]==0)):
			      return(5)
		      if((T[5]==T[8]==1)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[4]==1)and(T[8]==0)):
			      return(8)
		      if((T[0]==T[8]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[8]==1)and(T[0]==0)):
			      return(0)
		      if((T[6]==T[4]==1)and(T[2]==0)):
			      return(2)
		      if((T[6]==T[2]==1)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[2]==1)and(T[6]==0)):
			      return(6)
	      if(player==1):
		      if((T[0]==T[1]==2)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[2]==2)and(T[1]==0)):
			      return(1)
		      if((T[1]==T[2]==2)and(T[0]==0)):
			      return(0)
		      if((T[3]==T[4]==2)and(T[5]==0)):
			      return(5)
		      if((T[3]==T[5]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[5]==2)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[7]==2)and(T[8]==0)):
			      return(8)
		      if((T[6]==T[8]==2)and(T[7]==0)):
			      return(7)
		      if((T[7]==T[8]==2)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[3]==2)and(T[6]==0)):
			      return(6)
		      if((T[0]==T[6]==2)and(T[3]==0)):
			      return(3)
		      if((T[6]==T[3]==2)and(T[0]==0)):
			      return(0)
		      if((T[1]==T[4]==2)and(T[7]==0)):
			      return(7)
		      if((T[1]==T[7]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[7]==2)and(T[1]==0)):
			      return(1)
		      if((T[2]==T[5]==2)and(T[8]==0)):
			      return(8)
		      if((T[2]==T[8]==2)and(T[5]==0)):
			      return(5)
		      if((T[5]==T[8]==2)and(T[2]==0)):
			      return(2)
		      if((T[0]==T[4]==2)and(T[8]==0)):
			      return(8)
		      if((T[0]==T[8]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[8]==2)and(T[0]==0)):
			      return(0)
		      if((T[6]==T[4]==2)and(T[2]==0)):
			      return(2)
		      if((T[6]==T[2]==2)and(T[4]==0)):
			      return(4)
		      if((T[4]==T[2]==2)and(T[6]==0)):
			      return(6)


#Move
 def Move(self,x,player):
     if(T[x]==0):
         self.T[x] = player
         return True
     else:
         return False
         

        
    
 
