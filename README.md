# process-watcher
Watch Linux processes and notify when they complete. Should also work with MacOS*.

Only needs the */proc* pseudo-filesystem to check and gather information about processes. Does not need to create/own the process, if you want a daemon manager, see the *Alternatives* section below.

Currently written for **Python3**, but shouldn't be difficult to make python2 compatible.

\**If you run process-watcher on MacOS and it works, let me know so I can update the documentation.* 

**Supported notification methods:**

* Console (STDOUT)
* Email
* Desktop Notification

**Example output message**

## Installation

use `pip` or `pip3` (current only support python3) install it
```
[sudo] pip3 install proc_watcher
``` 
after install successful
> Collecting proc_watcher
    Downloading proc_watcher-0.1.1-py3-none-any.whl
  Collecting notify2 (from proc_watcher)
    Using cached notify2-0.3.1-py2.py3-none-any.whl
  Installing collected packages: notify2, proc-watcher
  Successfully installed notify2-0.3.1 proc-watcher-0.1.1

you can run the command like this

```
# proc_watcher


usage: proc_watcher [-h] [-i SECONDS] [-p PID [PID ...]] [-c COMMAND_PATTERN]
                    [-crx COMMAND_REGEX] [-w] [-d | -q] [--log] [--notify]
                    [--email EMAIL_ADDRESS [EMAIL_ADDRESS ...]]

Watch a process and notify when it completes via various     communication protocols.
    (See README.md for help installing dependencies)
    
    [+] indicates the argument may be specified multiple times, for example:
     proc_watcher -p 1234 4258 -c myapp* -crx "exec\d+" --to person1@domain.com person2@someplace.com
    

optional arguments:
  -h, --help            show this help message and exit
  -i SECONDS, --interval SECONDS
                        how often to check on processes. (default: 1.0 seconds)
  -d, --daemon          watch processes in daemon mode
  -q, --quiet           don't print anything to stdout except warnings and errors

which process can be watched:
  -p PID [PID ...], --pid PID [PID ...]
                        process ID(s) to watch [+]
  -c COMMAND_PATTERN, --command COMMAND_PATTERN
                        watch all processes matching the command name pattern. (shell-style wildcards) [+]
  -crx COMMAND_REGEX, --command-regex COMMAND_REGEX
                        watch all processes matching the command name regular expression. [+]
  -w, --watch-new       watch for new processes that match --command. (run forever)

Notify:
  --notify              send DBUS Desktop notification
  --email EMAIL_ADDRESS [EMAIL_ADDRESS ...]
                        email address to send to [+]

```

*Sent in body of messages. Other information from /proc/PID/status can easily be added by modifying the code.*

## Alternatives

If you are looking for a more substantial daemon monitoring system, people recommend [Monit](https://mmonit.com/monit)

> Monit is a small Open Source utility for managing and monitoring Unix systems. Monit conducts automatic maintenance and repair and can execute meaningful causal actions in error situations.

There is also [upstart](http://upstart.ubuntu.com), which Ubuntu and some other Linux distros have installed. See [Keeping Daemons alive with Upstart](http://www.alexreisner.com/code/upstart).


# Running

The program just runs until all processes end or forever if *--watch-new* is specified.

In Unix environments you can run a program in the background and disconnect from the terminal like this:
`nohup process_watcher ARGs &` 

## Examples
Send an email when process 1234 exits.

`process_watcher --pid 1234 --to me@gmail.com`

Watch all **myapp** processes and continue to watch for new ones. Send desktop notifications.

`process_watcher --command myapp --notify --watch-new`

Watch 2 PIDs, continue to watch for multiple command name patterns, email two people.

`process_watcher -p 4242 5655 -c myapp -c anotherapp -c "kworker/[24]" -w --email bob@gmail.com alice@gmail.com`

## Help

Arguments from **process_watcher --help**
```bash
-p means process id ,like -p 23 344 23423 ....
-c means command name, like -c top -c ps -c ping ....

```

# Optional Dependencies

## Desktop Notifications

Requires [notify2](https://notify2.readthedocs.org/en/latest)

`pip3 install notify2`

Requires **python-dbus**, which is easiest to install with your package manager:

`sudo apt-get install python3-dbus`

## Email

Uses Python's built-in email module. However, you will need to setup a local smtp server. 
[This tutorial](https://easyengine.io/tutorials/linux/ubuntu-postfix-gmail-smtp) shows how to setup Postfix with a GMail relay on Ubuntu. 
or config /usr/local/etc/process-watcher/watcher.conf
change the settings to your email sender

# Contributions

I created this after searching for a program to notify via email when a process ends. After a brief search, most suggestions I found were basic unix commands, such as on [StackExchange thread](http://unix.stackexchange.com/questions/55395/is-there-a-program-that-can-send-me-a-notification-e-mail-when-a-process-finishe).

So I decided to create this to refresh my Python skills and hopefully create something others find useful. I'm sure there are other programs that do the same thing, but if you think this code has promise and want to extend it, don't hesitate to send me a PR.

Fork from [arlowhite](https://github.com/arlowhite/process-watcher)

# Ideas & Bugs

These are some ideas and known issues I have; if any of these is particularly important to you, please create a GitHub issue (or PR) and describe your requirements and suggestions. Otherwise, I have no way of knowing what changes users want.

- Config file that specifies defaults so you don't need to specify email addresses or a different interval every time.
- Configure logging
- Define body message and /proc/PID/status fields in config
- Record other proc stats
- Rare race condition where a PID is found but ends before /proc/PID is read.
- Package so installable easily with pip
- MacOS support? Need someone to test.
- Other communication protocols. XMPP? Unix command
- Alert on high-memory and high-CPU usage
- Add --command-args option
- RegEx flags
- Make installable from pip
- [Pushover](https://pushover.net/) comm protocol
- IRC
- Separate communication code into another project after adding a few more protocols to make it more useful to people. Config file for setup and message templates. Investigate other python libs first. 
