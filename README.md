Convenient small scripts to be used on the clusters.

It works as follow:

1\ This folder is cloned to $HOME directories of each cluster.

2\ This folder can be changed on every cluster:
		 before change: pull 
		 after change: immediate add, commit and push

3\ Easier editting might be:
		on my local computer, pull, edit, add, commit, push
		then pull from the cluster

4\ Many of the scripts here needs to be in the working directory, but instead of copy, do "ln -s the_actual_file soft_link", in this way, we just have one copy of each file on each cluster. And every time we need to improve the script, we keep track of it.

5\ "Ready" folders are these end with \_script, and can be safely linked to. The path will not be changed.

6\ Folders that need to be cleaned are these end with \_tmp, and shouldn't be linked to, because they will be changed and moved to "ready" folders for use.



