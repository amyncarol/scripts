%read in splitted DOS
dos = dlmread(['/Users/yao/Desktop/data/SNO/SNO_orth/break_sym/U0/U6_NUPDOWN4/rawDOS/DOS5']);
for i = 6:8
    dos2 = dlmread(['/Users/yao/Desktop/data/SNO/SNO_orth/break_sym/U0/NUPDOWN4/rawDOS/DOS',int2str(i)]);
    dos(:,2:19)=dos(:,2:19)+dos2(:,2:19);
end

dos(:,20)=0;
for i=3:2:19
    dos(:,20)=dos(:,20)+dos(:,i);    
end

figure(8);
hold on;
plot(dos(:,1),dos(:,20),'k');













