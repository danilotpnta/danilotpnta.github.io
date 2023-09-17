---
title: "Command Environments"
description: "A useful list of conda commands"
date: "2023-08-22"
categories: [All, Environments, TAGS, Conda]
number-sections: false
---



# Environments

```bash
conda deactivate                  # to desactivate an environment
conda activate <progLab>          # to activate base environment
conda list                        # to see all packages in env
conda env list                    # to see all env
conda create -n <web> python=3.7  # install an environment
conda create -n <example_env>     # to create an env
conda env remove -n <ENV_NAME>    # remove env
conda create --name new_env --clone old_env    # Change name. Clone the old environment to a new environment with the name we want
conda remove --name old_env --all              # Delete the old environment
```

To make sure that the `progLab` environment is activated every time (auto) that we start a terminal, we can run the following command (replace `bash` with `zsh` if needed):

the following command (replace `bash` with `zsh` if needed):

```bash
echo 'conda activate progLab' >> ~/.zshrc
```

## Conda

> A conda environment is **a directory that contains a specific collection of conda packages that you have installed**. For example, you may have one environment with NumPy 1.7 and its dependencies, and another environment with NumPy 1.6 for legacy testing.

## Anaconda

> It gives you all the standard packages used in scientific computing in a convenient package without having to worry about installing them all individually with their dependencies.

## In short Conda + Anaconda

Conda is a package manager. It **helps you take care of your different packages by handling installing, updating and removing them**. Anaconda contains all of the most common packages (tools) a data scientist needs and can be considered the hardware store of data science tools.

```bash
conda install anaconda
```

# How to create an environment

------

Create your new environment, here called “mypython3” but you can call it what you wish:

```bash
conda create -n <mypython3> python=3
```

To activate the environment:

```bash
source activate mypython3
```

To get all the goodies (e.g. [Jupyter Notebook](https://jupyter.org/), [NumPy](http://docs.scipy.org/doc/numpy/reference/index.html), [matplotlib](http://matplotlib.org/contents.html)) you can install [Anaconda](https://www.anaconda.com/products/individual), which will auto-magically use Python 3.

```bash
conda install anaconda
```

and then our additional install, [netcdf4-python](http://unidata.github.io/netcdf4-python/)

```bash
conda install netcdf4
```

Now you have set-up your Python 3 environment. To start it in a new terminal

```bash
source activate mypython3
```

When you are using that environment your prompt will change and will include (mypython3). To return to using your “base” environment you can de-activate the conda environment with:

```bash
source deactivate
```
## How to erase an environment

```bash
conda remove --name ml1labs --all
```

## echo $PATH

------

**$PATH** (or the search path) is the list of directories that will be searched for anything that you type on the command line

We use sometimes **ls** or **pwd** or **echo** this is because there is a **$PATH** where this was. This list of pre-designated directories is stored in a special variable called “PATH”

This is a colon-delimited list of all the directories the command line looks in by default for programs on the particular computer. 

**Example**

```bash
$ (progLab) datoapanta@Danilos-MacBook-Pro ~ % echo $PATH
```

/Users/datoapanta/opt/anaconda3/envs/progLab/bin:/Users/datoapanta/opt/anaconda3/condabin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin:/usr/local/share/dotnet:~/.dotnet/tools:/Library/Frameworks/Mono.framework/Versions/Current/Commands:/Users/datoapanta/.local/bin:/Users/datoapanta/.local/bin 

```bash
echo $PATH | tr ":" "\n"
```

/Users/datoapanta/opt/anaconda3/envs/progLab/bin
/Users/datoapanta/opt/anaconda3/condabin
/usr/local/bin
/usr/bin
/bin
/usr/sbin
/sbin
/Library/TeX/texbin
/usr/local/share/dotnet
~/.dotnet/tools
/Library/Frameworks/Mono.framework/Versions/Current/Commands
/Users/datoapanta/.local/bin
/Users/datoapanta/.local/bin

> We can now more clearly see this is a list of directories. All of these places, stored in the variable called **“PATH”**, are searched whenever we are typing a command in the terminal window.
> 
>  If the command we are trying to use is present in any of the directories listed in our PATH, we don’t need to point at its specific location in full (its path, lowercase) when we are trying to use it – which is of course nice for things we use often.


