#include <stdio.h>

int anlboard( char *T, int sizeT );

int anlboard( char *T, int sizeT ){
  int i;
  for(i=0;i<10;i++){
  if((sizeT!=9)||((T[i]!='X')&&(T[i]!=2)&&(T[i]!=0))){
  return -1;}

  else{
  if((T[0]=='X' &&T[1]=='X' &&T[2]=='X')||(T[3]=='X' &&T[4]=='X' &&T[5]=='X')||(T[6]=='X' &&T[7]=='X' &&T[8]=='X')||(T[0]=='X' &&T[3]=='X' &&T[6]=='X')||(T[1]=='X' &&T[4]=='X' &&T[7]=='X')||(T[2]=='X' &&T[5]=='X' &&T[8]=='X')||(T[0]=='X' &&T[4]=='X' &&T[8]=='X')||(T[6]=='X' &&T[4]=='X' &&T[2]=='X')){
                return 1;}
  if((T[0]=='O' &&T[1]=='O' &&T[2]=='O')||(T[3]=='O' &&T[4]=='O' &&T[5]=='O' )||(T[6]=='O' &&T[7]=='O' &&T[8]=='O')||(T[0]=='O' &&T[3]=='O' &&T[6]=='O')||(T[1]=='O' &&T[4]=='O' &&T[7]=='O')||(T[2]=='O' &&T[5]=='O' &&T[8]=='O')||(T[0]=='O' &&T[4]=='O' &&T[8]=='O')||(T[6]=='O' &&T[4]=='O' &&T[2]=='O')){
                return 2;}
            else{
               if(T[0]!=0)&&(T[1]!=0)&&(T[2]!=0)&&(T[3]!=0)&&(T[4]!=0)&&(T[5]!=0)&&(T[6]!=0)&&(T[7]!=0)&&(T[8]!=0){
                   return 3;}
               else{
                   return 0;}}
  }
}
}
