# mujoco-xml-generator

## For developers

### Git prefix

| Prefix | Definition                                                  |
|--------|-------------------------------------------------------------|
| add    | Indicates addition of new files or directories.             |
| docs   | Indicates modifications made to documents or similar items. |
| fix    | Indicates bug fixes.                                        |
| impl   | Indicates implementation of new functions.                  |
| remove | Indicates removal of files or directories.                  |

If you want to commit changes while editing, please use the "-ing" suffix. For example, "impl-ing".

### How to treat the dependencies

To record the dependencies

```commandline
pip freeze > requirements.txt
```

To install the dependencies

```commandline
pip install -r requirements.txt
```