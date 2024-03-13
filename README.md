# mujoco-xml-generator

## For developers

### Git prefix

| Prefix | Definition                                                  |
|--------|-------------------------------------------------------------|
| add    | Indicates addition of new files or directories.             |
| docs   | Indicates modifications made to documents or similar items. |
| fix    | Indicates bug fixes.                                        |
| impl   | Indicates implementation of new functions.                  |
| mv     | Indicates movement or rename of files.                      |
| remove | Indicates removal of files or directories.                  |
| test   | Indicates something about tests.                            |

We define suffixes for above prefixes. For example, "impl-ing".

| Suffix | Definition                                     |
|--------|------------------------------------------------|
| -ing   | Indicates that something has not finished yet. |
| -suc   | Indicates that something has succeed.          |
| -fail  | Indicates that something has failed.           |

### How to treat the dependencies

To record the dependencies

```commandline
pip freeze > requirements.txt
```

To install the dependencies

```commandline
pip install -r requirements.txt
```