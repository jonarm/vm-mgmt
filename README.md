vm-mgmt
=======

vm-mgmt connects to a vCenter/ESX Server to execute tasks and generate reports

## Requirements ##
* Pysphere

## Usage ##
```
./vm-mgmt.py
```

## Example ##
1. Run the script
  ```
  ./vm-mgmt.py
  ```

2. Enter the necessary details
  ```
  Enter username: uname
  Password: pass
  Enter vCenter/ESX Server: vcenter.example.com
  Enter the serverlist file: vmlist.txt
  Enter target ESX Host: esx-svr01
  ```

  >Todo: include other functions like List VMs in an ESX Host from vcenter, Create multiple VMs based on a list, etc
