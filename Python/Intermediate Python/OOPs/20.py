# what is a context manager?
# A context manager helps you manage resources, such as files, automatically.
# You have already learned file handling, so this will build on your existing knowledge.

# with method is commonly used with a context manager.

# Let's a build a file logger.


class FileLogger:
    def __init__(self, filename):
        self.filename=filename

    def __enter__(self):
        self.file = open("filename","a") 
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with FileLogger("app.log") as log:
    log.write("User logged in\n")

print("Logging completed!")