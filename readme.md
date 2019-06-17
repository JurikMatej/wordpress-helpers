# Wordpress Pull Script

## About
* Can pull specified wordpress theme's files from your web to your working directory

## Usage
```bash
python pull.py --host=ftp_host --user=ftp_user --passwd=ftp_passwd --theme=theme_name --dir=save_directory
```

* Flags which's names do not match those specified above will be ignored
* If any of the arguments above are not specified, script refers to default values 
  defined in defaults.json (Create one as a copy of 'defaults-example.json' if it already doesn't exist)
* Save directory defaults to the current working directory