# Puppet Manifest to automatically configure
# an Nginx server using Puppet instead of Bash

exec { 'apt-get update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
}

file { 'index-html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file_line { 'redirect':
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'rewrite ^/redirect_me https://www.google.com permanent;',
  notify  => Service['nginx'],
  require => Package['nginx'],
}

exec {'HTTP header':
  command  => 'sudo sed -i "/server_name _;/a \        add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default'
  provider => 'shell'
}

service { 'nginx':
  ensure => running,
  enable => true,
}
