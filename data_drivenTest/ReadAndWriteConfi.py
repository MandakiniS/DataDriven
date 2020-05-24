from pyjavaproperties import Properties

file_name="/Users/smandaki/PycharmProjects/DataDriven/data/config.properties"
output_Sterm=open(file_name, "a")
prop= Properties()
prop.setProperty(key='ValueOfPi', value="double,valueTesting")
prop.store(output_Sterm)
output_Sterm.close()

input_stream=open(file_name, "r")
prop1=Properties()
prop1.load(input_stream)
newval=prop.getProperty("ValueOfPi")
Str1=newval.split(',')
print(Str1[0])
print(Str1[1])
input_stream.close()

'''
file_path = "/Users/smandaki/PycharmProjects/DataDriven/data/config.properties"
output_file = open(file_path, 'a')
prop = Properties()
prop.setProperty(key="Users", value='Agent,Admin')
prop.store(output_file)
output_file.close()


input_stream = open(file_path, mode='r')
prop = Properties()
prop.load(input_stream)

bname = prop.getProperty('browser')
print("browser :", bname)
username=prop.getProperty('username')
print('username:',username)
input_stream.close()'''