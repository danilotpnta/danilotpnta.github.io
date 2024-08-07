---
title: "Commands Terminal"
description: "Description of this Note"
date: "2023-09-03"
date-format: long
year: "2023"
categories: [All, TAGS]
number-sections: true
toc: false
---

## Terminal

```
cd -    # one folder back
cd ..   # one up
cd ../  # two up
cd      # home directory 
cd /    # root directory
pwd         # print working directory
open <PATH>
open .     # open current folder you're in
touch <file.txt> # to create a file
```

## Git Hub

```
git clone <HTTPS>    # copy repo from the HTTPS of the GitHub repository 
git status                      # to check whether the tree line has been updated
git add .                       # add all new folders and files to git repo
git add <name>       # add specific folder for the git repo
                                         # this is only to tell git taht there has been changes, we still need to commit
git commit -m "<message>"   # this save the files to git repo
git commit -m "<message>" -m "<message for the description box>"   # this save the files to git repo
```

So the way it works

1. You change the code
2. You need to save to the git file --> git add .
3. You need to commit --> git commit - m "message"
4. You push it to the repo --> git push main 

### Working with branches

> https://youtu.be/QV0kVNvkMxc

### Key Generation

```
ssh-keygen -t rsa -b 4096 -C "danilotpnta@gmail.com"   # to generate a key SSH
ls | grep git-key   # to check the keys available
                    # key.pub pub stands for public 
cat <example_key.pub>                     # to print the key
```

### Generating a new SSH key

```
ssh-keygen -t ed25519 -C "danilotpnta@gmail.com" 
```

### Adding your SSH key to the ssh-agent

```
eval "$(ssh-agent -s)"
open ~/.ssh/config
vim ~/.ssh/config
ssh-add ~/.ssh/id_ed25519   # to add the key with name "id_ed25519"
cat ~/.ssh/id_ed25519.pub   # to print the key that we created 
```

## Vim

```
:wq     # to write/save and quit
ESC     # to scape from __INSERT__
```

### Prompt Message

he Bash command prompt looks like this by default:

```
[USERNAME]@[HOSTNAME]:[PATH][SYMBOL]
```

- `[USERNAME]` is the username of the currently operating user. normally this is your user, but when you run `sudo su` or similar commands, you get a "root shell", that means the user is "root".
- `[HOSTNAME]` is your hostname. It's the name of your computer. You had to enter that during the system installation.
- `[PATH]` is your current working directory, the directory you're currently operating on. When you open a new terminal, the default directory is your current user's home directory. A synonym for `/home/YOURUSERNAME` is `~`.
- `[SYMBOL]` is usually either `$` if you're operating as any normal user, or `#` if you're operating as "root" user.

So your Bash prompt looks like this:

```
ganesh@ganesh:~$
```

That means you're logged in as user `ganesh` on a computer called `ganesh` as well, currently operating in your own home directory (`~`). Of course you're not "root", therefore the `$`.
