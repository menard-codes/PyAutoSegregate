# PyAutoSegregate
PyAutoSegregate is a simple Python Program that cleans up your messy files. It basically sorts out (or segregate) files based on their file extension and group them together to separate folders to make your files organized.

You may already be familiar with having messy files, most of which you probably aren't even using anymore some of those files which are rotting on that files storage taking a chunk in your disk.

And it's so sick and boring to copy, move, paste, and create folders here and there, and categorizing files after files, after files.

And besides, it eats up A LOT OF TIME and some energy just to do that.

Wonder if we can just automate it and skip the boring task, wouldn't that be so helpful?

Well, Python is there to do that pesky task for us.

Let me introduce you my simple program I call "PyAutoSegregate", your files clerk ready to clean up your folders in just a click of a button.

This is a simple program I wrote using Python inspired by my laziness to manually organize my files, especially my Downloads folder which always end up having lots and lots of different files in it. And since making that program, I no longer have that messy files, thanks to this program.

PyAutoSegregate only has three files in it, all working to instruct Python what to do.

The first one is the App.py module which is just basically the GUI part of the program, and it uses the built in tkinter module.

The real action happens in the second file, the AutoSegregate Module which contains a class in it and several methods.

The AutoSegregateFiles class inside this module is basically what the App.py module uses as its engine to execute the task of organizing the files inside the directory the user entered to the entry field.

The AutoSegregateFiles class then uses its segregate method to take the directory passed onto it, create the folders it need to organize the file like the Documents and Videos folder, scans all the files inside the directory it got, look through its extensions, categorize the files based on their extensions, and move it to the folder that matches its category.

And it categorizes the files based on the "categories.json" file which is the third file in the project folder.

The categories.json file contains different File Categories and the Specific Extensions that fall under these categories.

This is also the File you will modify if you want to Add another category and file extensions for the program to recoganize.

Note that the program uses the File Categories passed on to this .json file to NAME the Folders it will create to the directory, and use the extensions array corresponding to the specific category to match a file if it belongs to that category. And this  is the basis of the AutoSegragateFiles class to segregate every files it scans.

So that's basically all about this software.

Be sure to watch the video for the Guide on how to use it in YouTube and support me by Subscribing to the channel.
https://youtu.be/XH4cnJ4_o9U

See it on Medium.com:
https://medium.com/@menardmaranan19/automate-cleaning-your-files-with-pyautosegregate-fe491fdb7a65
