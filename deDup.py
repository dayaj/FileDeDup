import os
import shutil
import md5

os.chdir("deDupingInputFiles");
print os.getcwd();

fo = open("txt1.txt", "w");
fo.write("abc");
fo.close();
shutil.copyfile("txt1.txt", "txt2.txt");

fo1 = open("txt1.txt", "r");
fo2 = open("txt2.txt", "r");

if(fo1.read() == fo2.read()):
    print "Contents match"
else:
    print "Contents mismatch"
    
m2 = md5.new();
m2.update("abc");
m3 = md5.new();
m3.update("abc");
print m2.hexdigest();
print m3.hexdigest();


#m = md5.new("txt1.txt");
m = md5.new(fo1.read());
print m.hexdigest();
#m1 = md5.new("txt2.txt");
m1 = md5.new(fo2.read());
print m1.hexdigest();

if m.hexdigest() == m1.hexdigest():
    print "md5 Match";
else:
    print "md5 Mismatch";

fo1 = open("cropped.ppm", "r");
fo2 = open("cropped.ppm", "r");
m1 = md5.new(fo1.read());
m2 = md5.new(fo2.read());
if m1.hexdigest() == m2.hexdigest():
    print "Images match"
else:
    print "Images mismatch"
    

