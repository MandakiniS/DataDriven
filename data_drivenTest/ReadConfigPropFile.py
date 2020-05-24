from pyjavaproperties import Properties
file_path = "/Users/smandaki/PycharmProjects/DataDriven/data/config.properties"
input_stream = open(file_path, mode='r')
prop = Properties()
prop.load(input_stream)
bName = prop.getProperty("browser")
UserName = prop.getProperty("username")

print(bName)
print(UserName)
input_stream.close()