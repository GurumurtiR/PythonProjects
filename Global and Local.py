# Global and Local varible example

age = 23 # global variable
name = 'somesh' # name global variable
places = ['nagpur', 'mumbai', 'bangalure'] # global variable
def local():
    age = 20 # local
    name = 'ayush' # local
    print("%s is %i years old and lives in %s" %(name, age ,places[0]))
    return
local()
print('#############################################')
print("%s is %i years old and lives in %s" %(name, age, places[2]))