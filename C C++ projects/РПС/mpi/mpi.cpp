#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>
#include <math.h>
#include <stdbool.h>
#include "mpi.h"
#define WRITETOGNUPOT
double dx;
double dy;
double dt;
#define F(x,y,t) 0
#define A 0.5
#define LENGTHX 20
#define LENGTHY 20
#define LENGTHT 200
#define LEFT 1
#define RIGHT 2
double dx2;
double dy2;
double dt2;
double a2 ;
struct timeval tv1,tv2,dtv;
struct timezone tz;
void time_start() { gettimeofday(&tv1, &tz); }
int time_stop(){ 
gettimeofday(&tv2, &tz);
dtv.tv_sec= tv2.tv_sec -tv1.tv_sec;
dtv.tv_usec=tv2.tv_usec-tv1.tv_usec;
if(dtv.tv_usec<0) { dtv.tv_sec--; dtv.tv_usec+=1000000; }
return dtv.tv_sec*1000+dtv.tv_usec/1000;}
FILE *out,*fp;
void writeIntoFile(double* Z,int lengthX, int lengthY,double CurrentTime){
int i,k;
for(k=0;k<lengthY-1;k++)
{
for(i=0;i<lengthX-1;i++)
fprintf(out,"%d\t%d\t%lf\n",i*(int)dx,k*(int)dy,Z[k*lengthX+i]);
fprintf(out,"\n");}
fprintf(out, "\n\n"); }
void openFiles(int timeInterval){
out = fopen("out.txt","w");
fp = fopen("vgraph0.dat","w"); 
fprintf(fp,"set xrange [0:%d]\n", (int)LENGTHX-(int) dx );
fprintf(fp,"set yrange [0:%d]\n", (int)LENGTHY-(int) dy );
fprintf(fp,"set zrange [-2:2]\n");
fprintf(fp, "do for [i=0:%d]{\n", (int)LENGTHT-1);
fprintf(fp,"splot 'out.txt' index i using 1:2:3 with lines\npause 0.1}\n\n");}
void calculateFisrtTime(double* Z0,double* Z1,int lengthX,int lengthY){
10
int i,k;
for(k=0;k<lengthY;k++){
for(i=0;i<lengthX;i++){
Z0[k*lengthX + i] = Z1[k*lengthX + i] = 1;} }
#ifdef WRITETOGNUPOT
writeIntoFile(Z0,lengthX,lengthY,0);
#endif}
void calculate(double* Z0,double* Z1,int lengthX,int lengthY,double CurrentTime,int myrank,int 
total,double* zleft, double* zright)
{
int i,k;
int index;
for(k=1;k<lengthY-1;k++){
if ( myrank!= 0 ){
index = k*lengthX; 
Z1[index] = dt2*a2 * ( (zleft[k-1]-2*Z0[index]+Z0[index+1])/dx2 + (Z0[index+lengthX]-
2*Z0[index]+Z0[index-lengthX])/dy2 ) + 2*Z0[index]-Z1[index];
zleft[k-1] = Z1[index];}
for(i=1;i<lengthX-1;i++) {index = k*lengthX+i;
Z1[index] = dt2*a2 * ( (Z0[index-1]-2*Z0[index]+Z0[index+1])/dx2 + (Z0[index+lengthX]-
2*Z0[index]+Z0[index-lengthX])/dy2 ) + 2*Z0[index]-Z1[index]; }
if ( myrank!= total-1 ){
index = k*lengthX+lengthX-1;
Z1[index] = dt2*a2 * ( (Z0[index-1]-2*Z0[index]+zright[k-1])/dx2 + (Z0[index+lengthX]-
2*Z0[index]+Z0[index-lengthX])/dy2 ) + 2*Z0[index]-Z1[index];
zright[k-1] = Z1[index];}}
if( myrank!= total-1){ 
MPI_Send((void*)zright,lengthY-2,MPI_DOUBLE,myrank+1,LEFT,MPI_COMM_WORLD);
MPI_Recv((void*)zright,lengthY2,MPI_DOUBLE,myrank+1,RIGHT,MPI_COMM_WORLD,MPI_STATUS_IGNORE);}
if( myrank!= 0){
MPI_Send((void*)zleft,lengthY-2,MPI_DOUBLE,myrank-1,RIGHT,MPI_COMM_WORLD); 
MPI_Recv((void*)zleft,lengthY-2,MPI_DOUBLE,myrank1,LEFT,MPI_COMM_WORLD,MPI_STATUS_IGNORE); } }
int main(int argc, char **argv) {
int myrank, total; 
if ( argc < 4){printf("./a.out #lengthX #lengthY #timeInterval\n");exit(0);}
int lengthX = atoi(argv[1]);
int lengthY = atoi(argv[2]);
double timeInterval = atof(argv[3]); 
if(lengthX > LENGTHX)dx = 1.0;
else dx = LENGTHX / lengthX;
if(lengthY > LENGTHY)dy = 1.0;
else dy = LENGTHY / lengthY;
if(timeInterval > LENGTHT)dt = 1.0;
else dt = timeInterval / LENGTHT;
dx2 = dx*dx;
dy2 = dy*dy;
dt2 = dt*dt;
a2 = A*A;
double* Z0;
double* Z1;
11
double CurrentTime = dt;
int znumber=1; 
MPI_Init (&argc, &argv);
MPI_Comm_size (MPI_COMM_WORLD, &total);
MPI_Comm_rank (MPI_COMM_WORLD, &myrank);
int newlengthX = lengthX/total;
int remainder = lengthX%total; 
double* z0;
double* z1;
double* zleft;
double* zright;
double* tmp;
if (myrank == 0) { 
openFiles(timeInterval);
Z0 = (double*) calloc (lengthX*lengthY,sizeof(double)); 
Z1 = (double*) calloc (lengthX*lengthY,sizeof(double)); 
calculateFisrtTime(Z0,Z1,lengthX,lengthY); }
if(myrank == total-1) {newlengthX += remainder; }
z0 = (double*) calloc (newlengthX*lengthY,sizeof(double)); 
z1 = (double*) calloc (newlengthX*lengthY,sizeof(double)); 
zleft = (double*) calloc (lengthY-2,sizeof(double)); 
zright = (double*) calloc (lengthY-2,sizeof(double));
int* displsSend;
displsSend = (int *)calloc(total,sizeof(int));
int numberOfProc;
for(numberOfProc=0; numberOfProc < total; numberOfProc++)
displsSend[numberOfProc] = numberOfProc*newlengthX;
int* displsSendCount;
displsSendCount = (int *)calloc(total,sizeof(int));
for(numberOfProc=0; numberOfProc < total; numberOfProc++)
displsSendCount[numberOfProc] = newlengthX;
displsSendCount[total-1] += remainder;
int i;
for(i=0;i < lengthY; i++){
MPI_Scatterv((void *)(Z0+i*lengthX), displsSendCount, displsSend, MPI_DOUBLE,(void 
*)(z0+i*newlengthX), newlengthX, MPI_DOUBLE, 0, MPI_COMM_WORLD); 
MPI_Scatterv((void *)(Z1+i*lengthX), displsSendCount, displsSend, MPI_DOUBLE,(void 
*)(z1+i*newlengthX), newlengthX, MPI_DOUBLE, 0, MPI_COMM_WORLD);}
for(i=0;i<lengthY-2;i++){
zleft[i] = z0[newlengthX*(i+1)];
zright[i] = z0[newlengthX*(i+1)+newlengthX-1];}
if( myrank!= total-1) { 
MPI_Send((void*)zright,lengthY-2,MPI_DOUBLE,myrank+1,LEFT,MPI_COMM_WORLD);
MPI_Recv((void*)zright,lengthY2,MPI_DOUBLE,myrank+1,RIGHT,MPI_COMM_WORLD,MPI_STATUS_IGNORE);}
if( myrank!= 0){
MPI_Send((void*)zleft,lengthY-2,MPI_DOUBLE,myrank-1,RIGHT,MPI_COMM_WORLD); 
MPI_Recv((void*)zleft,lengthY-2,MPI_DOUBLE,myrank1,LEFT,MPI_COMM_WORLD,MPI_STATUS_IGNORE); }
if ( myrank == 0)time_start();bool flag = 1;
while(CurrentTime < timeInterval){
if( flag )calculate(z0,z1,newlengthX,lengthY,CurrentTime,myrank,total,zleft,zright);
12
else calculate(z1,z0,newlengthX,lengthY,CurrentTime,myrank,total,zleft,zright);
#ifdef WRITETOGNUPOT 
for(i=0;i < lengthY; i++){
if( flag )MPI_Gatherv((void *)(z1+i*newlengthX), newlengthX, MPI_DOUBLE,(void 
*)(Z1+i*lengthX),displsSendCount, displsSend, MPI_DOUBLE, 0, MPI_COMM_WORLD);
else MPI_Gatherv((void *)(z0+i*newlengthX), newlengthX, MPI_DOUBLE,(void 
*)(Z0+i*lengthX),displsSendCount, displsSend, MPI_DOUBLE, 0, MPI_COMM_WORLD); 
 } 
if( flag ){if(myrank == 0) writeIntoFile(Z1,lengthX, lengthY,CurrentTime);}
else{if(myrank == 0)writeIntoFile(Z0,lengthX, lengthY,CurrentTime); }
#endif
flag = !flag;
CurrentTime+=dt;}
if ( myrank == 0){
int ms = time_stop();
printf("Time: %d milliseconds\n", ms);}
free(z0);
free(z1);
free(zleft);
free(zright);
free(displsSend);
free(displsSendCount);
if (myrank == 0){
free(Z0);
free(Z1);
}
MPI_Finalize();
exit(0);}