# Fix Nginx server to handle huge amount of failed requests.
# Increase the ULIMIT of the default file

exec { 'increase max limit setting':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
