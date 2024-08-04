
def greet(fx):
  def mfx():
        print("good morning")
        fx()
        print("thankyou for using our website")
        return mfx()
@greet
def op():
    print("hello world")
op()





