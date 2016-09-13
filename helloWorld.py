import os
#required module for file-processing operations such as renaming or deleting files, directory related operations
import shutil

import os.path

def main():
        print ("Hello World")
        a = """two
three"""
        print a
        list=['abc',123,"ghi",46.0,34+5j]
        print(list[0]);
        print(list[0:2]);
        print(list[1:]);
        print(list * 2);
        tinylist=["newlist"]
        print(list + tinylist)
       # input("Press any key to terminate the application")

        # Standard input
        #str = raw_input("Enter your raw input")
        #print "Received input is:", str
        #str = input("Enter your input")
        #print "Your evaluated input:", str

        #file IO
        fo = open("simpleinput.txt", "r");
        print fo.closed
        print fo.mode
        print fo.name
        print fo.softspace
        fo.close()
        print fo.closed

        #file read
        fo = open("largeFile.txt","r");
        #str = fo.read();
        #print str;

        fo = open("simpleinput.txt", "r");
        str = fo.read(10);
        print "First 10 characters in file:", str;
        print fo.tell();
        print fo.read(5);
        fo.seek(9, 1);
        print fo.read();
        fo.close();
        
        #file write
        fo = open("simplefile.txt", "wb");
        fo.write("\nThis line wrote.\n");
        fo.close();

        #file append
        fo = open("simplefile.txt", "a+");
        fo.write("This is appended line\n");
        fo.close();

        #rename file
        os.rename("simplefile.txt", "newsimplefile.txt");

        #delete a file
        os.remove("newsimplefile.txt");

        #check if a file exists and delete it
        open("simplefile.txt", "w+")
        if os.path.exists("simplefile.txt"):
                print "File exists. Removing it"
                os.remove("simplefile.txt")
        
        #create directory
        os.mkdir("newDir");
        os.chdir("./newDir");
        print os.getcwd();
        os.chdir("../");
        print os.getcwd();
        os.chmod("./newDir", 0777);
      #  os.remove("newDir");
        shutil.rmtree("newDir");
if __name__ == "__main__":
        main()
