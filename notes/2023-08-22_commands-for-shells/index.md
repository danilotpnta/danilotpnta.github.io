---
title: "Commands Shells"
description: "A useful list of Shell commands"
date: "2023-08-22"
date-format: long
year: "2023"
categories: [All, Shells, Scripting, TAGS, Bash, Zsh]
number-sections: false
---

# Bash

```bash
# Creates an alias function that can be called from terminal
function(){
    
    # $1 first argument passed from terminal
    FOLDER=$(python create_dir.py $1 $2) 

    # To print a variable
    echo $FOLDER

    # Use var inside another var uses ${}
    BACKUPDIR=$(ls -td ${FOLDER}/*/ | head -1)

}
```


# Zsh
```bash

# Eliminate the last line of history
cd
code .zsh_history
reload_shell

# Makes reload the page
reload_shell(){
  cd 
  source .zshrc   
}

# Folder for plugin's
open ~/.oh-my-zsh/plugins

# Show all including empty files
ls -a            
```

# Syntax

```bash
# Valid naming
_ALI
TOKEN_A

# Invalid naming
2_VAR
-VARIABLE
VAR1-VAR2
```





