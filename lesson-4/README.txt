USE THE BAT FILES TO RUN THE FILE OR CMD FOR SOME REASON FILE READING DOESN'T WORK OTHERWISE :)

-----------------------------------------------------------------------------------------------

This is gonna explain the process behind the whole json file reading thing i've used to safe and 
read quiz answers

I've opted to use json just as good practice, this is because eval() can be very dangerous to use 
in certain circumstances. Whilst this may not be one of those circumstances I find it a lot cleaner 
in terms of the actual code and in most cases allows for sharing between different languages (json is used across a lot of different systems).

However, you may notice im actually saving to a .txt. This is because I need to save multiple 
dictionaries, which json does not support. Writing this I realise I could have just used pickling 
but I've already implemented the json process so hey ho.

The code "[json.loads(line) for line in f]" creates a list of dictionaries where each dictionary is 
a new line in the file. "json.loads()" loads json from a string, allowing me to iterate through each 
line in the file as text and load to a python object through the json module.

Whilst in a perfect world I could've then just written each dictionary to a newline in the txt file using f.write(), python likes to 
be awkward and using single quotes in dictionaries whilst json only supports the use of double quotes. Therefore, I need to use
"json.dumps()" to dump the python dict to a string of a json object with double quotes, which I can then use 'f.write(f"{dict}\n")'
to write it to the file, using "\n" to ensure each dict is on a new line.

Hope this explains the kinda odd way I've implemented saving and reading in activity 3