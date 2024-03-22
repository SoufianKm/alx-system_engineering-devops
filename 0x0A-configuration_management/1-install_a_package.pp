#Install werkzeug

exec {'pip3 install flask':
   require => Exec['python-installed'],
   command => '/usr/bin/pip3 install flask==2.1.0'
}
