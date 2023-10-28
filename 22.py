class Validator:
    def getCorr(self, str):
        if (len(str) > 0):
            print("Correect")
        else:
            raise Exception('name is incorrect')

    def isEmail(self, str):
        if str.startswith('@mail.com'):
            print("Correect")
        else:
            raise Exception('name is incorrect')

    def isDomen(self, str):
        if str.startswith('www.'):
            print("Correect")
        else:
            raise Exception('name is incorrect')

    def isNumber(self, str):
        if str.isnumeric():
            print("Correect")
        else:
            raise Exception('name is incorrect')


arrHelper = Validator()

sss = arrHelper.isEmail("@mail.com")
print(sss)

sssq = arrHelper.isNumber("21")
print(sssq)

str1 = arrHelper.getCorr("fsa")
print(str1)

str2 = arrHelper.getCorr("sas@mail.com")
print(str2)