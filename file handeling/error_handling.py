#error vs exceptions
# compile time, run time

try:
    with open('name.txt','r') as f:
        print(f.read())
        print(10/10)
        x=int("1")
        a=[1,2,3,4]
        print(a[1])
        x=10
except ZeroDivisionError:
    print("error:Zero by division is not possible")
except FileNotFoundError:
    print("file not found")
except ValueError:
    print("invalid value")
except IndexError:
    print("invalid index")
except Exception as e:
    print("some errror occured",e)
else:
    print("code executed successfully")
finally:
    print("eta print hobei")
    
def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("only .txt file arw allowed")
    print("valid file")
check_file('name.txt')
