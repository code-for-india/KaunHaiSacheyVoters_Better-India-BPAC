txtfile = 'C:\Users\ravindhrans\Desktop\AkshayaPatra\CodeForIndia\English.txt';
text = fileread(txtfile);

% Fix Google transliteration error for Marathi
strrep(text, 'Professionally', 'Kambhari');

% Find page3 start
PageStart = strfind(upper(text),upper('Number of parts'));
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

EndofEachPerson = strfind(text,'Available');
EndofEachPerson = EndofEachPerson(find(EndofEachPerson > PageStart));
PersonIndex = [PageStart EndofEachPerson];
EndofDoc = 0;

while(SrNumber<length(PersonIndex))
    
    Persontext = text(PersonIndex(SrNumber):PersonIndex(SrNumber+1));
    spc = strfind(Persontext,'Name of');
    person(SrNumber).uniqueID = strtrim(Persontext(spc-12:spc-1));
    spc2 = strfind(Persontext,'House number');
    spc3 = strfind(Persontext,'Age');
    spc4 = strfind(Persontext,'Gender');
    spc5 = strfind(Persontext,'Photo');
    if strcmp(strtrim(Persontext(spc+7:spc+13)),'Father')
        person(SrNumber).NameofFather = strtrim(Persontext(spc+14:spc2-1));
        person(SrNumber).SpouseName = [];
    else
        person(SrNumber).NameofFather = [];
        person(SrNumber).SpouseName = strtrim(Persontext(spc+14:spc2-1));
    end
    person(SrNumber).HouseNo = str2num(strtrim(Persontext(spc2+12:spc3-1)));
    person(SrNumber).Age = str2num(strtrim(Persontext(spc3+4:spc4-1)));
    person(SrNumber).Sex = strtrim(Persontext(spc4+7:spc4+12));
    subtext = Persontext(spc4:spc5);
    indx = strfind(subtext,':');
    indx = indx([1 2]);
    if ~strcmp(upper(person(SrNumber).Sex),'MALE')
        person(SrNumber).Sex = 'Female';
        person(SrNumber).FullName = strtrim((subtext(indx(1)+9:indx(2)-1)));
    else
        NameWithoutCleaning = subtext(indx(1)+1:indx(2)-1);
        person(SrNumber).FullName = strtrim(subtext(indx(1)+6:indx(2)-1));
    end
    if strfind(Persontext(spc5+7),'A')
        person(SrNumber).PhotoAvailable = 1;
    else
        person(SrNumber).PhotoAvailable = 0;
    end
   
    if (length(person(SrNumber).FullName)==0)
        person(SrNumber).Valid = 0;
    end 
    SrNumber = SrNumber + 1;
end

