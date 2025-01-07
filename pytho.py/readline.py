def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('student.csv',3)
f.write("Python Exercises\n")
f.write("Java Exercises")
file_read_from_head('student.csv')
   

