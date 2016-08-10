class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
        #print("The self is: %r" % self)

thing = MyStuff()  # instantiation
thing.apple()      # call method
print(thing.tangerine)
