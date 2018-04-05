%after md run, some atoms may exchange position;

%this code is to average the greatly distorted structures and non-distorted
%structures to make it less distorted.

%open the relaxed .vasp file (not so distorted)
filenameA='/Users/yao/Desktop/data/SNO/mdrun/SNO-5-relaxed.POSCAR.vasp';
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

for i=1:29
    filenameB=strcat('/Users/yao/Desktop/data/SNO/mdrun/',int2str(i),'.vasp');
    fileIdB=fopen(filenameB);
    %scan the header of B file into strB and postion info into positionB.
    formatSpec='%s';
    strB=textscan(fileIdB,formatSpec,n1,'Delimiter','\n');
    formatSpec='%f %f %f';
    positionB=textscan(fileIdB,formatSpec,n2,'Delimiter','\n');
    %create a new position cell to store the info for average position.
 
    %average the atom positions of the distorted structure and
    %non-distorted structure.
        
    for j=1:54
        for k=1:3
            positionNew{1,k}(j)=(positionA{1,k}(j)+positionB{1,k}(j))/2;
            if abs(positionNew{1,k}(j)-positionA{1,k}(j))>0.4
                positionNew{1,k}(j)=positionNew{1,k}(j)+0.5;
            end
        end
    end
                
        
        
    
    %create new .vasp files to average the distorted structure to make it
    %less distorted.
    filename=strcat('/Users/yao/Desktop/data/SNO/mdrun/less_distorted_',int2str(i),'.vasp');
    fid=fopen(filename,'w');
    for j=1:8
        formatSpec='%s';
        fprintf(fid,formatSpec,strA{1,1}{j,1});
        fprintf(fid,'\n');
    end
    for j=1:54
        formatSpec='%f %f %f';
        fprintf(fid,formatSpec,positionNew{1,1}(j),positionNew{1,2}(j),positionNew{1,3}(j));
        fprintf(fid,'\n');
    end
    fclose(fid);
end
    
    