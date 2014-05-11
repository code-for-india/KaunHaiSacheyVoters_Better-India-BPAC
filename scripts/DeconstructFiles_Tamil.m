path = 'C:\Users\ravindhrans\Desktop\AkshayaPatra\CodeForIndia\'
file = 'Tamil2.txt';
txtfile = [path file];
txtfileWrite = 'C:\Users\ravindhrans\Desktop\AkshayaPatra\CodeForIndia\TamilCleaned2.txt';
text = fileread(txtfile);

% Fix Google transliteration error for Marathi
text = strrep(text, 'Papayara', 'Name');
text = strrep(text, 'Tanacata', 'Father');
text = strrep(text, 'Vayata:', 'Age:');
text = strrep(text, 'Inama: ana','Gender: Male');
text = strrep(text, 'Inama: papana','Gender: Female');
text = strrep(text, 'Vatata Count:', 'House Number:');

StartingCodes = {'DGL0','PY/01','XDQ0','LXL0'};
index1 = strfind(text,StartingCodes{1});
index2 = strfind(text,StartingCodes{2});
index3 = strfind(text,StartingCodes{3});
index4 = strfind(text,StartingCodes{4});
StartingIndices = sort([index1 index2 index3 index4]);

% Find page3 start
PageStart = strfind(upper(text),upper('Page 4'));
PageStart = PageStart(1);
SrNumber = 1;
person(SrNumber).uniqueID = [];
person(SrNumber).NameofFather = [];
person(SrNumber).FullName = [];
person(SrNumber).SpouseName = [];
person(SrNumber).HouseNo = [];
person(SrNumber).Age = [];
person(SrNumber).Sex = [];
person(SrNumber).PhotoAvailable = [];

PersonIndex = StartingIndices;
EndofDoc = 0;

while(SrNumber<length(PersonIndex))
    
    Persontext = text(PersonIndex(SrNumber):PersonIndex(SrNumber+1));
    spc = strfind(Persontext,'Name'); spc = spc(1); 
    spc1 = strfind(Persontext,'Husband');
    spc2 = strfind(Persontext,'Father');
    spc3 = strfind(Persontext,'Age'); spc3 = spc3(1);
    spc4 = strfind(Persontext,'Gender');
    spc5 = strfind(Persontext,'House Number');
    
    person(SrNumber).uniqueID = strtrim(Persontext(1:spc-1));
    if (spc2 > 0)
        person(SrNumber).NameofFather = strtrim(Persontext(spc2+12:spc3-8));
        person(SrNumber).SpouseName = [];
        spc6 = spc2;
    else
        person(SrNumber).NameofFather = [];
        person(SrNumber).SpouseName = strtrim(Persontext(spc1+13:spc3-8));
        spc6 = spc1;
    end
    person(SrNumber).HouseNo = strtrim(Persontext(spc5+14:end-4));
    if length(person(SrNumber).HouseNo) > 2
        person(SrNumber).HouseNo = person(SrNumber).HouseNo(1:2);
    end
    person(SrNumber).Age = str2num(strtrim(Persontext(spc3+4:spc4-1)));
    person(SrNumber).Sex = strtrim(Persontext(spc4+7:spc5-2));
    person(SrNumber).PhotoAvailable = 0;
    person(SrNumber).FullName = strtrim(Persontext(spc+4:spc6-3)); 
    if (length(person(SrNumber).FullName)==0)
        person(SrNumber).Valid = 0;
    else
        person(SrNumber).Valid = 1;
    end 
    SrNumber = SrNumber + 1;
end


fileID = fopen(txtfileWrite,'w');
numpeople = size(person,2)
for n = 1:numpeople
    if (length(person(n).NameofFather)>0)
        fprintf(fileID,'father_name:');
        fprintf(fileID,'%s',person(n).NameofFather);
    else
        fprintf(fileID,'spouse_name:');
        fprintf(fileID,'%s',person(n).SpouseName);
    end
    fprintf(fileID,'|||house_number:');
    fprintf(fileID,'%s',person(n).HouseNo);
    fprintf(fileID,'|||voter_id:');
    fprintf(fileID,'%s',person(n).uniqueID);
    fprintf(fileID,'|||Gender:');
    fprintf(fileID,'%s',person(n).Sex);
    fprintf(fileID,'|||Age:');
    fprintf(fileID,'%d',person(n).Age);
    fprintf(fileID,'|||full_name:');
    fprintf(fileID,'%s',person(n).FullName);
    fprintf(fileID,'|||photo:');
    fprintf(fileID,'%d***',person(n).PhotoAvailable);
end
