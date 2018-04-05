%open the relaxed .vasp file (not so distorted)
filenameA='/Users/yao/Desktop/exp_1998_U7_relaxed.vasp';
fileIdA=fopen(filenameA);
n=62;
n1=8; %the first seven lines contain crystal parameters and etc.
n2=54; %the 9~62 lines contain 54 atom positions.
%scan the header of A file into strA and postion info into positionA.
formatSpec='%s';
strA=textscan(fileIdA,formatSpec,n1,'Delimiter','\n');
formatSpec='%f %f %f';
positionA=textscan(fileIdA,formatSpec,n2,'Delimiter','\n');

%% 
octahedra = zeros(10,18);
%% 
for i=11:20
    for j=21:54
        
        
    
