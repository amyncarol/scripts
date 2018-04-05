%split xdatcar into separate .vasp files (structure files)
fileID = fopen('/Users/yao/Desktop/data/SNO/mdrun/XDATCAR');
formatSpec='%s';
n1=7; %the first seven lines contain crystal parameters and etc.
n2=55; %the 8~62 lines contain "direct" label and 54 atom positions.
%scan the first seven lines into str1.
str1=textscan(fileID,formatSpec,n1,'Delimiter','\n');
%scan the atom postions into separate files using a loop.
while ~feof(fileID)
for i=1:100 
    %scan the atom postion lines into str2.
    str2=textscan(fileID,formatSpec,n2,'Delimiter','\n');
    %create a new cell to store the info for the new .vasp files.
    str{1,1}{62,1}=[];
    for j=1:7
        str{1,1}{j,1}=str1{1,1}{j,1};
    end
    for j=1:55
        str{1,1}{7+j,1}=str2{1,1}{j,1};
    end
    %create new .vasp files.
    filename=strcat('/Users/yao/Desktop/data/SNO/mdrun/',int2str(i),'.vasp');
    fid=fopen(filename,'w');
    %print str cell to the .vasp files.
    for j=1:62
        fprintf(fid,formatSpec,str{1,1}{j,1});
        fprintf(fid,'\n');
    end
    fclose(fid);
end
end
fclose(fileID);