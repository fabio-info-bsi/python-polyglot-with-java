import sys
import time
import java

if __name__ == "__main__":
    start = time.time()
    try:
        print(sys.version)
        Application = java.type("demo.Application")
        app = Application()
        print(app.findById(1))
        print(app.findByUcodeBatch(""))

    except Exception as e:
        print("General Error: {}".format(e))

    end = time.time()
    print(end - start)
