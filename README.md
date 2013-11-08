
auto-pull
=====================

Auto pull is a web based interface for calling `git pull` remotely. It removes the need for ssh access to sync repositories in remote servers so it is ideal for non-programers who have no expreience with terminal or ssh.

#### Dependencies

The application requires `web.py` and `spawn-fcgi` to run. Also, `nginx` is used for routing but it is not required. 

#### Setup

Install the dependencies if you haven't already:

    sudo apt-get update
    sudo apt-get install nginx spawn-fcgi python-pip
    sudo pip install webpy
   
Move the files `pull.py`, `start` and `stop` into your repository. Then you need to change some strings in these files: `<PROJECT_PATH>` to your repo's path in both `start` and `stop`. You should also set a user name and a password in `pull.py`.

You can start and and stop interface by running corresponding scripts.

After that, add this code inside your server declaration (e.g in `/etc/nginx/nginx.conf`)

    location /pull {                                                        
        fastcgi_pass 127.0.0.1:17225;
        fastcgi_param PATH_INFO $fastcgi_script_name;
    fastcgi_param REQUEST_METHOD $request_method;
        fastcgi_param QUERY_STRING $query_string;
    fastcgi_param SERVER_NAME $server_name;
        fastcgi_param SERVER_PORT $server_port;
    fastcgi_param SERVER_PROTOCOL $server_protocol;
        fastcgi_param CONTENT_TYPE $content_type;
    fastcgi_param CONTENT_LENGTH $content_length;
        fastcgi_pass_header Authorization;
        fastcgi_intercept_errors off;
    }

Lastly, restart the nginx. Now, you can access the interface via `http://yourdomain/pull`.
