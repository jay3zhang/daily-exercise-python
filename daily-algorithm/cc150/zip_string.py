# coding=utf-8

def zip_string(self, iniString):
        zipstr = ''
        same = 1
        for i in range(0,len(iniString)-1):
            # 对于每个字符，判断它和下一个字符是否相等
            # 相等same+1，不相等same重置为1
            if iniString[i]==iniString[i+1]:
                same +=1
            else:
                zipstr = zipstr+iniString[i]+str(same)
                same = 1 
        
        zipstr = zipstr+iniString[i]+str(same)

        if len(zipstr)>len(iniString):
            return iniString
        else:
            return zipstr
        
test = zip_string('welcometonowcoderrrrr')
print(test)