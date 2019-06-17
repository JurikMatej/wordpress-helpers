# Wordpress Helpers

## About
* Set of scripts that help with administrating your wordpress projects (for devs)
* Utilities:
  * Pull themes
  * Push Modified theme files (NYI)
  * More hopefully comming soon..

## Usage
### Pull themes
  ```bash
  python pull.py --host=ftp_host --user=ftp_user --passwd=ftp_passwd --theme=path_to_theme --dir=save_directory
  ```

  * __Flags__ with names that __do not match__ those specified above will be __ignored__
  * If any of the __arguments__ above are __not specified__, script refers to default values 
    defined __in defaults.json__ (_Create one as a copy of 'defaults-example.json' if it already doesn't exist_)
  * Save directory (_destination_) defaults to the _current working directory_
  * If your __save directory has a whitespace__ char in it, replace it with **```_S_```**

### Push modified theme files
  * __Not yet implemented__