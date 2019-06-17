# Wordpress Pull Script

## About
* Can pull specified wordpress theme's files from your web to your working directory

## Usage
```bash
python pull.py --host=ftp_host --user=ftp_user --passwd=ftp_passwd --theme=path_to_theme --dir=save_directory
```

* Flags with names that __do not match__ those specified above will be __ignored__
* If any of the __arguments__ above are __not specified__, script refers to default values 
  defined __in defaults.json__ (_Create one as a copy of 'defaults-example.json' if it already doesn't exist_)
* Save directory (_destination_) defaults to the _current working directory_
* If your __save directory has a whitespace__ char in it, replace it with **```_S_```**