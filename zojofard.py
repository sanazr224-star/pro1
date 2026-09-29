def main():
    x= int(input('x= '))
    if even(x):
       print('even')
    else :
       print('odd')
def even(n):
    return n%2==0
main()