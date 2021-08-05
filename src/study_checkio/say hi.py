'''
https://py.checkio.org/mission/say-history/

In this mission you should write a function that introduce a person with a given parameters in attributes.

Input: Two arguments. String and positive integer.

Output: String.
'''
def say_hi(name,age):
    str = "Hi. My name is %s and I'm %d years old"%(name,age)
    return str
def main():
    say_hi("alex",21)
if __name__=="__main__":
    main()