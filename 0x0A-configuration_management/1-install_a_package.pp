#Install flask from pip3

exec { 'install_flask_and_werkzeug':
  command     => '/usr/bin/pip3 install flask werkzeug',
  path        => ['/usr/bin'],
  environment => ['PIP_REQUIRE_VIRTUALENV=false'],
  unless      => '/usr/bin/pip3 show flask &>/dev/null && /usr/bin/pip3 show werkzeug &>/dev/null',
}
